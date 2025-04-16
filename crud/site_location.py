from sqlalchemy.orm import Session
from models.site_location import SiteLocation
from schemas.site_location import SiteLocationCreate, SiteLocationUpdate

def create_site_location(db: Session, site_data: SiteLocationCreate):
    new_site = SiteLocation(**site_data.dict())
    db.add(new_site)
    db.commit()
    db.refresh(new_site)
    return new_site

def get_site_location_by_id(db: Session, site_id: int):
    return db.query(SiteLocation).filter(SiteLocation.id == site_id).first()

def get_all_site_locations(db: Session):
    return db.query(SiteLocation).all()

def update_site_location(db: Session, site_id: int, updates: SiteLocationUpdate):
    db_site = db.query(SiteLocation).filter(SiteLocation.id == site_id).first()
    if db_site:
        for key, value in updates.dict(exclude_unset=True).items():
            setattr(db_site, key, value)
        db.commit()
        db.refresh(db_site)
    return db_site

def delete_site_location(db: Session, site_id: int):
    db_site = db.query(SiteLocation).filter(SiteLocation.id == site_id).first()
    if db_site:
        db.delete(db_site)
        db.commit()
    return db_site
