from pydantic import BaseModel
from typing import List, Optional, Literal

# ------------------------------
# Outdoor General Layout Info
# ------------------------------

class OutdoorGeneralLayoutInfoBase(BaseModel):
    site_session_id: int
    equipment_area_sunshade: Literal["Yes", "No", "Partially"]
    free_positions_for_new_cabinets: int  # 0-5
    cable_tray_height_cm: int
    cable_tray_width_cm: int
    cable_tray_depth_cm: int
    cable_tray_space_available: Literal["Yes", "No"]
    earth_bus_bar_count: int  # 1-3
    free_holes_in_bus_bars: int  # 1-3
    has_sketch_with_measurements: Literal["Yes", "No"]

class OutdoorGeneralLayoutInfoCreate(OutdoorGeneralLayoutInfoBase):
    pass

class OutdoorGeneralLayoutInfo(OutdoorGeneralLayoutInfoBase):
    id: int
    class Config:
        orm_mode = True

# ------------------------------
# Outdoor Cabinet
# ------------------------------

class OutdoorCabinetBase(BaseModel):
    site_session_id: int
    cabinet_index: int  # 1-based index for each cabinet
    cabinet_type: List[str]
    cabinet_vendor: Literal["Nokia", "Ericson", "Huawei", "ZTE", "Eltek", "Vertiv"]
    cabinet_model: str
    has_anti_theft: Literal["Yes", "No"]
    cooling_type: Literal["Air-condition", "Fan-filter"]
    cooling_capacity_watt: int
    compartment_count: Literal[1, 2]
    existing_hardware: List[str]
    has_ac_power_feed: Literal["Yes", "No"]
    ac_panel_cb_number: Optional[str] = None
    power_cable_length_meter: Optional[int] = None
    power_cable_cross_section_mm: Optional[int] = None
    has_blvd: Literal["Yes", "No"]
    blvd_has_free_cbs: Literal["Yes", "No"]
    has_llvd: Literal["Yes", "No"]
    llvd_has_free_cbs: Literal["Yes", "No"]
    has_pdu: Literal["Yes", "No"]
    pdu_has_free_cbs: Literal["Yes", "No"]
    internal_layout_suitable: Literal["Yes", "No", "Yes, with some modifications"]
    free_19u_for_telecom: int

class OutdoorCabinetCreate(OutdoorCabinetBase):
    pass

class OutdoorCabinet(OutdoorCabinetBase):
    id: int

    @classmethod
    def from_orm(cls, obj):
        # Convert comma-separated string to list for these fields
        data = obj.__dict__.copy()
        data['cabinet_type'] = obj.cabinet_type.split(',') if obj.cabinet_type else []
        data['existing_hardware'] = obj.existing_hardware.split(',') if obj.existing_hardware else []
        return cls(**data)

    class Config:
        orm_mode = True

# ------------------------------
# BLVD/LLVD/PDU CB Load Table (for each cabinet)
# ------------------------------

class CabinetCBLoadBase(BaseModel):
    cabinet_id: int
    label: str
    panel_id: int
    capacity_rate: float

class CabinetCBLoadCreate(CabinetCBLoadBase):
    pass

class CabinetCBLoad(CabinetCBLoadBase):
    id: int
    class Config:
        orm_mode = True

# ------------------------------
# MW Link Table (child of site_session_id)
# ------------------------------

class OutdoorMWLinkBase(BaseModel):
    site_session_id: int
    mw_link_index: int
    located_in: List[str]
    mw_equipment_vendor: str
    idu_type: str
    card_type_model: str
    destination_site_id: str
    mw_backhauling_type: Literal["Ethernet", "Fiber"]
    ethernet_ports_used: int
    ethernet_ports_free: int

class OutdoorMWLinkCreate(OutdoorMWLinkBase):
    pass

class OutdoorMWLink(OutdoorMWLinkBase):
    id: int
    class Config:
        orm_mode = True

# ------------------------------
# DC Rectifier Table (child of site_session_id)
# ------------------------------

class OutdoorDCRectifierBase(BaseModel):
    site_session_id: int
    location: str
    vendor: Literal["Nokia", "Ericson", "Huawei", "ZTE", "Other"]
    model: str
    module_count: int
    module_capacity_kw: float
    total_capacity_kw: float
    free_slots: int

class OutdoorDCRectifierCreate(OutdoorDCRectifierBase):
    pass

class OutdoorDCRectifier(OutdoorDCRectifierBase):
    id: int
    class Config:
        orm_mode = True

# ------------------------------
# Battery Table (child of site_session_id)
# ------------------------------

class OutdoorBatteryBase(BaseModel):
    site_session_id: int
    location: str
    vendor: Literal["Efore", "Enersys", "Leoch battery", "Narada", "Polarium", "Shoto", "Other"]
    battery_type: Literal["Lead acid", "Lithium"]
    string_count: int
    total_capacity_ah: int
    free_slots: int
    install_location: List[str]

class OutdoorBatteryCreate(OutdoorBatteryBase):
    pass

class OutdoorBattery(OutdoorBatteryBase):
    id: int
    class Config:
        orm_mode = True
