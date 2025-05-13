from sqlalchemy import Column, Integer, String, Float, Boolean
from database import Base

class RoomInfo(Base):
    __tablename__ = "room_info"

    id = Column(Integer, primary_key=True, autoincrement=True)
    height = Column(Float, nullable=False)
    width = Column(Float, nullable=False)
    depth = Column(Float, nullable=False)
    telecom_hardware_type = Column(String(255), nullable=False)
    has_sketch = Column(Boolean, nullable=False)

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

class RAN(Base):
    __tablename__ = "ran"

    id = Column(Integer, primary_key=True, autoincrement=True)
    equipment_vendor = Column(String(255), nullable=False)
    has_free_slots = Column(Boolean, nullable=False)
    rack_type_with_free_slots = Column(String(255), nullable=False)
    multiple_locations_available = Column(String(255), nullable=False)
    transmission_cable_length = Column(Float, nullable=False)
