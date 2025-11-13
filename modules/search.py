# warehouse_app/modules/search.py
"""
TÌM KIẾM SIÊU TỐC - TẬN DỤNG INDEX ĐÃ TẠO
- GIN: array, tsvector
- pg_trgm: component_id, component_name
- Composite: team_id + created_at
- Full-text: plainto_tsquery('simple')
"""
from typing import List, Dict, Any, Optional
import asyncpg
from config.settings import DB_HOST, DB_PORT, DB_USER, DB_PASS, DB_NAME


async def get_connection() -> asyncpg.Connection:
    return await asyncpg.connect(
        user=DB_USER, password=DB_PASS, database=DB_NAME,
        host=DB_HOST, port=DB_PORT, ssl=False, timeout=10.0
    )


async def search_entries(
    team_id: int,
    movement_type: Optional[str] = None,
    filters: Optional[Dict[str, Any]] = None,
    limit: Optional[int] = None,   # ← None = FULL
    offset: int = 0,
) -> List[Dict[str, Any]]:
    filters = filters or {}
    where: List[str] = ["ie.team_id = $1"]
    params: List[Any] = [team_id]
    idx = 2

    # movement_type truyền vào từ filters hoặc trực tiếp
    movement_type = filters.pop("movement_type", None)
    if movement_type:
        if movement_type == "in":
            # lọc "in"
            where.append(f"ie.movement_type = ANY(${idx}::text[])")
            params.append(["in", "adjustment"])
        elif movement_type == "out":
            # lọc"out"
            where.append(f"ie.movement_type = ${idx}")
            params.append("out")
        idx += 1

    if filters.get("component_id_exact"):
        where.append(f"ie.component_id = ${idx}")
        params.append(filters["component_id_exact"])
        idx += 1
    elif filters.get("component_id"):
        where.append(f"ie.component_id ILIKE ${idx}")
        params.append(f"%{filters['component_id']}%")
        idx += 1

    if filters.get("component_name"):
        where.append(f"ie.component_name ILIKE ${idx}")
        params.append(f"%{filters['component_name']}%")
        idx += 1

    for key, col in [
        ("groups", "group_name"),
        ("process", "process"),
        ("model", "model"),
        ("material", "material"),
    ]:
        if filters.get(key) and isinstance(filters[key], (list, tuple)) and filters[key]:
            where.append(f"ie.{col} && ${idx}::text[]")
            params.append(filters[key])
            idx += 1

    for field in ("storage_location", "status"):
        val = filters.get(field)
        if val:
            if isinstance(val, (list, tuple)) and val:
                where.append(f"ie.{field} = ANY(${idx}::text[])")
                params.append(val)
            else:
                where.append(f"ie.{field} = ${idx}")
                params.append(val)
            idx += 1

    if filters.get("invoice"):
        where.append(f"ie.invoice ILIKE ${idx}")
        params.append(f"%{filters['invoice']}%")
        idx += 1

    if filters.get("modinvoice"):
        where.append(f"ie.modinvoice ILIKE ${idx}")
        params.append(f"%{filters['modinvoice']}%")
        idx += 1

    if filters.get("size"):
        where.append(f"ie.size ILIKE ${idx}")
        params.append(f"%{filters['size']}%")
        idx += 1

    if filters.get("note_contains"):
        where.append(f"ie.note ILIKE ${idx}")
        params.append(f"%{filters['note_contains']}%")
        idx += 1

    if filters.get("note_not_contains"):
        where.append(f"ie.note NOT ILIKE ${idx}")
        params.append(f"%{filters['note_not_contains']}%")
        idx += 1

    if filters.get("note_is_empty"):
        where.append("(ie.note IS NULL OR ie.note = '')")

    if filters.get("note_is_not_empty"):
        where.append("(ie.note IS NOT NULL AND ie.note != '')")

    if filters.get("created_from"):
        where.append(f"ie.created_at >= ${idx}")
        params.append(filters["created_from"])
        idx += 1
    if filters.get("created_to"):
        where.append(f"ie.created_at <= ${idx}")
        params.append(filters["created_to"])
        idx += 1

    if filters.get("q"):
        where.append(f"ie.search_vector @@ plainto_tsquery('simple', ${idx})")
        params.append(filters["q"])
        idx += 1

    where_sql = " AND ".join(where)

    limit_clause = ""
    if limit is not None:
        limit_clause = f"LIMIT ${idx} OFFSET ${idx + 1}"
        params.extend([limit, offset])
        idx += 1
    else:
        limit_clause = f"OFFSET ${idx}"
        params.append(offset)

    sql = f"""
        SELECT
            ie.id, ie.component_id, ie.component_name, ie.group_name,
            ie.process, ie.model, ie.size, ie.unit, ie.material,
            ie.storage_location, ie.invoice, ie.modinvoice,
            ie.status, ie.note, ie.quantity, ie.movement_type,
            ie.created_at, ie.created_by
        FROM inventory_entries ie
        WHERE {where_sql}
        ORDER BY ie.created_at DESC
        {limit_clause}
    """

    conn = await get_connection()
    try:
        rows = await conn.fetch(sql, *params)
        return [dict(r) for r in rows]
    finally:
        await conn.close()

# Tạo gợi ý đặt tên linh kiện


async def get_name_suggestions(team_id: int, prefix: str, limit: int = 10) -> List[str]:
    print(f"[SQL DEBUG] team_id={team_id}, prefix='{prefix}'")
    conn = await get_connection()
    try:
        sql = """
            SELECT DISTINCT ON (component_name) component_name
            FROM inventory_entries
            WHERE team_id = $1
              AND component_name ILIKE $2 || '%'
            ORDER BY component_name, similarity(component_name, $2) DESC
            LIMIT $3
        """
        rows = await conn.fetch(sql, team_id, prefix, limit)
        result = [row["component_name"] for row in rows]
        print(f"[SQL RESULT] {len(result)} gợi ý: {result}")
        return result
    except Exception as e:
        print(f"[SQL ERROR] {e}")
        return []
    finally:
        await conn.close()


async def search_current_stock(team_id: int, filters: dict):
    conn = await get_connection()
    try:
        sql = "SELECT * FROM current_stock WHERE team_id = $1"
        params = [team_id]
        idx = 2

        if "component_id" in filters:
            sql += f" AND component_id = ${idx}"
            params.append(filters["component_id"])
            idx += 1

        if "component_name_contains" in filters:
            sql += f" AND component_name ILIKE ${idx}"
            params.append(f"%{filters['component_name_contains']}%")
            idx += 1

        if "size" in filters:
            sql += f" AND size ILIKE ${idx}"
            params.append(f"%{filters['size']}%")
            idx += 1

        if "status" in filters:
            sql += f" AND status = ${idx}"
            params.append(filters["status"])
            idx += 1

        if "invoice" in filters:
            sql += f" AND invoice ILIKE ${idx}"
            params.append(f"%{filters['invoice']}%")
            idx += 1

        if "modinvoice" in filters:
            sql += f" AND modinvoice ILIKE ${idx}"
            params.append(f"%{filters['modinvoice']}%")
            idx += 1

        if "note_contains" in filters:
            sql += f" AND note ILIKE ${idx}"
            params.append(f"%{filters['note_contains']}%")
            idx += 1

        # Array filters
        for key in ["group_name", "process", "model", "material"]:
            if key in filters:
                for val in filters[key]:
                    sql += f" AND ${idx} = ANY({key})"
                    params.append(val)
                    idx += 1

        sql += " ORDER BY component_id LIMIT 1000"
        rows = await conn.fetch(sql, *params)
        return [dict(r) for r in rows]
    finally:
        await conn.close()
