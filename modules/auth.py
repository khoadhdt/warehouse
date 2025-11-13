# modules/auth.py
from config.settings import DB_HOST, DB_PORT, DB_USER, DB_PASS, DB_NAME
from passlib.context import CryptContext
import asyncpg
import warnings
warnings.filterwarnings("ignore", category=UserWarning, module="passlib")

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


async def get_connection():
    return await asyncpg.connect(
        user=DB_USER,
        password=DB_PASS,
        database=DB_NAME,
        host=DB_HOST,
        port=DB_PORT,
        ssl=False
    )


async def verify_user(username: str, password: str):
    """
    Kiểm tra thông tin đăng nhập.
    Trả về dict {id, username, role, team_id} nếu đúng,
    hoặc None nếu sai.
    """
    conn = await get_connection()
    try:
        row = await conn.fetchrow(
            "SELECT id, username, password, role, team_id FROM users WHERE username = $1",
            username
        )
        if not row:
            return None

        hashed_pw = row["password"]
        if pwd_context.verify(password, hashed_pw):
            return {
                "id": row["id"],
                "username": row["username"],
                "role": row["role"],
                "team_id": row["team_id"]
            }
        return None
    finally:
        await conn.close()


async def create_user(username: str, password: str, role: str = "user", team_id: int = 1):
    """
    Tạo người dùng mới (hash password).
    """
    conn = await get_connection()
    try:
        hashed_pw = pwd_context.hash(password)
        await conn.execute(
            """
            INSERT INTO users (username, password, role, team_id)
            VALUES ($1, $2, $3, $4)
            ON CONFLICT (username) DO NOTHING
            """,
            username, hashed_pw, role, team_id
        )
    finally:
        await conn.close()
