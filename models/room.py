from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey, Table
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
