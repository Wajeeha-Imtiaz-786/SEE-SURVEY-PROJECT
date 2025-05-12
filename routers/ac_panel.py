from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.ac_panel import ACPanelCreate, ACPanelResponse, ACPanelOut
from database import get_db
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from models.power_meter import PowerMeter
from models.ac_panel import ACPanel

router = APIRouter(prefix="/ac-panel", tags=["AC Panel"])
@router.post("/ac-panel/", response_model=ACPanelResponse)
def create_ac_panel(data: ACPanelCreate, db: Session = Depends(get_db)):
    panel = ACPanel(**data.dict())
    db.add(panel)
    db.commit()
    db.refresh(panel)
    return panel

@router.get("/ac-panel/{id}", response_model=ACPanelResponse)
def get_ac_panel(id: int, db: Session = Depends(get_db)):
    panel = db.query(ACPanel).filter(ACPanel.id == id).first()
    if not panel:
        raise HTTPException(status_code=404, detail="ACPanel not found")
    return panel

@router.put("/ac-panel/{id}", response_model=ACPanelResponse)
def update_ac_panel(id: int, data: ACPanelCreate, db: Session = Depends(get_db)):
    panel = db.query(ACPanel).filter(ACPanel.id == id).first()
    if not panel:
        raise HTTPException(status_code=404, detail="ACPanel not found")
    for key, value in data.dict().items():
        setattr(panel, key, value)
    db.commit()
    db.refresh(panel)
    return panel

@router.delete("/ac-panel/{id}")
def delete_ac_panel(id: int, db: Session = Depends(get_db)):
    panel = db.query(ACPanel).filter(ACPanel.id == id).first()
    if not panel:
        raise HTTPException(status_code=404, detail="ACPanel not found")
    db.delete(panel)
    db.commit()
    return {"detail": "ACPanel deleted"}

