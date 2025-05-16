from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, JSON
from database import Base
from sqlalchemy.orm import relationship

class SiteInformation(Base):
    __tablename__ = "site_information"

    id = Column(Integer, primary_key=True, autoincrement=True)
    id = Column(Integer, ForeignKey("site_location.id"), primary_key=True)
    site_session_id = Column(Integer, ForeignKey("site_session.id"))  # NEW
    site_location_id = Column(Integer, ForeignKey("site_location.site_id"))
    site_area = Column(String(255), nullable=False)
    site_ownership = Column(String(255), nullable=False)
    shared_site = Column(Boolean)
    telecom_operators = Column(JSON(String(255)))
    ac_power_sharing = Column(Boolean)
    dc_power_sharing = Column(Boolean)
    site_topology = Column(String(255), nullable=False)
    site_type = Column(String(255), nullable=False)
    planned_scope = Column(JSON(String(255)))
    existing_rack_cabinets = Column(JSON(String(255)))
    planned_rack_cabinets = Column(JSON(String(255)))
    existing_technology = Column(JSON(String(255)))
    site_session = relationship("SiteSession", back_populates="site_information")
