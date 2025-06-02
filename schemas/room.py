from pydantic import BaseModel, Field
from typing import List, Optional, Literal

# ------------------------------
# RoomInfo Schemas
# ------------------------------

class RoomInfoBase(BaseModel):
    site_session_id: int
    height: float
    width: float
    depth: float
    telecom_hardware_type: str
    has_sketch: bool

class RoomInfoCreate(RoomInfoBase):
    pass

class RoomInfoUpdate(BaseModel):
    height: Optional[float] = None
    width: Optional[float] = None
    depth: Optional[float] = None
    telecom_hardware_type: Optional[str] = None
    has_sketch: Optional[bool] = None

class RoomInfo(RoomInfoBase):
    id: int
    class Config:
        orm_mode = True

class RoomInfoOut(RoomInfo):
    pass

# ------------------------------
# RoomPreparation Schemas
# ------------------------------

class RoomPreparationBase(BaseModel):
    site_session_id: int
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

class RoomPreparationUpdate(BaseModel):
    air_condition_type: Optional[str] = None
    air_condition_count: Optional[str] = None
    air_condition_capacity: Optional[float] = None
    air_condition_status: Optional[str] = None
    cable_tray_clearance: Optional[float] = None
    cable_tray_width: Optional[float] = None
    has_space_on_cable_tray: Optional[bool] = None
    has_space_in_feeders_window: Optional[bool] = None
    free_holes_in_feeders_window: Optional[int] = None
    bus_bar_count: Optional[int] = None
    free_holes_in_bus_bars: Optional[int] = None
    free_positions_for_racks: Optional[int] = None

class RoomPreparation(RoomPreparationBase):
    id: int
    class Config:
        orm_mode = True

class RoomPreparationOut(RoomPreparation):
    pass

# ------------------------------
# RAN Schemas
# ------------------------------

class RANBase(BaseModel):
    site_session_id: int
    equipment_vendor: str
    has_free_slots: bool
    rack_type_with_free_slots: str
    multiple_locations_available: str
    transmission_cable_length: float

class RANCreate(RANBase):
    pass

class RANUpdate(BaseModel):
    equipment_vendor: Optional[str] = None
    has_free_slots: Optional[bool] = None
    rack_type_with_free_slots: Optional[str] = None
    multiple_locations_available: Optional[str] = None
    transmission_cable_length: Optional[float] = None

class RAN(RANBase):
    id: int
    class Config:
        orm_mode = True

class RANOut(RAN):
    pass

# ------------------------------
# MWLink Schemas
# ------------------------------

class MWLinkBase(BaseModel):
    transmission_mw_id: int
    destination_site_id: str
    mw_equipment_vendor: str
    idu_type: str
    card_type_model: str
    mw_backhauling_type: str
    ethernet_ports_used: int
    ethernet_ports_free: int

class MWLinkCreate(MWLinkBase):
    pass

class MWLinkUpdate(BaseModel):
    destination_site_id: Optional[str] = None
    mw_equipment_vendor: Optional[str] = None
    idu_type: Optional[str] = None
    card_type_model: Optional[str] = None
    mw_backhauling_type: Optional[str] = None
    ethernet_ports_used: Optional[int] = None
    ethernet_ports_free: Optional[int] = None

class MWLink(MWLinkBase):
    id: int
    class Config:
        orm_mode = True

class MWLinkOut(MWLink):
    pass

# ------------------------------
# TransmissionMW Schemas
# ------------------------------

class TransmissionMWBase(BaseModel):
    site_session_id: int
    type_of_transmission: str
    transmission_equipment_vendor: str
    cable_length_from_odf_to_baseband: float
    odf_fiber_cable_type: str
    free_ports_on_odf: int
    mw_links_exist: int
    space_available_for_mw_idu_installation: str

class TransmissionMWCreate(TransmissionMWBase):
    pass

class TransmissionMWUpdate(BaseModel):
    type_of_transmission: Optional[str] = None
    transmission_equipment_vendor: Optional[str] = None
    cable_length_from_odf_to_baseband: Optional[float] = None
    odf_fiber_cable_type: Optional[str] = None
    free_ports_on_odf: Optional[int] = None
    mw_links_exist: Optional[int] = None
    space_available_for_mw_idu_installation: Optional[str] = None

class TransmissionMW(TransmissionMWBase):
    id: int
    mw_links: List[MWLink] = []
    class Config:
        orm_mode = True

class TransmissionMWOut(TransmissionMW):
    pass

# ------------------------------
# DCPowerSystem Schemas
# ------------------------------

class DCPowerSystemBase(BaseModel):
    site_session_id: int
    existing_dc_equipment_vendor: Optional[Literal["Nokia", "Ericson", "Huawei", "ZTE", "Other"]] = None
    existing_dc_power_rack: Optional[int] = None
    existing_rectifier_modules: Optional[int] = None
    rectifier_module_model: Optional[str] = None
    rectifier_module_capacity: Optional[int] = None
    free_slots_new_rectifier: Optional[int] = None
    is_blvd_available: Optional[Literal["Yes", "No"]] = None
    blvd_has_free_cbs: Optional[Literal["Yes", "No"]] = None
    is_llvd_available: Optional[Literal["Yes", "No"]] = None
    llvd_has_free_cbs: Optional[Literal["Yes", "No"]] = None
    is_pdu_available: Optional[Literal["Yes", "No"]] = None
    pdu_has_free_cbs: Optional[Literal["Yes", "No"]] = None
    battery_strings: Optional[int] = None
    battery_type: Optional[Literal["Lead acid", "Lithium"]] = None
    battery_vendor: Optional[str] = None
    total_battery_capacity: Optional[int] = None

class DCPowerSystemCreate(DCPowerSystemBase):
    pass

class DCPowerSystemUpdate(BaseModel):
    existing_dc_equipment_vendor: Optional[Literal["Nokia", "Ericson", "Huawei", "ZTE", "Other"]] = None
    existing_dc_power_rack: Optional[int] = None
    existing_rectifier_modules: Optional[int] = None
    rectifier_module_model: Optional[str] = None
    rectifier_module_capacity: Optional[int] = None
    free_slots_new_rectifier: Optional[int] = None
    is_blvd_available: Optional[Literal["Yes", "No"]] = None
    blvd_has_free_cbs: Optional[Literal["Yes", "No"]] = None
    is_llvd_available: Optional[Literal["Yes", "No"]] = None
    llvd_has_free_cbs: Optional[Literal["Yes", "No"]] = None
    is_pdu_available: Optional[Literal["Yes", "No"]] = None
    pdu_has_free_cbs: Optional[Literal["Yes", "No"]] = None
    battery_strings: Optional[int] = None
    battery_type: Optional[Literal["Lead acid", "Lithium"]] = None
    battery_vendor: Optional[str] = None
    total_battery_capacity: Optional[int] = None

class BLVDCBLoadBase(BaseModel):
    dc_power_system_id: int
    label: Optional[str] = None
    capacity: Optional[str] = None

class BLVDCBLoadCreate(BLVDCBLoadBase):
    pass

class BLVDCBLoad(BLVDCBLoadBase):
    id: int
    class Config:
        orm_mode = True

class BLVDCBLoadOut(BLVDCBLoad):
    pass

class LLVDCBLoadBase(BaseModel):
    dc_power_system_id: int
    label: Optional[str] = None
    capacity: Optional[str] = None

class LLVDCBLoadCreate(LLVDCBLoadBase):
    pass

class LLVDCBLoad(LLVDCBLoadBase):
    id: int
    class Config:
        orm_mode = True

class LLVDCBLoadOut(LLVDCBLoad):
    pass

class PDUCBLoadBase(BaseModel):
    dc_power_system_id: int
    label: Optional[str] = None
    capacity: Optional[str] = None

class PDUCBLoadCreate(PDUCBLoadBase):
    pass

class PDUCBLoad(PDUCBLoadBase):
    id: int
    class Config:
        orm_mode = True

class PDUCBLoadOut(PDUCBLoad):
    pass

class DCPowerSystem(DCPowerSystemBase):
    id: int
    blvd_cb_loads: List[BLVDCBLoad] = []
    llvd_cb_loads: List[LLVDCBLoad] = []
    pdu_cb_loads: List[PDUCBLoad] = []
    class Config:
        orm_mode = True
