from sqlalchemy import Column, Integer, String, Float
from src.database import Base

class Crop(Base):
    __tablename__ = "crops"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    water_requirement = Column(Float, nullable=False)