from sqlalchemy import Column, Integer, String
from database import Base
from sqlalchemy.orm import relationship

class SiteSession(Base):
    __tablename__ = "site_session"

    id = Column(Integer, primary_key=True, autoincrement=True)
    session_code = Column(String(255), unique=True, nullable=False)
    description = Column(String(255))

    # Updated relationship with SiteLocation to include ForeignKey
    site_location = relationship("SiteLocation", back_populates="site_session", uselist=False)
    site_access = relationship("SiteAccess", back_populates="site_session", uselist=False)
    site_information = relationship("SiteInformation", back_populates="site_session", uselist=False)
    ac_panel = relationship("ACPanel", back_populates="site_session", uselist=False)
    power_meter = relationship("PowerMeter", back_populates="site_session", uselist=False)
    ac_connection_info = relationship("ACConnectionInfo", back_populates="site_session", uselist=False)
