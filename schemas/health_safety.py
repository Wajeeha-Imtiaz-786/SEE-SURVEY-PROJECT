from pydantic import BaseModel
from typing import Optional

class HealthSafetyBase(BaseModel):
    site_session_id: int

    access_road_safe: str
    site_access_secure: str
    safe_usage_access: str
    site_safe_environmental: str
    fence_installed: str
    access_to_equipment_safe: str
    walkways_trip_hazard_free: str
    walkways_radiation_safe: str
    emergency_exits_clear: str
    vehicles_condition_safe: str
    site_clean: str
    manual_handling_safe: str
    ladder_length_adequate: str
    special_permits: str
    ladders_condition_ok: str

    climbing_system_installed: str
    walking_path_safety: str
    mw_antennas_exclusion_zone: str
    non_auth_access_prevented: str
    bts_lighting_ok: str
    access_to_bts_safe: str
    walking_grids_installed: str

class HealthSafetyCreate(HealthSafetyBase):
    pass

class HealthSafetyOut(HealthSafetyBase):
    id: int

    class Config:
        orm_mode = True
