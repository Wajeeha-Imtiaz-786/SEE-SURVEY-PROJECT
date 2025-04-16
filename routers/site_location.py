from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.site_location import SiteLocation
from schemas.site_location import SiteLocationCreate, SiteLocationOut
from database import get_db

router = APIRouter()

@router.post("/", response_model=SiteLocationOut)
def create_site_location(site_location: SiteLocationCreate, db: Session = Depends(get_db)):
    db_site = SiteLocation(**site_location.dict())
    db.add(db_site)
    db.commit()
    db.refresh(db_site)
    return db_site

@router.get("/{site_id}", response_model=SiteLocationOut)
def get_site_location(site_id: int, db: Session = Depends(get_db)):
    site = db.query(SiteLocation).filter(SiteLocation.id == site_id).first()
    if not site:
        raise HTTPException(status_code=404, detail="Site not found")
    return site
