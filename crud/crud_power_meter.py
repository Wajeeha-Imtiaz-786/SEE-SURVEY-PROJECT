from sqlalchemy.orm import Session
from models.power_meter import PowerMeter
from schemas.power_meter import PowerMeterCreate

def create_power_meter(db: Session, meter: PowerMeterCreate):
    db_meter = PowerMeter(**meter.dict())
    db.add(db_meter)
    db.commit()
    db.refresh(db_meter)
    return db_meter

def get_power_meter_by_session(db: Session, session_id: int):
    return db.query(PowerMeter).filter(PowerMeter.site_session_id == session_id).first()
