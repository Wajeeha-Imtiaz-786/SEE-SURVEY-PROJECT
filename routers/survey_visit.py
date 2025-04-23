from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models.survey_visit import SurveyVisit
from schemas.survey_visit import SurveyVisitCreate, SurveyVisitUpdate, SurveyVisit as SurveyVisitSchema
from typing import List

router = APIRouter(prefix="/survey-visit", tags=["Survey Visit"])

@router.get("/", response_model=List[SurveyVisitSchema])
def get_visits(db: Session = Depends(get_db)):
    return db.query(SurveyVisit).all()

@router.get("/{visit_id}", response_model=SurveyVisitSchema)
def get_visit(visit_id: int, db: Session = Depends(get_db)):
    visit = db.query(SurveyVisit).filter(SurveyVisit.id == visit_id).first()
    if not visit:
        raise HTTPException(status_code=404, detail="Survey visit not found")
    return visit

@router.get("/survey-visit/{site_session_id}", response_model=List[SurveyVisitSchema])
def get_visits_by_site_session(site_session_id: int, db: Session = Depends(get_db)):
    visits = db.query(SurveyVisit).filter(SurveyVisit.site_session_id == site_session_id).all()
    if not visits:
        raise HTTPException(status_code=404, detail="No survey visits found for this site session ID")
    return visits

@router.post("/", response_model=SurveyVisitSchema)
def create_visit(visit: SurveyVisitCreate, db: Session = Depends(get_db)):
    new_visit = SurveyVisit(**visit.dict())
    db.add(new_visit)
    db.commit()
    db.refresh(new_visit)
    return new_visit

@router.put("/{visit_id}", response_model=SurveyVisitSchema)
def update_visit(visit_id: int, visit: SurveyVisitUpdate, db: Session = Depends(get_db)):
    db_visit = db.query(SurveyVisit).filter(SurveyVisit.id == visit_id).first()
    if not db_visit:
        raise HTTPException(status_code=404, detail="Survey visit not found")
    
    for key, value in visit.dict(exclude_unset=True).items():
        setattr(db_visit, key, value)
    
    db.commit()
    db.refresh(db_visit)
    return db_visit

@router.delete("/{visit_id}", response_model=SurveyVisitSchema)
def delete_visit(visit_id: int, db: Session = Depends(get_db)):
    db_visit = db.query(SurveyVisit).filter(SurveyVisit.id == visit_id).first()
    if not db_visit:
        raise HTTPException(status_code=404, detail="Survey visit not found")
    
    db.delete(db_visit)
    db.commit()
    return db_visit
