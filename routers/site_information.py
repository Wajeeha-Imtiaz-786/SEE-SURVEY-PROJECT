from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models.site_information import SiteInformation
from schemas.site_information import SiteInformationCreate

router = APIRouter(prefix="/site-information", tags=["Site Information"])

@router.get("/")
def get_all_site_info(db: Session = Depends(get_db)):
    return db.query(SiteInformation).all()

@router.post("/")
def create_site_info(info: SiteInformationCreate, db: Session = Depends(get_db)):
    new_info = SiteInformation(**info.dict())
    db.add(new_info)
    db.commit()
    db.refresh(new_info)
    return new_info
