from sqlalchemy.orm import Session
from models.ac_panel import ACPanel
from schemas.ac_panel import ACPanelCreate

def create_ac_panel(db: Session, panel: ACPanelCreate):
    db_panel = ACPanel(**panel.dict())
    db.add(db_panel)
    db.commit()
    db.refresh(db_panel)
    return db_panel

def get_ac_panel_by_session(db: Session, session_id: int):
    return db.query(ACPanel).filter(ACPanel.site_session_id == session_id).first()
