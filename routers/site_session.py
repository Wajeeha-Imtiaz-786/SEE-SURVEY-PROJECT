from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
import schemas.site_session as schemas
import crud.site_session as crud

router = APIRouter(
    prefix="/site_session",
    tags=["Site Session"]
)

@router.post("/", response_model=schemas.SiteSession)
def create_site_session(site_session: schemas.SiteSessionCreate, db: Session = Depends(get_db)):
    return crud.create_site_session(db, site_session)

@router.get("/{site_session_id}", response_model=schemas.SiteSession)
def read_site_session(site_session_id: int, db: Session = Depends(get_db)):
    db_site_session = crud.get_site_session(db, site_session_id)
    if db_site_session is None:
        raise HTTPException(status_code=404, detail="Site session not found")
    return db_site_session

@router.get("/", response_model=list[schemas.SiteSession])
def read_all_site_sessions(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_all_site_sessions(db, skip=skip, limit=limit)

@router.get("/{site_session_id}/details")
def get_full_site_session_details(site_session_id: int, db: Session = Depends(get_db)):
    site_location = crud.get_site_location_by_session(db, site_session_id)
    site_information = crud.get_site_information_by_session(db, site_session_id)
    site_access = crud.get_site_access_by_session(db, site_session_id)
    return {
        "site_location": site_location,
        "site_information": site_information,
        "site_access": site_access
    }

@router.put("/{site_session_id}", response_model=schemas.SiteSession)
def update_site_session(site_session_id: int, site_session: schemas.SiteSessionUpdate, db: Session = Depends(get_db)):
    db_site_session = crud.get_site_session(db, site_session_id)
    if db_site_session is None:
        raise HTTPException(status_code=404, detail="Site session not found")
    return crud.update_site_session(db, site_session_id, site_session)

@router.delete("/{site_session_id}")
def delete_site_session(site_session_id: int, db: Session = Depends(get_db)):
    db_site_session = crud.get_site_session(db, site_session_id)
    if db_site_session is None:
        raise HTTPException(status_code=404, detail="Site session not found")
    crud.delete_site_session(db, site_session_id)
    return {"detail": "Site session deleted"}
