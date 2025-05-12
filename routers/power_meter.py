from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional
from pydantic import BaseModel

from database import get_db
from models.power_meter import PowerMeter
from models.ac_connection_info import ACConnectionInfo
from models.ac_panel import ACPanel
from models.ac_panel_cb_load import ACPanelCBLoad
from schemas.power_meter import (
    PowerMeterCreate)
from schemas.ac_connection_info import ACConnectionInfoCreate, ACConnectionInfoResponse

class ACConnectionInfoBase(BaseModel):
    ac_power_source: Optional[str]
    if_diesel_generator_exist_how_many: Optional[int]
    diesel_generator_1_capacity_kva: Optional[float]
    diesel_generator_1_operational_status: Optional[str]
    diesel_generator_2_capacity_kva: Optional[float]
    diesel_generator_2_operational_status: Optional[str]
    solar_system_capacity_kw: Optional[float]

    class Config:
        from_attributes = True

class ACConnectionInfoCreate(BaseModel):
    site_session_id: int
    ac_power_source: str
    if_diesel_generator_exist_how_many: int
    diesel_generator_1_capacity_kva: float
    diesel_generator_1_operational_status: str
    diesel_generator_2_capacity_kva: float
    diesel_generator_2_operational_status: str
    solar_system_capacity_kw: float

    class Config:
        from_attributes = True

class ACConnectionInfoOut(ACConnectionInfoBase):
    id: int
    site_session_id: int

    class Config:
        from_attributes = True

class ACConnectionInfoResponse(BaseModel):
    id: int
    site_session_id: int
    ac_power_source: str
    if_diesel_generator_exist_how_many: int
    diesel_generator_1_capacity_kva: float
    diesel_generator_1_operational_status: str
    diesel_generator_2_capacity_kva: float
    diesel_generator_2_operational_status: str
    solar_system_capacity_kw: float

    class Config:
        from_attributes = True

class PowerMeterResponse(BaseModel):
    id: int
    name: str
    description: str

    class Config:
        from_attributes = True

router = APIRouter(prefix="/power-meter", tags=["Power Meter"])
@router.post("/power-meter/", response_model=PowerMeterResponse)
def create_power_meter(data: PowerMeterCreate, db: Session = Depends(get_db)):
    meter = PowerMeter(**data.dict())
    db.add(meter)
    db.commit()
    db.refresh(meter)
    return meter

@router.get("/power-meter/{id}", response_model=PowerMeterResponse)
def get_power_meter(id: int, db: Session = Depends(get_db)):
    meter = db.query(PowerMeter).filter(PowerMeter.id == id).first()
    if not meter:
        raise HTTPException(status_code=404, detail="PowerMeter not found")
    return meter

@router.put("/power-meter/{id}", response_model=PowerMeterResponse)
def update_power_meter(id: int, data: PowerMeterCreate, db: Session = Depends(get_db)):
    meter = db.query(PowerMeter).filter(PowerMeter.id == id).first()
    if not meter:
        raise HTTPException(status_code=404, detail="PowerMeter not found")
    for key, value in data.dict().items():
        setattr(meter, key, value)
    db.commit()
    db.refresh(meter)
    return meter

@router.delete("/power-meter/{id}")
def delete_power_meter(id: int, db: Session = Depends(get_db)):
    meter = db.query(PowerMeter).filter(PowerMeter.id == id).first()
    if not meter:
        raise HTTPException(status_code=404, detail="PowerMeter not found")
    db.delete(meter)
    db.commit()
    return {"detail": "PowerMeter deleted"}
