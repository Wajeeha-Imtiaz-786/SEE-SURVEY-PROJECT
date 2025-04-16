from sqlalchemy.orm import Session
from models.site_access import SiteAccess
from schemas.site_access import SiteAccessCreate, SiteAccessUpdate

def create_site_access(db: Session, access_data: SiteAccessCreate):
    access = SiteAccess(**access_data.dict())
    db.add(access)
    db.commit()
    db.refresh(access)
    return access

def get_site_access_by_id(db: Session, access_id: int):
    return db.query(SiteAccess).filter(SiteAccess.id == access_id).first()

def get_all_site_access_entries(db: Session):
    return db.query(SiteAccess).all()

def update_site_access(db: Session, access_id: int, updates: SiteAccessUpdate):
    db_access = db.query(SiteAccess).filter(SiteAccess.id == access_id).first()
    if db_access:
        for key, value in updates.dict(exclude_unset=True).items():
            setattr(db_access, key, value)
        db.commit()
        db.refresh(db_access)
    return db_access

def delete_site_access(db: Session, access_id: int):
    db_access = db.query(SiteAccess).filter(SiteAccess.id == access_id).first()
    if db_access:
        db.delete(db_access)
        db.commit()
    return db_access
