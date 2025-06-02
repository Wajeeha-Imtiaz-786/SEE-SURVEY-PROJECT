from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

# 1. Antenna Structure Info
class AntennaStructureInfo(Base):
    __tablename__ = "antenna_structure_info"
    id = Column(Integer, primary_key=True, index=True)
    site_session_id = Column(Integer, index=True)
    has_sketch = Column(String(8))
    tower_type = Column(String(128))  # comma-separated
    gf_structure_height = Column(Integer, nullable=True)
    rt_structure_count = Column(Integer, nullable=True)
    rt_existing_heights = Column(String(64), nullable=True)  # comma-separated
    rt_building_height = Column(Integer, nullable=True)
    lightening_system_installed = Column(String(8))
    earthing_bus_bars_exist = Column(String(8))
    free_holes_in_bus_bars = Column(String(16))

# 2. MW Antennas (child table)
class MWAntennas(Base):
    __tablename__ = "mw_antennas"
    id = Column(Integer, primary_key=True, index=True)
    site_session_id = Column(Integer, index=True)
    mw_antenna_index = Column(Integer)
    height_meter = Column(Integer)
    diameter_cm = Column(Integer)
    azimuth_degree = Column(Integer)

# 3. External DC PDU (child table)
class ExternalDCPDU(Base):
    __tablename__ = "external_dc_pdu"
    id = Column(Integer, primary_key=True, index=True)
    site_session_id = Column(Integer, index=True)
    pdu_index = Column(Integer)
    shared_with_other_operator = Column(String(8))
    model = Column(String(32))
    location = Column(String(32))
    base_height_meter = Column(Integer, nullable=True)
    dc_feed_from_cabinet = Column(String(64))
    dc_feed_from_distribution = Column(String(16))
    dc_cb_fuse = Column(String(64), nullable=True)
    dc_power_cable_length_meter = Column(Integer, nullable=True)
    dc_power_cable_cross_section_mm2 = Column(Integer, nullable=True)
    has_free_cbs_fuses = Column(String(8))

# 3.1. DC PDU CB/Fuse Table (child of ExternalDCPDU)
class DCPDUCBFuse(Base):
    __tablename__ = "dcpdu_cb_fuse"
    id = Column(Integer, primary_key=True, index=True)
    pdu_id = Column(Integer, index=True)
    port_number = Column(Integer)
    rating = Column(Integer)
    connected_load = Column(String(128))

# 4. Radio Antennas (child table)
class RadioAntenna(Base):
    __tablename__ = "radio_antenna"
    id = Column(Integer, primary_key=True, index=True)
    site_session_id = Column(Integer, index=True)
    antenna_index = Column(Integer)
    operator = Column(String(32), nullable=True)
    base_height_meter = Column(Integer)
    tower_leg = Column(String(2))
    sector = Column(Integer)
    technology = Column(String(64))  # comma-separated
    azimuth_degree = Column(Integer)
    mechanical_tilt_exist = Column(String(8))
    mechanical_tilt_degree = Column(Integer, nullable=True)
    electrical_tilt_degree = Column(Integer, nullable=True)
    ret_connectivity = Column(String(32))
    vendor = Column(String(32))
    is_nokia_active = Column(String(8), nullable=True)
    nokia_module_name = Column(String(64), nullable=True)
    nokia_fiber_count = Column(Integer, nullable=True)
    nokia_fiber_length = Column(Integer, nullable=True)
    other_vendor_model = Column(String(64), nullable=True)
    other_vendor_length_cm = Column(Integer, nullable=True)
    other_vendor_width_cm = Column(Integer, nullable=True)
    other_vendor_depth_cm = Column(Integer, nullable=True)
    other_vendor_port_type = Column(String(64), nullable=True)  # comma-separated
    other_vendor_bands = Column(String(128), nullable=True)  # comma-separated
    other_vendor_total_ports = Column(Integer, nullable=True)
    other_vendor_free_ports = Column(Integer, nullable=True)
    other_vendor_bands_supported_by_free_ports = Column(String(128), nullable=True)  # comma-separated
    other_vendor_radio_units_connected = Column(Integer, nullable=True)
    side_arm_length_cm = Column(Integer, nullable=True)
    side_arm_diameter_cm = Column(Integer, nullable=True)
    side_arm_offset_cm = Column(Integer, nullable=True)
    earth_cable_length_m = Column(Integer, nullable=True)
    included_in_swap_upgrade = Column(String(8))

# 5. Radio Units (child table)
class RadioUnit(Base):
    __tablename__ = "radio_unit"
    id = Column(Integer, primary_key=True, index=True)
    site_session_id = Column(Integer, index=True)
    radio_unit_index = Column(Integer)
    operator = Column(String(32), nullable=True)
    base_height_meter = Column(Integer)
    tower_leg = Column(String(2))
    vendor = Column(String(32))
    nokia_model = Column(String(64), nullable=True)
    nokia_port_count = Column(Integer, nullable=True)
    other_vendor_model = Column(String(64), nullable=True)
    other_vendor_length_cm = Column(Integer, nullable=True)
    other_vendor_width_cm = Column(Integer, nullable=True)
    other_vendor_depth_cm = Column(Integer, nullable=True)
    side_arm = Column(String(64))
    side_arm_length_cm = Column(Integer, nullable=True)
    side_arm_diameter_cm = Column(Integer, nullable=True)
    side_arm_offset_cm = Column(Integer, nullable=True)
    dc_power_source = Column(String(64))
    dc_cb_fuse = Column(String(128), nullable=True)  # comma-separated
    dc_power_cable_length_m = Column(Integer, nullable=True)
    dc_power_cable_cross_section_mm2 = Column(Integer, nullable=True)
    fiber_cable_length_m = Column(Integer, nullable=True)
    jumper_length_m = Column(Integer, nullable=True)
    feeder_type = Column(String(32), nullable=True)
    feeder_length_m = Column(Integer, nullable=True)
    included_in_swap_upgrade = Column(String(8))
    earth_cable_length_m = Column(Integer, nullable=True)

# 5.1. Radio Unit Port Connectivity (child of RadioUnit)
class RadioUnitPortConnectivity(Base):
    __tablename__ = "radio_unit_port_connectivity"
    id = Column(Integer, primary_key=True, index=True)
    radio_unit_id = Column(Integer, index=True)
    port_number = Column(Integer)
    sector_number = Column(Integer)
    antenna_number = Column(Integer)
    jumper_length_m = Column(Integer)
