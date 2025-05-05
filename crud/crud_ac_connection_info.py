from sqlalchemy.orm import Session
from models.ac_connection_info import ACConnectionInfo
from schemas.ac_connection_info import ACConnectionInfoCreate

def create_ac_connection_info(db: Session, info: ACConnectionInfoCreate):
    db_info = ACConnectionInfo(**info.dict())
    db.add(db_info)
    db.commit()
    db.refresh(db_info)
    return db_info

def get_ac_connection_info_by_session(db: Session, session_id: int):
    return db.query(ACConnectionInfo).filter(ACConnectionInfo.site_session_id == session_id).first()
