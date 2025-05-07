from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from crud import crud_ac_panel_cb_load
from schemas.ac_panel_cb_load import ACPanelCBLoadCreate, ACPanelCBLoadOut
from database import get_db
from typing import List

router = APIRouter( tags=["AC Panel CB Loads"])

@router.post("/", response_model=ACPanelCBLoadOut)
def create_cb_load(load: ACPanelCBLoadCreate, db: Session = Depends(get_db)):
    return crud_ac_panel_cb_load.create_cb_load(db, load)

@router.get("/{ac_panel_id}", response_model=List[ACPanelCBLoadOut])
def get_cb_loads(ac_panel_id: int, db: Session = Depends(get_db)):
    return crud_ac_panel_cb_load.get_cb_loads_by_panel(db, ac_panel_id)
