from sqlalchemy import Column, Integer, String, DECIMAL
from database import Base

class SiteLocation(Base):
    __tablename__ = "site_location"

    id = Column(Integer, primary_key=True, autoincrement=True)
    site_id = Column(String(255), nullable=False)
    site_name = Column(String(255), nullable=False)
    region = Column(String(255), nullable=False)
    city = Column(String(255), nullable=False)
    longitude = Column(DECIMAL(10,6), nullable=False)
    latitude = Column(DECIMAL(10,6), nullable=False)
    site_elevation = Column(DECIMAL(6,2))
    address = Column(String(255), nullable=False)
