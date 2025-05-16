from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class ACConnectionInfo(Base):
    __tablename__ = "ac_connection_info"

    id = Column(Integer, primary_key=True, index=True)
    site_session_id = Column(Integer, ForeignKey("site_session.id"))

    ac_power_source = Column(String(255))
    if_diesel_generator_exist_how_many = Column(Integer)
    diesel_generator_1_capacity_kva = Column(Float)
    diesel_generator_1_operational_status = Column(String(255))
    diesel_generator_2_capacity_kva = Column(Float)
    diesel_generator_2_operational_status = Column(String(255))
    solar_system_capacity_kw = Column(Float)

    site_session = relationship("SiteSession", back_populates="ac_connection_info")
