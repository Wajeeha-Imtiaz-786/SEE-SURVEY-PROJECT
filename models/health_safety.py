from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class HealthSafety(Base):
    __tablename__ = "health_safety"

    id = Column(Integer, primary_key=True, index=True)
    site_session_id = Column(Integer, ForeignKey("site_session.id"), nullable=False)

    # Site Access
    access_road_safe = Column(String(255))
    site_access_secure = Column(String(255))
    safe_usage_access = Column(String(255))
    site_safe_environmental = Column(String(255))
    fence_installed = Column(String(255))
    access_to_equipment_safe = Column(String(255))
    walkways_trip_hazard_free = Column(String(255))
    walkways_radiation_safe = Column(String(255))
    emergency_exits_clear = Column(String(255))
    vehicles_condition_safe = Column(String(255))
    site_clean = Column(String(255))
    manual_handling_safe = Column(String(255))
    ladder_length_adequate = Column(String(255))
    special_permits = Column(String(255))
    ladders_condition_ok = Column(String(255))

    # BTS/Antenna Access
    climbing_system_installed = Column(String(255))
    walking_path_safety = Column(String(255))
    mw_antennas_exclusion_zone = Column(String(255))
    non_auth_access_prevented = Column(String(255))
    bts_lighting_ok = Column(String(255))
    access_to_bts_safe = Column(String(255))
    walking_grids_installed = Column(String(255))
