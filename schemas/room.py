from pydantic import BaseModel
from typing import Optional

class RoomInfoBase(BaseModel):
    height: float
    width: float
    depth: float
    telecom_hardware_type: str
    has_sketch: bool

class RoomInfoCreate(RoomInfoBase):
    pass

class RoomInfoOut(RoomInfoBase):
    id: int

    class Config:
        from_attributes = True

class RoomPreparationBase(BaseModel):
    air_condition_type: str
    air_condition_count: str
    air_condition_capacity: float
    air_condition_status: str
    cable_tray_clearance: float
    cable_tray_width: float
    has_space_on_cable_tray: bool
    has_space_in_feeders_window: bool
    free_holes_in_feeders_window: int
    bus_bar_count: int
    free_holes_in_bus_bars: int
    free_positions_for_racks: int

class RoomPreparationCreate(RoomPreparationBase):
    pass

class RoomPreparationOut(RoomPreparationBase):
    id: int

    class Config:
        from_attributes = True

class RANBase(BaseModel):
    equipment_vendor: str
    has_free_slots: bool
    rack_type_with_free_slots: str
    multiple_locations_available: str
    transmission_cable_length: float

class RANCreate(RANBase):
    pass

class RANOut(RANBase):
    id: int

    class Config:
        from_attributes = True
