from sqlalchemy.orm import Session
from models.health_safety import HealthSafety
from schemas.health_safety import HealthSafetyCreate

def create_health_safety(db: Session, data: HealthSafetyCreate):
    record = HealthSafety(**data.dict())
    db.add(record)
    db.commit()
    db.refresh(record)
    return record

def get_all_health_safety(db: Session):
    return db.query(HealthSafety).all()

def get_health_safety_by_session(db: Session, session_id: int):
    return db.query(HealthSafety).filter(HealthSafety.site_session_id == session_id).all()

def update_health_safety(db: Session, id: int, data: HealthSafetyCreate):
    record = db.query(HealthSafety).filter(HealthSafety.id == id).first()
    if record:
        for key, value in data.dict().items():
            setattr(record, key, value)
        db.commit()
        db.refresh(record)
    return record

def delete_health_safety(db: Session, id: int):
    record = db.query(HealthSafety).filter(HealthSafety.id == id).first()
    if record:
        db.delete(record)
        db.commit()
    return record
