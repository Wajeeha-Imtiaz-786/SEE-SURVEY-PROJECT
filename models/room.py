from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey, Table, Enum
from sqlalchemy.orm import relationship
from database import Base

# ---------------- RoomInfo ----------------
class RoomInfo(Base):
    __tablename__ = "room_info"

    id = Column(Integer, primary_key=True, autoincrement=True)
    height = Column(Float, nullable=False)
    width = Column(Float, nullable=False)
    depth = Column(Float, nullable=False)
    telecom_hardware_type = Column(String(255), nullable=False)
    has_sketch = Column(Boolean, nullable=False)


# ---------------- RoomPreparation ----------------
class RoomPreparation(Base):
    __tablename__ = "room_preparation"

    id = Column(Integer, primary_key=True, autoincrement=True)
    air_condition_type = Column(String(255), nullable=False)
    air_condition_count = Column(String(255), nullable=False)
    air_condition_capacity = Column(Float, nullable=False)
    air_condition_status = Column(String(255), nullable=False)
    cable_tray_clearance = Column(Float, nullable=False)
    cable_tray_width = Column(Float, nullable=False)
    has_space_on_cable_tray = Column(Boolean, nullable=False)
    has_space_in_feeders_window = Column(Boolean, nullable=False)
    free_holes_in_feeders_window = Column(Integer, nullable=False)
    bus_bar_count = Column(Integer, nullable=False)
    free_holes_in_bus_bars = Column(Integer, nullable=False)
    free_positions_for_racks = Column(Integer, nullable=False)


# ---------------- RAN ----------------
class RAN(Base):
    __tablename__ = "ran"

    id = Column(Integer, primary_key=True, autoincrement=True)
    equipment_vendor = Column(String(255), nullable=False)
    has_free_slots = Column(Boolean, nullable=False)
    rack_type_with_free_slots = Column(String(255), nullable=False)
    multiple_locations_available = Column(String(255), nullable=False)
    transmission_cable_length = Column(Float, nullable=False)


# ---------------- TransmissionMW ----------------
class TransmissionMW(Base):
    __tablename__ = "transmission_mw"

    id = Column(Integer, primary_key=True, autoincrement=True)
    type_of_transmission = Column(String(255), nullable=False)  # Fiber / MW / Not exist
    transmission_equipment_vendor = Column(String(255), nullable=False)  # comma-separated: Nokia, Huawei, etc.
    cable_length_from_odf_to_baseband = Column(Float, nullable=False)
    odf_fiber_cable_type = Column(String(50), nullable=False)  # LC / SC / FC
    free_ports_on_odf = Column(Integer, nullable=False)
    mw_links_exist = Column(Integer, nullable=False)  # 1 to 10
    space_available_for_mw_idu_installation = Column(String(255), nullable=False)  # comma-separated: Wall mount, New rack, etc.

    mw_links = relationship("MWLink", back_populates="transmission_mw", cascade="all, delete-orphan")


# ---------------- MWLink ----------------
class MWLink(Base):
    __tablename__ = "mw_link"

    id = Column(Integer, primary_key=True, autoincrement=True)
    transmission_mw_id = Column(Integer, ForeignKey("transmission_mw.id"), nullable=False)

    destination_site_id = Column(String(255), nullable=False)
    mw_equipment_vendor = Column(String(255), nullable=False)  # Nokia / Ericson / etc.
    idu_type = Column(String(255), nullable=False)
    card_type_model = Column(String(255), nullable=False)
    mw_backhauling_type = Column(String(50), nullable=False)  # Ethernet / Fiber
    ethernet_ports_used = Column(Integer, nullable=False)
    ethernet_ports_free = Column(Integer, nullable=False)

    transmission_mw = relationship("TransmissionMW", back_populates="mw_links")


# ---------------- DCPowerSystem ----------------

class DCPowerSystem(Base):
    __tablename__ = "dc_power_system"

    id = Column(Integer, primary_key=True, index=True)
    site_session_id = Column(Integer, ForeignKey("site_session.id"))

    existing_dc_equipment_vendor = Column(Enum("Nokia", "Ericson", "Huawei", "ZTE", "Other"))
    existing_dc_power_rack = Column(Integer)
    existing_rectifier_modules = Column(Integer)
    rectifier_module_model = Column(String(255))
    rectifier_module_capacity = Column(Integer)
    free_slots_new_rectifier = Column(Integer)
    is_blvd_available = Column(Enum("Yes", "No"))
    blvd_has_free_cbs = Column(Enum("Yes", "No"))
    is_llvd_available = Column(Enum("Yes", "No"))
    llvd_has_free_cbs = Column(Enum("Yes", "No"))
    is_pdu_available = Column(Enum("Yes", "No"))
    pdu_has_free_cbs = Column(Enum("Yes", "No"))
    battery_strings = Column(Integer)
    battery_type = Column(Enum("Lead acid", "Lithium"))
    battery_vendor = Column(String(255))  # Comma-separated string
    total_battery_capacity = Column(Integer)

    # Relationships
    blvd_cb_loads = relationship("BLVDCBLoad", back_populates="dc_power_system", cascade="all, delete")
    llvd_cb_loads = relationship("LLVDCBLoad", back_populates="dc_power_system", cascade="all, delete")
    pdu_cb_loads = relationship("PDUCBLoad", back_populates="dc_power_system", cascade="all, delete")


class BLVDCBLoad(Base):
    __tablename__ = "blvd_cb_load"

    id = Column(Integer, primary_key=True, index=True)
    dc_power_system_id = Column(Integer, ForeignKey("dc_power_system.id"))
    label = Column(String(255))
    capacity = Column(String(255))

    dc_power_system = relationship("DCPowerSystem", back_populates="blvd_cb_loads")


class LLVDCBLoad(Base):
    __tablename__ = "llvd_cb_load"

    id = Column(Integer, primary_key=True, index=True)
    dc_power_system_id = Column(Integer, ForeignKey("dc_power_system.id"))
    label = Column(String(255))
    capacity = Column(String(255))

    dc_power_system = relationship("DCPowerSystem", back_populates="llvd_cb_loads")


class PDUCBLoad(Base):
    __tablename__ = "pdu_cb_load"

    id = Column(Integer, primary_key=True, index=True)
    dc_power_system_id = Column(Integer, ForeignKey("dc_power_system.id"))
    label = Column(String(255))
    capacity = Column(String(255))

    dc_power_system = relationship("DCPowerSystem", back_populates="pdu_cb_loads")
