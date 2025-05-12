from pydantic import BaseModel
from typing import Optional

class ACConnectionInfoBase(BaseModel):
    ac_power_source: Optional[str]
    if_diesel_generator_exist_how_many: Optional[int]
    diesel_generator_1_capacity_kva: Optional[float]
    diesel_generator_1_operational_status: Optional[str]
    diesel_generator_2_capacity_kva: Optional[float]
    diesel_generator_2_operational_status: Optional[str]
    solar_system_capacity_kw: Optional[float]

    class Config:
        from_attributes = True

class ACConnectionInfoCreate(BaseModel):
    site_session_id: int
    ac_power_source: str
    if_diesel_generator_exist_how_many: int
    diesel_generator_1_capacity_kva: float
    diesel_generator_1_operational_status: str
    diesel_generator_2_capacity_kva: float
    diesel_generator_2_operational_status: str
    solar_system_capacity_kw: float

    class Config:
        from_attributes = True

class ACConnectionInfoOut(ACConnectionInfoBase):
    id: int
    site_session_id: int

    class Config:
        from_attributes = True

class ACConnectionInfoResponse(BaseModel):
    id: int
    site_session_id: int
    ac_power_source: str
    if_diesel_generator_exist_how_many: int
    diesel_generator_1_capacity_kva: float
    diesel_generator_1_operational_status: str
    diesel_generator_2_capacity_kva: float
    diesel_generator_2_operational_status: str
    solar_system_capacity_kw: float

    class Config:
        from_attributes = True
