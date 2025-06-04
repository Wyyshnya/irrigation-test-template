from sqlalchemy import Column, Integer, Float
from src.database import Base

class Soil(Base):
    __tablename__ = "soil"
    
    id = Column(Integer, primary_key=True, index=True)
    moisture_level = Column(Float, nullable=False)
    soil_type = Column(Integer, nullable=False)