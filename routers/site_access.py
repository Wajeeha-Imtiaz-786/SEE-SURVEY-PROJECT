from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models.site_access import SiteAccess
from schemas.site_access import SiteAccessCreate

router = APIRouter(prefix="/site-access", tags=["Site Access"])

@router.get("/")
def get_all_access_records(db: Session = Depends(get_db)):
    return db.query(SiteAccess).all()

@router.post("/")
def create_access_record(access: SiteAccessCreate, db: Session = Depends(get_db)):
    new_access = SiteAccess(**access.dict())
    db.add(new_access)
    db.commit()
    db.refresh(new_access)
    return new_access
