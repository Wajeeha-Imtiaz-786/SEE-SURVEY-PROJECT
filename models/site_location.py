from sqlalchemy import Column, Integer, String, DECIMAL, ForeignKey
from database import Base
from sqlalchemy.orm import relationship

class SiteLocation(Base):
    __tablename__ = "site_location"

    id = Column(Integer, primary_key=True, autoincrement=True)
    #site_session_id = Column(Integer, ForeignKey("site_session.id"))  # NEW
    site_id = Column(String(255), nullable=False)
    site_name = Column(String(255), nullable=False)
    region = Column(String(255), nullable=False)
    city = Column(String(255), nullable=False)
    operator = Column(String(255), nullable=False)
    longitude = Column(DECIMAL(10,6), nullable=False)
    latitude = Column(DECIMAL(10,6), nullable=False)
    site_elevation = Column(DECIMAL(6,2))
    address = Column(String(255), nullable=False)
    #site_session = relationship("SiteSession", back_populates="site_location")
