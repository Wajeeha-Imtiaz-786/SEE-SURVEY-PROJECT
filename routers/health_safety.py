from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from typing import List

from crud.health_safety import (
    create_health_safety, get_all_health_safety,
    get_health_safety_by_session, update_health_safety, delete_health_safety
)
from schemas.health_safety import HealthSafetyCreate, HealthSafetyOut
from models.health_safety import HealthSafety

router = APIRouter(prefix="/health-safety", tags=["Health & Safety"])

@router.post("/", response_model=HealthSafetyOut)
def add_health_safety(data: HealthSafetyCreate, db: Session = Depends(get_db)):
    return create_health_safety(db, data)

@router.get("/", response_model=List[HealthSafetyOut])
def list_all_health_safety(db: Session = Depends(get_db)):
    return get_all_health_safety(db)

@router.get("/session/{site_session_id}", response_model=List[HealthSafetyOut])
def list_by_session(site_session_id: int, db: Session = Depends(get_db)):
    return get_health_safety_by_session(db, site_session_id)

@router.put("/{id}", response_model=HealthSafetyOut)
def update_record(id: int, data: HealthSafetyCreate, db: Session = Depends(get_db)):
    record = update_health_safety(db, id, data)
    if not record:
        raise HTTPException(status_code=404, detail="Health & Safety record not found")
    return record

@router.delete("/{id}")
def delete_record(id: int, db: Session = Depends(get_db)):
    record = delete_health_safety(db, id)
    if not record:
        raise HTTPException(status_code=404, detail="Health & Safety record not found")
    return {"detail": "Deleted"}
