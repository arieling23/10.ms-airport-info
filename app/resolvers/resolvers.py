import strawberry
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException

from app.db.database import get_session
from app.services.airport_service import AirportService
from app.utils.logger import logger


@strawberry.type
class AirportType:
    id: int
    name: str
    city: str
    country: str
    iataCode: str  


def to_airport_type(airport) -> AirportType:
    return AirportType(
        id=airport.id,
        name=airport.name,
        city=airport.city,
        country=airport.country,
        iataCode=airport.iata_code  
    )


@strawberry.type
class Query:

    @strawberry.field
    async def airports(self, info) -> List[AirportType]:
        user = info.context.get("user")
        role = user.get("role")

        if role not in ["admin", "user"]:
            logger.warning(f"Acceso denegado para rol: {role}")
            raise HTTPException(status_code=403, detail="Acceso no autorizado")

        logger.info(f"Usuario autenticado ({user.get('sub')}) accedió a consulta de aeropuertos.")

        session_generator = get_session()
        session: AsyncSession = await session_generator.__anext__()

        data = await AirportService.list_airports(session)
        logger.debug(f"Se recuperaron {len(data)} aeropuertos desde la base de datos.")
        return [to_airport_type(a) for a in data]


@strawberry.type
class Mutation:

    @strawberry.mutation
    async def createAirport( 
        self,
        info,
        name: str,
        city: str,
        country: str,
        iataCode: str, 
    ) -> AirportType:
        user = info.context.get("user")
        logger.info(f"Usuario {user.get('sub')} está intentando crear un aeropuerto.")

        session_generator = get_session()
        session: AsyncSession = await session_generator.__anext__()

        airport = await AirportService.add_airport(session, {
            "name": name,
            "city": city,
            "country": country,
            "iata_code": iataCode,  
        })

        logger.info(f"Aeropuerto '{name}' creado exitosamente por {user.get('sub')}.")
        return to_airport_type(airport)
