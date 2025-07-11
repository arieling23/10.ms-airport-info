from app.models.models import Airport
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

class AirportRepository:

    @staticmethod
    async def get_all(session: AsyncSession):
        result = await session.execute(select(Airport))
        return result.scalars().all()

    @staticmethod
    async def create(session: AsyncSession, data: dict):
        airport = Airport(**data)
        session.add(airport)
        await session.commit()
        await session.refresh(airport)
        return airport

    @staticmethod
    async def get_by_iata_code(session: AsyncSession, iata_code: str):
        result = await session.execute(
            select(Airport).where(Airport.iata_code == iata_code)
        )
        return result.scalars().first()
