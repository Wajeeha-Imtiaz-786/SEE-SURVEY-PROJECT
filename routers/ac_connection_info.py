from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from crud import crud_ac_connection_info
from schemas.ac_connection_info import ACConnectionInfoCreate, ACConnectionInfoOut
from database import get_db

router = APIRouter(prefix="/ac-connection-info", tags=["AC Connection Info"])

@router.post("/", response_model=ACConnectionInfoOut)
def create_ac_connection_info(info: ACConnectionInfoCreate, db: Session = Depends(get_db)):
    return crud_ac_connection_info.create_ac_connection_info(db, info)

@router.get("/{session_id}", response_model=ACConnectionInfoOut)
def get_by_session(session_id: int, db: Session = Depends(get_db)):
    info = crud_ac_connection_info.get_ac_connection_info_by_session(db, session_id)
    if not info:
        raise HTTPException(status_code=404, detail="Data not found")
    return info
