from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import declarative_base
from app.config.settings import settings  

engine = create_async_engine(settings.database_url, echo=True)
async_session = async_sessionmaker(bind=engine, expire_on_commit=False)
Base = declarative_base()

async def get_session():
    async with async_session() as session:
        yield session
