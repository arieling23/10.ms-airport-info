
from app.repositories.airport_repository import AirportRepository
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException

class AirportService:

    @staticmethod
    async def list_airports(session: AsyncSession):
        return await AirportRepository.get_all(session)

    @staticmethod
    async def add_airport(session: AsyncSession, data: dict):
        existing = await AirportRepository.get_by_iata_code(session, data["iata_code"])
        if existing:
            raise HTTPException(status_code=400, detail="El código IATA ya existe.")
        return await AirportRepository.create(session, data)
