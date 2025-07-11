from sqlalchemy import Column, Integer, String
from app.db.database import Base

class Airport(Base):
    __tablename__ = "airports"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    city = Column(String, nullable=False)
    country = Column(String, nullable=False)
    iata_code = Column(String, unique=True, nullable=False)
