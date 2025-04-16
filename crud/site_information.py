from sqlalchemy.orm import Session
from models.site_information import SiteInformation
from schemas.site_information import SiteInformationCreate, SiteInformationUpdate

def create_site_information(db: Session, info_data: SiteInformationCreate):
    info = SiteInformation(**info_data.dict())
    db.add(info)
    db.commit()
    db.refresh(info)
    return info

def get_site_information_by_id(db: Session, info_id: int):
    return db.query(SiteInformation).filter(SiteInformation.id == info_id).first()

def get_all_site_information(db: Session):
    return db.query(SiteInformation).all()

def update_site_information(db: Session, info_id: int, updates: SiteInformationUpdate):
    db_info = db.query(SiteInformation).filter(SiteInformation.id == info_id).first()
    if db_info:
        for key, value in updates.dict(exclude_unset=True).items():
            setattr(db_info, key, value)
        db.commit()
        db.refresh(db_info)
    return db_info

def delete_site_information(db: Session, info_id: int):
    db_info = db.query(SiteInformation).filter(SiteInformation.id == info_id).first()
    if db_info:
        db.delete(db_info)
        db.commit()
    return db_info
