from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class ACPanel(Base):
    __tablename__ = "ac_panel"

    id = Column(Integer, primary_key=True, index=True)
    site_session_id = Column(Integer, ForeignKey("site_session.id"))

    length_power_cable_from_meter_m = Column(Float)
    cross_section_cable_from_meter_mm2 = Column(Float)
    ac_panel_main_cb_rating_amp = Column(Float)
    ac_panel_main_cb_type = Column(String(255))
    has_free_cbs = Column(String(255))
    free_space_to_add_new_cbs = Column(Integer)

    site_session = relationship("SiteSession", back_populates="ac_panel")
    cbs_loads = relationship("ACPanelCBLoad", back_populates="ac_panel", cascade="all, delete")
