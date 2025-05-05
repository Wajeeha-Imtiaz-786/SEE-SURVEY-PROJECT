from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from crud import crud_ac_panel
from schemas.ac_panel import ACPanelCreate, ACPanelOut
from database import get_db

router = APIRouter(prefix="/ac-panel", tags=["AC Panel"])

@router.post("/", response_model=ACPanelOut)
def create_ac_panel(panel: ACPanelCreate, db: Session = Depends(get_db)):
    return crud_ac_panel.create_ac_panel(db, panel)

@router.get("/{session_id}", response_model=ACPanelOut)
def get_by_session(session_id: int, db: Session = Depends(get_db)):
    panel = crud_ac_panel.get_ac_panel_by_session(db, session_id)
    if not panel:
        raise HTTPException(status_code=404, detail="Data not found")
    return panel
