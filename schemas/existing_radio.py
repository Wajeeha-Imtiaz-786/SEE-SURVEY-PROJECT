from pydantic import BaseModel, Field
from typing import List, Optional, Literal

# 1. Antenna Structure Info
class AntennaStructureInfoBase(BaseModel):
    site_session_id: int
    has_sketch: Literal["Yes", "No"]
    tower_type: List[Literal["GF tower", "GF Monopole", "GF Palm tree", "RT tower", "RT poles", "Wall mounted", "Other"]]
    gf_structure_height: Optional[int] = None
    rt_structure_count: Optional[int] = None
    rt_existing_heights: Optional[List[Literal["3m", "6m", "9m", "12m", "15m", "Other"]]] = None
    rt_building_height: Optional[int] = None
    lightening_system_installed: Literal["Yes", "No"]
    earthing_bus_bars_exist: Literal["Yes", "No"]
    free_holes_in_bus_bars: Literal[1,2,3,4,5,6,7,8,9,10,"more than 10"]

class AntennaStructureInfoCreate(AntennaStructureInfoBase):
    pass
class AntennaStructureInfo(AntennaStructureInfoBase):
    id: int
    class Config:
        orm_mode = True

# 2. MW Antennas (child table)
class MWAntennasBase(BaseModel):
    site_session_id: int
    mw_antenna_index: int
    height_meter: int
    diameter_cm: int
    azimuth_degree: int
class MWAntennasCreate(MWAntennasBase):
    pass
class MWAntennas(MWAntennasBase):
    id: int
    class Config:
        orm_mode = True

# 3. External DC PDU (child table)
class ExternalDCPDUBase(BaseModel):
    site_session_id: int
    pdu_index: int
    shared_with_other_operator: Literal["Yes", "No"]
    model: Literal["Nokia FPFH", "Nokia FPFD", "DC panel", "Other"]
    location: Literal["On ground level", "On tower"]
    base_height_meter: Optional[int] = None
    dc_feed_from_cabinet: str
    dc_feed_from_distribution: Literal["BLVD", "LLVD", "PDU"]
    dc_cb_fuse: Optional[str] = None
    dc_power_cable_length_meter: Optional[int] = None
    dc_power_cable_cross_section_mm2: Optional[int] = None
    has_free_cbs_fuses: Literal["Yes", "No"]
class ExternalDCPDUCreate(ExternalDCPDUBase):
    pass
class ExternalDCPDU(ExternalDCPDUBase):
    id: int
    class Config:
        orm_mode = True

# 3.1. DC PDU CB/Fuse Table (child of ExternalDCPDU)
class DCPDUCBFuseBase(BaseModel):
    pdu_id: int
    port_number: int
    rating: int
    connected_load: str
class DCPDUCBFuseCreate(DCPDUCBFuseBase):
    pass
class DCPDUCBFuse(DCPDUCBFuseBase):
    id: int
    class Config:
        orm_mode = True

# 4. Radio Antennas (child table)
class RadioAntennaBase(BaseModel):
    site_session_id: int
    antenna_index: int
    operator: Optional[str] = None
    base_height_meter: int
    tower_leg: Literal["A", "B", "C", "D"]
    sector: int
    technology: List[Literal["2G", "3G", "4G", "5G"]]
    azimuth_degree: int
    mechanical_tilt_exist: Literal["Yes", "No"]
    mechanical_tilt_degree: Optional[int] = None
    electrical_tilt_degree: Optional[int] = None
    ret_connectivity: Literal["Chaining", "Direct", "Not applicable"]
    vendor: Literal["Nokia", "PROS", "COMMSCOPE", "Kathrine", "Huawei", "Andrew", "Other"]
    is_nokia_active: Optional[Literal["Yes", "No"]] = None
    nokia_module_name: Optional[str] = None
    nokia_fiber_count: Optional[int] = None
    nokia_fiber_length: Optional[int] = None
    other_vendor_model: Optional[str] = None
    other_vendor_length_cm: Optional[int] = None
    other_vendor_width_cm: Optional[int] = None
    other_vendor_depth_cm: Optional[int] = None
    other_vendor_port_type: Optional[List[Literal["7/16", "4.3-10", "MQ4", "MQ5"]]] = None
    other_vendor_bands: Optional[List[str]] = None
    other_vendor_total_ports: Optional[int] = None
    other_vendor_free_ports: Optional[int] = None
    other_vendor_bands_supported_by_free_ports: Optional[List[str]] = None
    other_vendor_radio_units_connected: Optional[int] = None
    side_arm_length_cm: Optional[int] = None
    side_arm_diameter_cm: Optional[int] = None
    side_arm_offset_cm: Optional[int] = None
    earth_cable_length_m: Optional[int] = None
    included_in_swap_upgrade: Literal["Yes", "No"]
class RadioAntennaCreate(RadioAntennaBase):
    pass
class RadioAntenna(RadioAntennaBase):
    id: int
    class Config:
        orm_mode = True

# 5. Radio Units (child table)
class RadioUnitBase(BaseModel):
    site_session_id: int
    radio_unit_index: int
    operator: Optional[str] = None
    base_height_meter: int
    tower_leg: Literal["A", "B", "C", "D"]
    vendor: Literal["Nokia", "Huawei", "Ericsson", "ZTE", "Other"]
    nokia_model: Optional[str] = None
    nokia_port_count: Optional[int] = None
    other_vendor_model: Optional[str] = None
    other_vendor_length_cm: Optional[int] = None
    other_vendor_width_cm: Optional[int] = None
    other_vendor_depth_cm: Optional[int] = None
    side_arm: Literal["Same antenna side arm", "Separate side arm only for the radio unit", "Shared side arm with other radio units", "Other"]
    side_arm_length_cm: Optional[int] = None
    side_arm_diameter_cm: Optional[int] = None
    side_arm_offset_cm: Optional[int] = None
    dc_power_source: str
    dc_cb_fuse: Optional[List[str]] = None
    dc_power_cable_length_m: Optional[int] = None
    dc_power_cable_cross_section_mm2: Optional[int] = None
    fiber_cable_length_m: Optional[int] = None
    jumper_length_m: Optional[int] = None
    feeder_type: Optional[Literal["7/8 inch", "1-1/4 inch", "1-5/4 inch", "1/2 inch"]] = None
    feeder_length_m: Optional[int] = None
    included_in_swap_upgrade: Literal["Yes", "No"]
    earth_cable_length_m: Optional[int] = None
class RadioUnitCreate(RadioUnitBase):
    pass
class RadioUnit(RadioUnitBase):
    id: int
    class Config:
        orm_mode = True

# 5.1. Radio Unit Port Connectivity (child of RadioUnit)
class RadioUnitPortConnectivityBase(BaseModel):
    radio_unit_id: int
    port_number: int
    sector_number: int
    antenna_number: int
    jumper_length_m: int
class RadioUnitPortConnectivityCreate(RadioUnitPortConnectivityBase):
    pass
class RadioUnitPortConnectivity(RadioUnitPortConnectivityBase):
    id: int
    class Config:
        orm_mode = True
