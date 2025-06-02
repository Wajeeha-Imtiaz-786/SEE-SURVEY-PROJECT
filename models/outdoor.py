from sqlalchemy import Column, Integer, String, Float, ForeignKey, Table, Boolean, Enum
from sqlalchemy.orm import relationship
from database import Base

# ------------------------------
# Outdoor General Layout Info
# ------------------------------
class OutdoorGeneralLayoutInfo(Base):
    __tablename__ = "outdoor_general_layout_info"
    id = Column(Integer, primary_key=True, index=True)
    site_session_id = Column(Integer, index=True)
    equipment_area_sunshade = Column(String(16))
    free_positions_for_new_cabinets = Column(Integer)
    cable_tray_height_cm = Column(Integer)
    cable_tray_width_cm = Column(Integer)
    cable_tray_depth_cm = Column(Integer)
    cable_tray_space_available = Column(String(8))
    earth_bus_bar_count = Column(Integer)
    free_holes_in_bus_bars = Column(Integer)
    has_sketch_with_measurements = Column(String(8))

# ------------------------------
# Outdoor Cabinet
# ------------------------------
class OutdoorCabinet(Base):
    __tablename__ = "outdoor_cabinet"
    id = Column(Integer, primary_key=True, index=True)
    site_session_id = Column(Integer, index=True)
    cabinet_index = Column(Integer)
    cabinet_type = Column(String(128))  # store as comma-separated string
    cabinet_vendor = Column(String(32))
    cabinet_model = Column(String(64))
    has_anti_theft = Column(String(8))
    cooling_type = Column(String(16))
    cooling_capacity_watt = Column(Integer)
    compartment_count = Column(Integer)
    existing_hardware = Column(String(128))  # store as comma-separated string
    has_ac_power_feed = Column(String(8))
    ac_panel_cb_number = Column(String(32), nullable=True)
    power_cable_length_meter = Column(Integer, nullable=True)
    power_cable_cross_section_mm = Column(Integer, nullable=True)
    has_blvd = Column(String(8))
    blvd_has_free_cbs = Column(String(8))
    has_llvd = Column(String(8))
    llvd_has_free_cbs = Column(String(8))
    has_pdu = Column(String(8))
    pdu_has_free_cbs = Column(String(8))
    internal_layout_suitable = Column(String(32))
    free_19u_for_telecom = Column(Integer)

# ------------------------------
# Cabinet CB Load Table (for each cabinet)
# ------------------------------
class CabinetCBLoad(Base):
    __tablename__ = "cabinet_cb_load"
    id = Column(Integer, primary_key=True, index=True)
    cabinet_id = Column(Integer, index=True)
    label = Column(String(64))
    panel_id = Column(Integer)
    capacity_rate = Column(Float)

# ------------------------------
# MW Link Table (child of site_session_id)
# ------------------------------
class OutdoorMWLink(Base):
    __tablename__ = "outdoor_mw_link"
    id = Column(Integer, primary_key=True, index=True)
    site_session_id = Column(Integer, index=True)
    mw_link_index = Column(Integer)
    located_in = Column(String(128))  # store as comma-separated string
    mw_equipment_vendor = Column(String(32))
    idu_type = Column(String(64))
    card_type_model = Column(String(64))
    destination_site_id = Column(String(64))
    mw_backhauling_type = Column(String(16))
    ethernet_ports_used = Column(Integer)
    ethernet_ports_free = Column(Integer)

# ------------------------------
# DC Rectifier Table (child of site_session_id)
# ------------------------------
class OutdoorDCRectifier(Base):
    __tablename__ = "outdoor_dc_rectifier"
    id = Column(Integer, primary_key=True, index=True)
    site_session_id = Column(Integer, index=True)
    location = Column(String(64))
    vendor = Column(String(32))
    model = Column(String(64))
    module_count = Column(Integer)
    module_capacity_kw = Column(Float)
    total_capacity_kw = Column(Float)
    free_slots = Column(Integer)

# ------------------------------
# Battery Table (child of site_session_id)
# ------------------------------
class OutdoorBattery(Base):
    __tablename__ = "outdoor_battery"
    id = Column(Integer, primary_key=True, index=True)
    site_session_id = Column(Integer, index=True)
    location = Column(String(64))
    vendor = Column(String(32))
    battery_type = Column(String(16))
    string_count = Column(Integer)
    total_capacity_ah = Column(Integer)
    free_slots = Column(Integer)
    install_location = Column(String(128))  # store as comma-separated string
