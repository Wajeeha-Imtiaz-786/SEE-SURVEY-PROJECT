from pydantic import BaseModel
from typing import Optional

class PowerMeterBase(BaseModel):
    power_meter_serial_number: Optional[str]
    power_meter_reading: Optional[float]
    ac_power_source: Optional[str]
    length_power_cable_to_meter_m: Optional[float]
    cross_section_power_cable_to_meter_mm2: Optional[float]
    main_cb_rating_amp: Optional[float]
    main_cb_type: Optional[str]

class PowerMeterCreate(BaseModel):
    name: str
    description: str

class PowerMeterResponse(BaseModel):
    id: int
    name: str
    description: str

    class Config:
        from_attributes = True
