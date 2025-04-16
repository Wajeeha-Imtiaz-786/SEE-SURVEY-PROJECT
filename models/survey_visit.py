from sqlalchemy import Column, Integer, String, Date
from database import Base

class SurveyVisit(Base):
    __tablename__ = "survey_visit"

    id = Column(Integer, primary_key=True, autoincrement=True)
    survey_date = Column(Date, nullable=False)
    subcontractor_company = Column(String(255), nullable=False)
    surveyor_name = Column(String(255), nullable=False)
    surveyor_phone = Column(String(255), nullable=False)
    nokia_rep_name = Column(String(255))
    nokia_rep_title = Column(String(255))
    customer_rep_name = Column(String(255))
    customer_rep_title = Column(String(255))
