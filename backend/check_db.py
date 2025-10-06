import asyncio
from sqlalchemy import text
from .database import engine, SessionLocal


async def main():
    async with engine.begin() as conn:
        r = await conn.execute(text("SELECT 1"))
        print("engine_ok:", r.scalar())

    async with SessionLocal() as session:
        r = await session.execute(text("SELECT 2"))
        print("session_ok:", r.scalar())

if __name__ == "__main__":
    asyncio.run(main())
