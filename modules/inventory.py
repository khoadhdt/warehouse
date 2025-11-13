# warehouse_app/modules/inventory.py
import asyncpg
from config.settings import DB_HOST, DB_PORT, DB_USER, DB_PASS, DB_NAME
import re
from typing import Optional, Dict


async def get_connection():
    """Kết nối asyncpg – dùng cho test & các hàm khác."""
    return await asyncpg.connect(
        user=DB_USER,
        password=DB_PASS,
        database=DB_NAME,
        host=DB_HOST,
        port=DB_PORT,
        ssl=False,
    )

# ----------------------------------------------------------------------
# 1. Edit entry – update
# ----------------------------------------------------------------------


async def update_entry(
    id: int, component_id: str, component_name: str, group_name: list[str],
    process: list[str], model: list[str], size: str, unit: str,
    team_id: int, material: list[str], storage_location: str,
    invoice: str, modinvoice: str, status: str, note: str,
    quantity: float, created_by: int
    # ← XÓA movement_type KHỎI THAM SỐ
):
    conn = await get_connection()
    try:
        async with conn.transaction():
            # Lấy dữ liệu cũ để audit
            old_data = await conn.fetchrow(
                "SELECT to_jsonb(t) FROM inventory_entries t WHERE id=$1", id
            )

            # Cập nhật – KHÔNG ĐỘNG VÀO movement_type
            sql = """
                UPDATE inventory_entries SET
                    component_id=$1, component_name=$2, group_name=$3, process=$4,
                    model=$5, size=$6, unit=$7, material=$8, storage_location=$9,
                    invoice=$10, modinvoice=$11, status=$12, note=$13,
                    quantity=$14, updated_by=$15, updated_at=NOW()
                WHERE id=$16 AND team_id=$17
                RETURNING id
            """
            row = await conn.fetchrow(sql,
                                      component_id, component_name, group_name, process, model, size, unit,
                                      material, storage_location, invoice, modinvoice, status, note,
                                      quantity, created_by, id, team_id
                                      )

            # Audit log
            await conn.execute("""
                INSERT INTO audit_log (table_name, record_id, action, old_row_data, new_row_data, changed_by)
                VALUES ('inventory_entries', $1, 'U', $2,
                        (SELECT row_to_json(t) FROM inventory_entries t WHERE t.id = $1),
                        $3)
            """, id, old_data["to_jsonb"], created_by)

        await refresh_current_stock()
        return row["id"]
    finally:
        await conn.close()

# ----------------------------------------------------------------------
# 2. Thêm phiếu nhập / xuất / điều chỉnh
# ----------------------------------------------------------------------


async def add_entry(
    component_id: str, component_name: str, group_name: list[str],
    process: list[str], model: list[str], size: str, unit: str,
    team_id: int, material: list[str], storage_location: str,
    invoice: str, modinvoice: str, status: str, note: str,
    quantity: float, movement_type: str, created_by: int
):
    conn = await get_connection()
    try:
        async with conn.transaction():
            sql = """
                INSERT INTO inventory_entries (
                    component_id, component_name, group_name, process, model, size,
                    unit, team_id, material, storage_location, invoice, modinvoice,
                    status, note, quantity, movement_type, created_by, updated_by,
                    created_at, updated_at
                )
                VALUES ($1,$2,$3,$4,$5,$6,$7,$8,$9,$10,$11,$12,$13,$14,$15,$16,$17,$18,NOW(),NOW())
                RETURNING id
            """
            row = await conn.fetchrow(
                sql,
                component_id, component_name, group_name, process, model, size, unit,
                team_id, material, storage_location, invoice, modinvoice, status,
                note, quantity, movement_type, created_by, created_by,
            )
            entry_id = row["id"]

            # audit log
            await conn.execute(
                """
                INSERT INTO audit_log (table_name, record_id, action, new_row_data, changed_by)
                VALUES ('inventory_entries', $1, 'I',
                        (SELECT row_to_json(t) FROM inventory_entries t WHERE t.id = $1),
                        $2)
                """,
                entry_id, created_by,
            )
        # luôn làm mới tồn kho ngay sau khi thêm
        await refresh_current_stock()
        return entry_id
    finally:
        await conn.close()


# ----------------------------------------------------------------------
# 3. Liệt kê giao dịch gần nhất (được dùng trong test)
# ----------------------------------------------------------------------
async def list_entries(team_id: int, limit: int = 50):
    """Lấy `limit` giao dịch mới nhất của team."""
    conn = await get_connection()
    try:
        rows = await conn.fetch(
            """
            SELECT id, component_id, component_name, group_name, quantity,
                   unit, movement_type, status, created_at, note
            FROM inventory_entries
            WHERE team_id = $1
            ORDER BY created_at DESC
            LIMIT $2
            """,
            team_id, limit,
        )
        return [dict(r) for r in rows]
    finally:
        await conn.close()


# ----------------------------------------------------------------------
# 4. Tồn kho hiện tại (materialized view)
# ----------------------------------------------------------------------
async def get_current_stock(team_id: int, component_filter: str = ""):
    conn = await get_connection()
    try:
        sql = """
            SELECT component_id, component_name, current_quantity, unit, status, note
            FROM current_stock
            WHERE team_id = $1
        """
        params = [team_id]
        if component_filter:
            sql += " AND component_id ILIKE $2"
            params.append(f"%{component_filter}%")
        sql += " ORDER BY component_id"
        rows = await conn.fetch(sql, *params)
        return [dict(r) for r in rows]
    finally:
        await conn.close()


# ----------------------------------------------------------------------
# 5. Làm mới materialized view (CONCURRENTLY)
# ----------------------------------------------------------------------
async def refresh_current_stock():
    conn = await get_connection()
    try:
        await conn.execute("REFRESH MATERIALIZED VIEW CONCURRENTLY current_stock")
    finally:
        await conn.close()


# ----------------------------------------------------------------------
# 6. Xóa giao dịch + audit log
# ----------------------------------------------------------------------
async def delete_entry(entry_id: int, user_id: int):
    conn = await get_connection()
    try:
        async with conn.transaction():
            old_data = await conn.fetchrow(
                "SELECT to_jsonb(t) FROM inventory_entries t WHERE id=$1", entry_id
            )
            await conn.execute("DELETE FROM inventory_entries WHERE id=$1", entry_id)
            await conn.execute(
                """
                INSERT INTO audit_log (table_name, record_id, action, old_row_data, changed_by)
                VALUES ('inventory_entries', $1, 'D', $2, $3)
                """,
                entry_id, old_data["to_jsonb"], user_id,
            )
        await refresh_current_stock()
    finally:
        await conn.close()

# ----------------------------------------------------------------------
# 7. Sinh Component ID
# ----------------------------------------------------------------------


# modules/inventory.py
async def generate_next_cid(storage_location: str) -> str:
    conn = await get_connection()
    try:
        suffix = storage_location.strip().split()[-1].upper()
        if len(suffix) < 3:
            return ""

        prefix = suffix  # VE02
        pattern = f"{prefix}___"  # VE02___

        # DÙNG SQL: Tìm số lớn nhất trong 3 chữ số cuối
        sql = """
            SELECT MAX(CAST(RIGHT(component_id, 3) AS INTEGER)) AS max_num
            FROM inventory_entries
            WHERE component_id LIKE $1
        """
        row = await conn.fetchrow(sql, f"{prefix}%")

        max_num = row["max_num"] or 0
        next_num = max_num + 1
        return f"{prefix}{str(next_num).zfill(3)}"

    except Exception as e:
        print(f"[generate_next_cid] Lỗi: {e}")
        return ""
    finally:
        await conn.close()

# inventory.py → THÊM HÀM NÀY


async def get_component_info_from_stock(team_id: int, component_id: str) -> Optional[Dict[str, any]]:
    """
    Lấy toàn bộ thông tin linh kiện từ current_stock (Materialized View)
    """
    sql = """
        SELECT 
            component_id, component_name, group_name, process, model, size, unit,
            material, storage_location, invoice, modinvoice, status, note,
            current_quantity
        FROM current_stock 
        WHERE team_id = $1 AND component_id = $2
    """
    conn = await get_connection()
    try:
        row = await conn.fetchrow(sql, team_id, component_id)
        return dict(row) if row else None
    finally:
        await conn.close()
