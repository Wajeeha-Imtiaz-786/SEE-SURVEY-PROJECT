from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DECIMAL, JSON
from database import Base
from sqlalchemy.orm import relationship

class SiteAccess(Base):
    __tablename__ = "site_access"

    id = Column(Integer, primary_key=True, autoincrement=True)
    site_session_id = Column(Integer, ForeignKey("site_session.id"))  # NEW
    site_location_id = Column(Integer, ForeignKey("site_location.id"))
    access_permission = Column(Boolean)
    crane_access_time = Column(JSON(String(255)))
    site_access_contact = Column(String(255))
    site_access_phone = Column(String(255))
    available_access_time = Column(JSON(String(255)))
    road_access = Column(String(255), nullable=False)
    gated_fence = Column(String(255), nullable=False)
    keys_required = Column(String(255), nullable=False)
    key_types = Column(JSON(String(255)))
    key_contact_person = Column(String(255))
    key_contact_phone = Column(String(255))
    material_access = Column(JSON(String(255)))
    stair_lift_height = Column(DECIMAL(6,2))
    stair_lift_width = Column(DECIMAL(6,2))
    stair_lift_depth = Column(DECIMAL(6,2))
    site_session_id = Column(Integer, ForeignKey("site_session.id"))
    site_session = relationship("SiteSession", back_populates="site_access")