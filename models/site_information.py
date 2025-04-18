from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, JSON
from database import Base

class SiteInformation(Base):
    __tablename__ = "site_information"

    id = Column(Integer, primary_key=True, autoincrement=True)
    site_location_id = Column(Integer, ForeignKey("site_location.id"))
    site_area = Column(String(255), nullable=False)
    site_ownership = Column(String(255), nullable=False)
    shared_site = Column(Boolean)
    telecom_operators = Column(JSON(String(255)))
    ac_power_sharing = Column(Boolean)
    dc_power_sharing = Column(Boolean)
    site_topology = Column(String(255), nullable=False)
    site_type = Column(String(255), nullable=False)
    planned_scope = Column(JSON(String(255)))
    existing_rack_location = Column(JSON(String(255)))
    planned_rack_location = Column(JSON(String(255)))
    existing_technology = Column(JSON(String(255)))
