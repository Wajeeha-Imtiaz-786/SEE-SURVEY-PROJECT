from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from database import get_db
from models.power_meter import PowerMeter
from models.ac_panel import ACPanel
from models.ac_panel_cb_load import ACPanelCBLoad
from models.ac_connection_info import ACConnectionInfo


from schemas.ac_connection_info import (
    ACConnectionInfoCreate,
    ACConnectionInfoResponse,
)
from typing import List

router = APIRouter( tags=["AC Connection Info"])

@router.post("/", response_model=ACConnectionInfoResponse)
def create_ac_connection_info(payload: ACConnectionInfoCreate, db: Session = Depends(get_db)):
    ac_info = ACConnectionInfo(**payload.dict())
    db.add(ac_info)
    db.commit()
    db.refresh(ac_info)
    return ac_info

@router.get("/", response_model=List[ACConnectionInfoResponse])
def get_all_ac_connection_info(db: Session = Depends(get_db)):
    return db.query(ACConnectionInfo).all()

@router.get("/{id}", response_model=ACConnectionInfoResponse)
def get_ac_connection_info_by_id(id: int, db: Session = Depends(get_db)):
    ac_info = db.query(ACConnectionInfo).filter(ACConnectionInfo.id == id).first()
    if not ac_info:
        raise HTTPException(status_code=404, detail="AC connection info not found")
    return ac_info

# ✅ PUT endpoint - update by ID
@router.put("/{id}", response_model=ACConnectionInfoResponse)
def update_ac_connection_info(id: int, payload: ACConnectionInfoCreate, db: Session = Depends(get_db)):
    ac_info = db.query(ACConnectionInfo).filter(ACConnectionInfo.id == id).first()
    if not ac_info:
        raise HTTPException(status_code=404, detail="AC connection info not found")

    for key, value in payload.dict().items():
        setattr(ac_info, key, value)

    db.commit()
    db.refresh(ac_info)
    return ac_info

# ✅ DELETE endpoint - delete by ID
@router.delete("/{id}")
def delete_ac_connection_info(id: int, db: Session = Depends(get_db)):
    ac_info = db.query(ACConnectionInfo).filter(ACConnectionInfo.id == id).first()
    if not ac_info:
        raise HTTPException(status_code=404, detail="AC connection info not found")

    db.delete(ac_info)
    db.commit()
    return {"detail": "AC connection info deleted successfully"}
