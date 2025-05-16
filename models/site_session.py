from sqlalchemy import Column, Integer, String
from database import Base
from sqlalchemy.orm import relationship

class SiteSession(Base):
    __tablename__ = "site_session"

    id = Column(Integer, primary_key=True, autoincrement=True)
    session_code = Column(String(255), unique=True, nullable=False)
    description = Column(String(255))

    site_location = relationship("SiteLocation", back_populates="site_session", uselist=False)
    site_access = relationship("SiteAccess", back_populates="site_session", uselist=False)
