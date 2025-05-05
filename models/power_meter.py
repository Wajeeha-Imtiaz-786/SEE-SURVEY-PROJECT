from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class PowerMeter(Base):
    __tablename__ = "power_meter"

    id = Column(Integer, primary_key=True, index=True)
    site_session_id = Column(Integer, ForeignKey("site_session.id"))

    power_meter_serial_number = Column(String)
    power_meter_reading = Column(Float)
    ac_power_source = Column(String)
    length_power_cable_to_meter_m = Column(Float)
    cross_section_power_cable_to_meter_mm2 = Column(Float)
    main_cb_rating_amp = Column(Float)
    main_cb_type = Column(String)

    site_session = relationship("SiteSession", back_populates="power_meter")
