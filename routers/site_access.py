from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models.site_access import SiteAccess
from schemas.site_access import SiteAccessCreate, SiteAccessBase

router = APIRouter( tags=["Site Access"])

@router.get("/")
def get_all_access_records(db: Session = Depends(get_db)):
    return db.query(SiteAccess).all()

@router.get("/{id}")
def get_access_record(id: int, db: Session = Depends(get_db)):
    access = db.query(SiteAccess).filter(SiteAccess.id == id).first()
    if access is None:
        raise HTTPException(status_code=404, detail="Access record not found")
    return access

@router.post("/")
def create_access_record(access: SiteAccessCreate, db: Session = Depends(get_db)):
    new_access = SiteAccess(**access.dict())
    db.add(new_access)
    db.commit()
    db.refresh(new_access)
    return new_access

@router.put("/{id}")
def update_access_record(id: int, access: SiteAccessBase, db: Session = Depends(get_db)):
    existing_access = db.query(SiteAccess).filter(SiteAccess.id == id).first()
    if existing_access is None:
        raise HTTPException(status_code=404, detail="Access record not found")
    
    for key, value in access.dict(exclude_unset=True).items():
        setattr(existing_access, key, value)

    db.commit()
    db.refresh(existing_access)
    return existing_access

@router.delete("/{id}")
def delete_access_record(id: int, db: Session = Depends(get_db)):
    access = db.query(SiteAccess).filter(SiteAccess.id == id).first()
    if access is None:
        raise HTTPException(status_code=404, detail="Access record not found")
    
    db.delete(access)
    db.commit()
    return {"detail": "Access record deleted"}
