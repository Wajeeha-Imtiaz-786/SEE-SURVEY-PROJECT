from sqlalchemy.orm import Session
from models.survey_visit import SurveyVisit
from schemas.survey_visit import SurveyVisitCreate, SurveyVisitUpdate

def create_survey_visit(db: Session, visit_data: SurveyVisitCreate):
    visit = SurveyVisit(**visit_data.dict())
    db.add(visit)
    db.commit()
    db.refresh(visit)
    return visit

def get_survey_visit_by_id(db: Session, visit_id: int):
    return db.query(SurveyVisit).filter(SurveyVisit.id == visit_id).first()

def get_all_survey_visits(db: Session):
    return db.query(SurveyVisit).all()

def update_survey_visit(db: Session, visit_id: int, updates: SurveyVisitUpdate):
    db_visit = db.query(SurveyVisit).filter(SurveyVisit.id == visit_id).first()
    if db_visit:
        for key, value in updates.dict(exclude_unset=True).items():
            setattr(db_visit, key, value)
        db.commit()
        db.refresh(db_visit)
    return db_visit

def delete_survey_visit(db: Session, visit_id: int):
    db_visit = db.query(SurveyVisit).filter(SurveyVisit.id == visit_id).first()
    if db_visit:
        db.delete(db_visit)
        db.commit()
    return db_visit
