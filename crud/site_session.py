from sqlalchemy.orm import Session
from models.site_session import SiteSession
from models.site_location import SiteLocation
from models.site_information import SiteInformation
from models.site_access import SiteAccess
import schemas.site_session as schemas


def create_site_session(db: Session, site_session: schemas.SiteSessionCreate):
    db_site_session = SiteSession(**site_session.dict())
    db.add(db_site_session)
    db.commit()
    db.refresh(db_site_session)
    return db_site_session


def get_site_session(db: Session, site_session_id: int):
    return db.query(SiteSession).filter(SiteSession.id == site_session_id).first()


def get_all_site_sessions(db: Session, skip: int = 0, limit: int = 100):
    return db.query(SiteSession).offset(skip).limit(limit).all()


def get_site_location_by_session(db: Session, site_session_id: int):
    return db.query(SiteLocation).filter(SiteLocation.site_session_id == site_session_id).first()


def get_site_information_by_session(db: Session, site_session_id: int):
    return db.query(SiteInformation).filter(SiteInformation.site_session_id == site_session_id).first()


def get_site_access_by_session(db: Session, site_session_id: int):
    return db.query(SiteAccess).filter(SiteAccess.site_session_id == site_session_id).first()
