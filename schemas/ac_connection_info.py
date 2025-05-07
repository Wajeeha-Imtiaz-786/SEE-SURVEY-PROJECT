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

class ACConnectionInfoCreate(ACConnectionInfoBase):
    site_session_id: int

class ACConnectionInfoOut(ACConnectionInfoBase):
    id: int
    site_session_id: int

    class Config:
        from_attributes = True  # Updated from 'orm_mode'
        validate_by_name = True  # Updated from 'allow_population_by_field_name'
