from sqlalchemy import Column, Integer, String, Enum, TIMESTAMP, func
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    first_name = Column(String(50))
    last_name = Column(String(50))
    phone = Column(String(20))
    password_hash = Column(String(255), nullable=False)
    user_status = Column(Enum("Active", "Inactive"), default="Active")
    creation_date = Column(TIMESTAMP, server_default=func.current_timestamp())
    last_login = Column(TIMESTAMP, server_default=func.current_timestamp(), onupdate=func.current_timestamp())
    title = Column(String(50))
    nid = Column(String(50), unique=True, nullable=True)

    projects = relationship("Project", back_populates="user")
    roles = relationship("Role", back_populates="user")
