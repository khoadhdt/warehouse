# modules/options.py
import asyncpg
from config.settings import DB_HOST, DB_PORT, DB_USER, DB_PASS, DB_NAME


async def get_connection():
    return await asyncpg.connect(
        user=DB_USER,
        password=DB_PASS,
        database=DB_NAME,
        host=DB_HOST,
        port=DB_PORT,
        ssl=False
    )


# ✅ Lấy danh sách theo category
async def get_options(team_id: int, category: str, only_active=True):
    conn = await get_connection()
    try:
        sql = """
            SELECT id, value, sort_order, is_active, created_at, updated_at
            FROM options
            WHERE team_id = $1 AND category = $2
        """
        if only_active:
            sql += " AND is_active = TRUE"
        sql += " ORDER BY sort_order, value"

        rows = await conn.fetch(sql, team_id, category)
        return [dict(r) for r in rows]
    finally:
        await conn.close()


# ✅ Thêm / cập nhật danh sách options
async def upsert_options(team_id: int, category: str, values: list[str], created_by: int = 0):
    conn = await get_connection()
    try:
        async with conn.transaction():
            # Xóa dữ liệu cũ
            await conn.execute(
                "DELETE FROM options WHERE team_id = $1 AND category = $2",
                team_id, category
            )

            # Thêm mới danh sách
            for idx, v in enumerate(values, start=1):
                await conn.execute("""
                    INSERT INTO options (
                        team_id, category, value, is_active, sort_order,
                        created_at, created_by, updated_at, updated_by
                    )
                    VALUES ($1, $2, $3, TRUE, $4, NOW(), $5, NOW(), $6)
                """, team_id, category, v.strip(), idx, created_by, created_by)
    finally:
        await conn.close()


# ✅ Xóa toàn bộ options theo team
async def clear_team_options(team_id: int):
    conn = await get_connection()
    try:
        await conn.execute("DELETE FROM options WHERE team_id = $1", team_id)
    finally:
        await conn.close()


# ✅ Lấy toàn bộ danh mục (grouped theo category)
async def get_all_categories(team_id: int):
    conn = await get_connection()
    try:
        rows = await conn.fetch("""
            SELECT category, value, sort_order, is_active
            FROM options
            WHERE team_id = $1 AND is_active = TRUE
            ORDER BY category, sort_order
        """, team_id)

        result = {}
        for r in rows:
            cat = r["category"]
            result.setdefault(cat, []).append(r["value"])
        return result
    finally:
        await conn.close()
