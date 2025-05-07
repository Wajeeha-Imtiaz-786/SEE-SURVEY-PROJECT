from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from crud import crud_power_meter
from schemas.power_meter import PowerMeterCreate, PowerMeterOut
from database import get_db

router = APIRouter( tags=["Power Meter"])

@router.post("/", response_model=PowerMeterOut)
def create_power_meter(meter: PowerMeterCreate, db: Session = Depends(get_db)):
    return crud_power_meter.create_power_meter(db, meter)

@router.get("/{session_id}", response_model=PowerMeterOut)
def get_by_session(session_id: int, db: Session = Depends(get_db)):
    meter = crud_power_meter.get_power_meter_by_session(db, session_id)
    if not meter:
        raise HTTPException(status_code=404, detail="Data not found")
    return meter
