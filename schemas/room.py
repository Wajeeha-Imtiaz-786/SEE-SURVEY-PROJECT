from pydantic import BaseModel
from typing import Optional, List


# ------------------------------
# RoomInfo Schemas
# ------------------------------

class RoomInfoBase(BaseModel):
    site_session_id: int
    room_name: Optional[str]
    floor_number: Optional[int]

class RoomInfoCreate(RoomInfoBase):
    pass

class RoomInfoUpdate(BaseModel):
    room_name: Optional[str] = None
    floor_number: Optional[int] = None

class RoomInfo(RoomInfoBase):
    id: int

    class Config:
        orm_mode = True

class RoomInfoOut(BaseModel):
    id: int
    site_session_id: int
    room_name: Optional[str]
    floor_number: Optional[int]

    class Config:
        orm_mode = True


# ------------------------------
# DCSystem Schemas
# ------------------------------

class DCSystemBase(BaseModel):
    site_session_id: int
    manufacturer: Optional[str]
    model: Optional[str]
    capacity_ah: Optional[float]
    battery_type: Optional[str]
    installation_date: Optional[str]

class DCSystemCreate(DCSystemBase):
    pass

class DCSystemUpdate(BaseModel):
    manufacturer: Optional[str] = None
    model: Optional[str] = None
    capacity_ah: Optional[float] = None
    battery_type: Optional[str] = None
    installation_date: Optional[str] = None

class DCSystem(DCSystemBase):
    id: int

    class Config:
        orm_mode = True


# ------------------------------
# BLVD Schemas
# ------------------------------

class BLVDBase(BaseModel):
    dc_system_id: int
    cb_rating: Optional[str]
    load_connected: Optional[str]

class BLVDCreate(BLVDBase):
    pass

class BLVDUpdate(BaseModel):
    cb_rating: Optional[str] = None
    load_connected: Optional[str] = None

class BLVD(BLVDBase):
    id: int

    class Config:
        orm_mode = True


# ------------------------------
# BLVDCBLoad Schemas
# ------------------------------

class BLVDCBLoadBase(BaseModel):
    dc_power_system_id: int
    cb_rating: Optional[str]
    load_connected: Optional[str]

class BLVDCBLoadCreate(BLVDCBLoadBase):
    pass

class BLVDCBLoadOut(BLVDCBLoadBase):
    id: int

    class Config:
        orm_mode = True


# ------------------------------
# LLVD Schemas
# ------------------------------

class LLVDBase(BaseModel):
    dc_system_id: int
    cb_rating: Optional[str]
    load_connected: Optional[str]

class LLVDCreate(LLVDBase):
    pass

class LLVDUpdate(BaseModel):
    cb_rating: Optional[str] = None
    load_connected: Optional[str] = None

class LLVD(LLVDBase):
    id: int

    class Config:
        orm_mode = True


# ------------------------------
# LLVDCBLoad Schemas
# ------------------------------

class LLVDCBLoadBase(BaseModel):
    dc_power_system_id: int
    cb_rating: Optional[str]
    load_connected: Optional[str]

class LLVDCBLoadCreate(LLVDCBLoadBase):
    pass

class LLVDCBLoadOut(LLVDCBLoadBase):
    id: int

    class Config:
        orm_mode = True


# ------------------------------
# PDUCB Schemas
# ------------------------------

class PDUCBBase(BaseModel):
    dc_system_id: int
    cb_rating: Optional[str]
    load_connected: Optional[str]

class PDUCBCreate(PDUCBBase):
    pass

class PDUCBUpdate(BaseModel):
    cb_rating: Optional[str] = None
    load_connected: Optional[str] = None

class PDUCB(PDUCBBase):
    id: int

    class Config:
        orm_mode = True


# ------------------------------
# PDUCBLoad Schemas
# ------------------------------

class PDUCBLoadBase(BaseModel):
    dc_system_id: int
    cb_rating: Optional[str]
    load_connected: Optional[str]

class PDUCBLoadCreate(PDUCBLoadBase):
    pass

class PDUCBLoadOut(PDUCBLoadBase):
    id: int

    class Config:
        orm_mode = True


# ------------------------------
# RoomPreparation Schemas
# ------------------------------

class RoomPreparationBase(BaseModel):
    site_session_id: int
    preparation_type: Optional[str]
    notes: Optional[str]

class RoomPreparationCreate(RoomPreparationBase):
    pass

class RoomPreparationUpdate(BaseModel):
    preparation_type: Optional[str] = None
    notes: Optional[str] = None

class RoomPreparation(RoomPreparationBase):
    id: int

    class Config:
        orm_mode = True

class RoomPreparationOut(BaseModel):
    id: int
    site_session_id: int
    preparation_type: Optional[str]
    notes: Optional[str]

    class Config:
        orm_mode = True


# ------------------------------
# RAN Schemas
# ------------------------------

class RANBase(BaseModel):
    site_session_id: int
    ran_vendor: Optional[str]
    free_slots: Optional[int]
    rack_type: Optional[str]
    location_options: Optional[List[str]]
    transmission_cable_length: Optional[float]

class RANCreate(RANBase):
    pass

class RANUpdate(BaseModel):
    ran_vendor: Optional[str] = None
    free_slots: Optional[int] = None
    rack_type: Optional[str] = None
    location_options: Optional[List[str]] = None
    transmission_cable_length: Optional[float] = None

class RAN(RANBase):
    id: int

    class Config:
        orm_mode = True

class RANOut(BaseModel):
    id: int
    site_session_id: int
    ran_vendor: Optional[str]
    free_slots: Optional[int]
    rack_type: Optional[str]
    location_options: Optional[List[str]]
    transmission_cable_length: Optional[float]

    class Config:
        orm_mode = True


# ------------------------------
# TransmissionMW Schemas
# ------------------------------

class TransmissionMWBase(BaseModel):
    site_session_id: int
    type_of_transmission: Optional[str]
    transmission_equipment_vendor: Optional[List[str]]
    cable_length_from_odf_to_baseband: Optional[float]
    odf_fiber_cable_type: Optional[str]
    free_ports_on_odf: Optional[int]
    mw_links_exist: Optional[int]
    space_available_for_mw_idu_installation: Optional[List[str]]
    mw_links: Optional[List[str]]

class TransmissionMWCreate(TransmissionMWBase):
    pass

class TransmissionMWUpdate(BaseModel):
    type_of_transmission: Optional[str] = None
    transmission_equipment_vendor: Optional[List[str]] = None
    cable_length_from_odf_to_baseband: Optional[float] = None
    odf_fiber_cable_type: Optional[str] = None
    free_ports_on_odf: Optional[int] = None
    mw_links_exist: Optional[int] = None
    space_available_for_mw_idu_installation: Optional[List[str]] = None
    mw_links: Optional[List[str]] = None

class TransmissionMW(TransmissionMWBase):
    id: int

    class Config:
        orm_mode = True

class TransmissionMWOut(BaseModel):
    id: int
    site_session_id: int
    type_of_transmission: Optional[str]
    transmission_equipment_vendor: Optional[List[str]]
    cable_length_from_odf_to_baseband: Optional[float]
    odf_fiber_cable_type: Optional[str]
    free_ports_on_odf: Optional[int]
    mw_links_exist: Optional[int]
    space_available_for_mw_idu_installation: Optional[List[str]]
    mw_links: Optional[List[str]]

    class Config:
        orm_mode = True


# ------------------------------
# MWLink Schemas
# ------------------------------

class MWLinkBase(BaseModel):
    transmission_mw_id: int
    destination_site_id: Optional[str]
    mw_equipment_vendor: Optional[str]
    idu_type: Optional[str]
    card_type_model: Optional[str]
    mw_backhauling_type: Optional[str]
    ethernet_ports_used: Optional[int]
    ethernet_ports_free: Optional[int]

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

class MWLinkOut(BaseModel):
    id: int
    transmission_mw_id: int
    destination_site_id: Optional[str]
    mw_equipment_vendor: Optional[str]
    idu_type: Optional[str]
    card_type_model: Optional[str]
    mw_backhauling_type: Optional[str]
    ethernet_ports_used: Optional[int]
    ethernet_ports_free: Optional[int]

    class Config:
        orm_mode = True
