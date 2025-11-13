# warehouse_app/db/database.py
from contextlib import asynccontextmanager
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text  # ← QUAN TRỌNG
from config.settings import DATABASE_URL
import pandas as pd
import asyncio


engine = create_async_engine(
    DATABASE_URL,
    echo=False,
    future=True,
    connect_args={"ssl": False},
)

AsyncSessionLocal = sessionmaker(
    engine, expire_on_commit=False, class_=AsyncSession
)


@asynccontextmanager
async def get_session():
    async with AsyncSessionLocal() as session:
        yield session


class DatabaseHandler:
    def read_data(self, table_name: str, columns: list):
        return asyncio.run(self._read_async(table_name, columns))

    async def _read_async(self, table_name: str, columns: list):
        async with get_session() as session:
            query = text(f"SELECT {', '.join(columns)} FROM {table_name}")
            result = await session.execute(query)
            rows = result.fetchall()
            return pd.DataFrame(rows, columns=columns)
