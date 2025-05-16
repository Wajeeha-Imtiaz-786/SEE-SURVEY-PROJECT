from pydantic import BaseModel
from typing import Optional, List


# ---------------- RoomInfo ----------------
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


# ---------------- RoomPreparation ----------------
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


# ---------------- RAN ----------------
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


# ---------------- MW Link (Child Table) ----------------
class MWLinkBase(BaseModel):
    destination_site_id: str
    mw_equipment_vendor: str  # radio button: Nokia / Ericson / Huawei / ZTE / Other
    idu_type: str
    card_type_model: str
    mw_backhauling_type: str  # radio button: Ethernet / Fiber
    ethernet_ports_used: int
    ethernet_ports_free: int

class MWLinkCreate(MWLinkBase):
    pass

class MWLinkOut(MWLinkBase):
    id: int

    class Config:
        from_attributes = True


# ---------------- Transmission / MW ----------------
class TransmissionMWBase(BaseModel):
    type_of_transmission: str  # radio button: Fiber / MW / Not exist
    transmission_equipment_vendor: List[str]  # checkboxes
    cable_length_from_odf_to_baseband: float
    odf_fiber_cable_type: str  # radio button: LC / SC / FC
    free_ports_on_odf: int
    mw_links_exist: int  # drop down: 1 to 10
    space_available_for_mw_idu_installation: List[str]  # checkboxes

class TransmissionMWCreate(TransmissionMWBase):
    mw_links: List[MWLinkCreate] = []

class TransmissionMWOut(TransmissionMWBase):
    id: int
    mw_links: List[MWLinkOut] = []

    class Config:
        from_attributes = True

from pydantic import BaseModel
from typing import Optional


class MWLinkUpdate(BaseModel):
    mw_type: Optional[str]
    frequency_band: Optional[str]
    channel_bandwidth: Optional[str]
    hop_length: Optional[str]
    tx_frequency: Optional[str]
    rx_frequency: Optional[str]
    tx_power: Optional[str]
    rx_power: Optional[str]
    antenna_size: Optional[str]
    polarization: Optional[str]
    transmission_mw_id: Optional[int]

    class Config:
        orm_mode = True
# ---------------- DCPowerSystem ----------------

class CBLoadBase(BaseModel):
    label: str
    capacity: str


class BLVDCBLoadCreate(CBLoadBase):
    pass


class LLVDCBLoadCreate(CBLoadBase):
    pass


class PDUCBLoadCreate(CBLoadBase):
    pass


class DCPowerSystemBase(BaseModel):
    existing_dc_equipment_vendor: str
    existing_dc_power_rack: int
    existing_rectifier_modules: int
    rectifier_module_model: str
    rectifier_module_capacity: int
    free_slots_new_rectifier: int
    is_blvd_available: str
    blvd_has_free_cbs: str
    is_llvd_available: str
    llvd_has_free_cbs: str
    is_pdu_available: str
    pdu_has_free_cbs: str
    battery_strings: int
    battery_type: str
    battery_vendor: str
    total_battery_capacity: int

    blvd_cb_loads: List[BLVDCBLoadCreate]
    llvd_cb_loads: List[LLVDCBLoadCreate]
    pdu_cb_loads: List[PDUCBLoadCreate]


class DCPowerSystemCreate(DCPowerSystemBase):
    site_session_id: int


class DCPowerSystemOut(DCPowerSystemBase):
    id: int

    class Config:
        orm_mode = True
