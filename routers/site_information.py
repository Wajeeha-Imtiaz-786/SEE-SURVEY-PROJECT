from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models.site_information import SiteInformation
from schemas.site_information import SiteInformationCreate, SiteInformationUpdate, SiteInformationOut
from typing import List

router = APIRouter( tags=["Site Information"])

@router.get("/", response_model=List[SiteInformationOut])
def get_all_site_info(db: Session = Depends(get_db)):
    return db.query(SiteInformation).all()

@router.post("/", response_model=SiteInformationOut)
def create_site_info(info: SiteInformationCreate, db: Session = Depends(get_db)):
    new_info = SiteInformation(**info.dict())
    db.add(new_info)
    db.commit()
    db.refresh(new_info)
    return new_info

@router.put("/{site_info_id}", response_model=SiteInformationOut)
def update_site_info(site_info_id: int, update_data: SiteInformationUpdate, db: Session = Depends(get_db)):
    info = db.query(SiteInformation).filter(SiteInformation.id == site_info_id).first()
    if not info:
        raise HTTPException(status_code=404, detail="Site information not found")
    
    for field, value in update_data.dict(exclude_unset=True).items():
        setattr(info, field, value)

    db.commit()
    db.refresh(info)
    return info

@router.delete("/{site_info_id}", response_model=SiteInformationOut)
def delete_site_info(site_info_id: int, db: Session = Depends(get_db)):
    info = db.query(SiteInformation).filter(SiteInformation.id == site_info_id).first()
    if not info:
        raise HTTPException(status_code=404, detail="Site information not found")

    db.delete(info)
    db.commit()
    return info
