from pydantic import BaseModel
from typing import Optional
from datetime import date


class SurveyVisitBase(BaseModel):
    survey_date: date
    subcontractor_company: str
    surveyor_name: str
    surveyor_phone: str
    nokia_rep_name: Optional[str] = None
    nokia_rep_title: Optional[str] = None
    customer_rep_name: Optional[str] = None
    customer_rep_title: Optional[str] = None


class SurveyVisitCreate(SurveyVisitBase):
    pass


class SurveyVisitUpdate(SurveyVisitBase):
    survey_date: Optional[date] = None
    subcontractor_company: Optional[str] = None
    surveyor_name: Optional[str] = None
    surveyor_phone: Optional[str] = None


class SurveyVisit(SurveyVisitBase):
    id: int

    class Config:
        from_attributes = True
