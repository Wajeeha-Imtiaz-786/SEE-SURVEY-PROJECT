from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from crud import crud_ac_panel_cb_load
from schemas.ac_panel_cb_load import ACPanelCBLoadCreate, ACPanelCBLoadOut, ACPanelsCBLoadResponse, ACPanelsCBLoadCreate
from database import get_db
from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from models.power_meter import PowerMeter
from models.ac_panel import ACPanel
from models.ac_panel_cb_load import ACPanelCBLoad
from models.ac_connection_info import ACConnectionInfo
from schemas.ac_connection_info import ACConnectionInfoCreate
from schemas.power_meter import (
    PowerMeterCreate, PowerMeterResponse
)
from schemas.ac_panel import ACPanelCreate, ACPanelResponse

router = APIRouter( tags=["AC Panel CB Loads"])

@router.post("/ac-panel-cb-load/", response_model=ACPanelsCBLoadResponse)
def create_cb_load(data: ACPanelsCBLoadCreate, db: Session = Depends(get_db)):
    cb = ACPanelCBLoad(**data.dict())
    db.add(cb)
    db.commit()
    db.refresh(cb)
    return cb

@router.get("/ac-panel-cb-load/{id}", response_model=ACPanelsCBLoadResponse)
def get_cb_load(id: int, db: Session = Depends(get_db)):
    cb = db.query(ACPanelCBLoad).filter(ACPanelCBLoad.id == id).first()
    if not cb:
        raise HTTPException(status_code=404, detail="ACPanelsCBLoad not found")
    return cb

@router.put("/ac-panel-cb-load/{id}", response_model=ACPanelsCBLoadResponse)
def update_cb_load(id: int, data: ACPanelsCBLoadCreate, db: Session = Depends(get_db)):
    cb = db.query(ACPanelCBLoad).filter(ACPanelCBLoad.id == id).first()
    if not cb:
        raise HTTPException(status_code=404, detail="ACPanelsCBLoad not found")
    for key, value in data.dict().items():
        setattr(cb, key, value)
    db.commit()
    db.refresh(cb)
    return cb

@router.delete("/ac-panel-cb-load/{id}")
def delete_cb_load(id: int, db: Session = Depends(get_db)):
    cb = db.query(ACPanelCBLoad).filter(ACPanelCBLoad.id == id).first()
    if not cb:
        raise HTTPException(status_code=404, detail="ACPanelsCBLoad not found")
    db.delete(cb)
    db.commit()
    return {"detail": "ACPanelsCBLoad deleted"}
