import asyncio
from app.db.database import engine, Base
from app.models.models import Airport  # importa todos los modelos explícitamente

async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    print("✅ Tablas creadas exitosamente")

if __name__ == "__main__":
    asyncio.run(create_tables())
