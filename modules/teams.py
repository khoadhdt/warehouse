# modules/teams.py
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


async def list_teams():
    """Lấy danh sách tất cả nhóm hoạt động."""
    conn = await get_connection()
    try:
        rows = await conn.fetch("""
            SELECT id, name, display_name, image_folder, invoice_folder, is_active
            FROM teams
            WHERE is_active = TRUE
            ORDER BY id
        """)
        return [dict(r) for r in rows]
    finally:
        await conn.close()


async def get_team_by_id(team_id: int):
    """Lấy thông tin team theo team_id (bao gồm image_folder, invoice_folder)"""
    conn = await get_connection()
    try:
        row = await conn.fetchrow("""
            SELECT id, name, display_name, image_folder, invoice_folder
            FROM teams
            WHERE id = $1
        """, team_id)
        return dict(row) if row else None
    finally:
        await conn.close()


async def get_team_by_name(team_name: str):
    """Lấy thông tin nhóm theo tên (EOL, FOL, TEST, SMT)."""
    conn = await get_connection()
    try:
        row = await conn.fetchrow("""
            SELECT id, name, display_name, image_folder, invoice_folder
            FROM teams
            WHERE name = $1
        """, team_name)
        return dict(row) if row else None
    finally:
        await conn.close()


async def create_team(name, display_name, image_folder, invoice_folder):
    """Thêm nhóm mới."""
    conn = await get_connection()
    try:
        await conn.execute("""
            INSERT INTO teams (name, display_name, image_folder, invoice_folder)
            VALUES ($1, $2, $3, $4)
            ON CONFLICT (name) DO NOTHING
        """, name, display_name, image_folder, invoice_folder)
    finally:
        await conn.close()
