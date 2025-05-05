from sqlalchemy.orm import Session
from models.ac_panel_cb_load import ACPanelCBLoad
from schemas.ac_panel_cb_load import ACPanelCBLoadCreate

def create_cb_load(db: Session, load: ACPanelCBLoadCreate):
    db_load = ACPanelCBLoad(**load.dict())
    db.add(db_load)
    db.commit()
    db.refresh(db_load)
    return db_load

def get_cb_loads_by_panel(db: Session, ac_panel_id: int):
    return db.query(ACPanelCBLoad).filter(ACPanelCBLoad.ac_panel_id == ac_panel_id).all()
