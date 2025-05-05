from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class ACPanelCBLoad(Base):
    __tablename__ = "ac_panel_cbs_load"

    id = Column(Integer, primary_key=True, index=True)
    label = Column(String(255))
    capacity_rate = Column(Float)

    ac_panel_id = Column(Integer, ForeignKey("ac_panel.id"))

    ac_panel = relationship("ACPanel", back_populates="cbs_loads")
