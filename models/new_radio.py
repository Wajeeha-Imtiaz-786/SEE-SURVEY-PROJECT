from sqlalchemy import Column, Integer, String, ForeignKey, Float, Boolean
from sqlalchemy.orm import relationship
from database import Base

# 1. New Radio Installation
class NewRadioInstallation(Base):
    __tablename__ = "new_radio_installations"

    id = Column(Integer, primary_key=True, index=True)
    site_session_id = Column(Integer, ForeignKey('site_session.id'))

    new_sectors_planned = Column(String(255))
    new_antennas_planned = Column(String(255))
    new_radio_units_planned = Column(String(255))
    swapped_antennas = Column(String(255))
    swapped_radio_units = Column(String(255))
    new_fpfh_installed = Column(String(255))


# 2. New Antenna
class NewAntenna(Base):
    __tablename__ = "new_antennas"

    id = Column(Integer, primary_key=True, index=True)
    site_session_id = Column(Integer, ForeignKey('site_session.id'))

    sector_number = Column(String(255))
    new_or_swap = Column(String(255))
    antenna_technology = Column(String(255))  # store as comma-separated 2G/3G/4G/5G
    azimuth = Column(Integer)
    base_height = Column(Float)
    tower_leg = Column(String(255))
    leg_section = Column(String(255))
    angular_dimensions = Column(String(255))  # e.g., "100x150"
    tubular_cross_section = Column(String(255))
    side_arm = Column(String(255))
    side_arm_length = Column(Float)
    side_arm_cross_section = Column(String(255))
    side_arm_offset = Column(Float)
    earth_bus_bar_exists = Column(String(255))
    earth_cable_length = Column(Float)


# 3. New Radio Unit
class NewRadioUnit(Base):
    __tablename__ = "new_radio_units"

    id = Column(Integer, primary_key=True, index=True)
    site_session_id = Column(Integer, ForeignKey('site_session.id'))

    sector = Column(String(255))
    antenna_connection = Column(String(255))
    antenna_technology = Column(String(255))
    model = Column(String(255))
    location = Column(String(255))
    feeder_length = Column(Float)
    tower_leg_section = Column(String(255))
    angular_dimensions = Column(String(255))
    tubular_cross_section = Column(String(255))
    side_arm = Column(String(255))
    side_arm_length = Column(Float)
    side_arm_cross_section = Column(String(255))
    side_arm_offset = Column(Float)
    dc_power_source = Column(String(255))
    dc_power_length = Column(Float)
    fiber_length = Column(Float)
    jumper_length = Column(Float)
    earth_bus_bar_exists = Column(String(255))
    earth_cable_length = Column(Float)


# 4. New FPFH
class NewFPFH(Base):
    __tablename__ = "new_fpfhs"

    id = Column(Integer, primary_key=True, index=True)
    site_session_id = Column(Integer, ForeignKey('site_session.id'))

    installation_type = Column(String(255))
    location = Column(String(255))
    base_height = Column(Float)
    tower_leg = Column(String(255))
    power_source = Column(String(255))
    rectifier_distribution = Column(String(255))
    ethernet_length = Column(Float)
    dc_power_length = Column(Float)
    earth_bus_bar_exists = Column(String(255))
    earth_cable_length = Column(Float)


# 5. GPS
class NewGPS(Base):
    __tablename__ = "new_gps"

    id = Column(Integer, primary_key=True, index=True)
    site_session_id = Column(Integer, ForeignKey('site_session.id'))

    location = Column(String(255))
    height = Column(Float)
    cable_length = Column(Float)
