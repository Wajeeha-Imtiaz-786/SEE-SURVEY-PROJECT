from sqlalchemy.orm import Session
from models import outdoor as models
from schemas import outdoor as schemas

# ----------- Outdoor General Layout Info CRUD -----------
def create_outdoor_general_layout_info(db: Session, data: schemas.OutdoorGeneralLayoutInfoCreate):
    obj = models.OutdoorGeneralLayoutInfo(**data.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def get_outdoor_general_layout_info(db: Session, site_session_id: int):
    return db.query(models.OutdoorGeneralLayoutInfo).filter_by(site_session_id=site_session_id).all()

def update_outdoor_general_layout_info(db: Session, id: int, data: dict):
    obj = db.query(models.OutdoorGeneralLayoutInfo).filter_by(id=id).first()
    if obj:
        for k, v in data.items():
            setattr(obj, k, v)
        db.commit()
        db.refresh(obj)
    return obj

def delete_outdoor_general_layout_info(db: Session, id: int):
    obj = db.query(models.OutdoorGeneralLayoutInfo).filter_by(id=id).first()
    if obj:
        db.delete(obj)
        db.commit()
    return obj

# ----------- Outdoor Cabinet CRUD -----------
def create_outdoor_cabinet(db: Session, data: schemas.OutdoorCabinetCreate):
    data_dict = data.dict()
    data_dict['cabinet_type'] = ','.join(data_dict['cabinet_type'])
    data_dict['existing_hardware'] = ','.join(data_dict['existing_hardware'])
    obj = models.OutdoorCabinet(**data_dict)
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def get_outdoor_cabinets(db: Session, site_session_id: int):
    return db.query(models.OutdoorCabinet).filter_by(site_session_id=site_session_id).all()

def update_outdoor_cabinet(db: Session, id: int, data: dict):
    obj = db.query(models.OutdoorCabinet).filter_by(id=id).first()
    if obj:
        for k, v in data.items():
            setattr(obj, k, v)
        db.commit()
        db.refresh(obj)
    return obj

def delete_outdoor_cabinet(db: Session, id: int):
    obj = db.query(models.OutdoorCabinet).filter_by(id=id).first()
    if obj:
        db.delete(obj)
        db.commit()
    return obj

# ----------- Cabinet CB Load CRUD -----------
def create_cabinet_cb_load(db: Session, data: schemas.CabinetCBLoadCreate):
    obj = models.CabinetCBLoad(**data.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def get_cabinet_cb_loads(db: Session, cabinet_id: int):
    return db.query(models.CabinetCBLoad).filter_by(cabinet_id=cabinet_id).all()

def update_cabinet_cb_load(db: Session, id: int, data: dict):
    obj = db.query(models.CabinetCBLoad).filter_by(id=id).first()
    if obj:
        for k, v in data.items():
            setattr(obj, k, v)
        db.commit()
        db.refresh(obj)
    return obj

def delete_cabinet_cb_load(db: Session, id: int):
    obj = db.query(models.CabinetCBLoad).filter_by(id=id).first()
    if obj:
        db.delete(obj)
        db.commit()
    return obj

# ----------- Outdoor MW Link CRUD -----------
def create_outdoor_mw_link(db: Session, data: schemas.OutdoorMWLinkCreate):
    obj = models.OutdoorMWLink(**data.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def get_outdoor_mw_links(db: Session, site_session_id: int):
    return db.query(models.OutdoorMWLink).filter_by(site_session_id=site_session_id).all()

def update_outdoor_mw_link(db: Session, id: int, data: dict):
    obj = db.query(models.OutdoorMWLink).filter_by(id=id).first()
    if obj:
        for k, v in data.items():
            setattr(obj, k, v)
        db.commit()
        db.refresh(obj)
    return obj

def delete_outdoor_mw_link(db: Session, id: int):
    obj = db.query(models.OutdoorMWLink).filter_by(id=id).first()
    if obj:
        db.delete(obj)
        db.commit()
    return obj

# ----------- Outdoor DC Rectifier CRUD -----------
def create_outdoor_dc_rectifier(db: Session, data: schemas.OutdoorDCRectifierCreate):
    obj = models.OutdoorDCRectifier(**data.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def get_outdoor_dc_rectifiers(db: Session, site_session_id: int):
    return db.query(models.OutdoorDCRectifier).filter_by(site_session_id=site_session_id).all()

def update_outdoor_dc_rectifier(db: Session, id: int, data: dict):
    obj = db.query(models.OutdoorDCRectifier).filter_by(id=id).first()
    if obj:
        for k, v in data.items():
            setattr(obj, k, v)
        db.commit()
        db.refresh(obj)
    return obj

def delete_outdoor_dc_rectifier(db: Session, id: int):
    obj = db.query(models.OutdoorDCRectifier).filter_by(id=id).first()
    if obj:
        db.delete(obj)
        db.commit()
    return obj

# ----------- Outdoor Battery CRUD -----------
def create_outdoor_battery(db: Session, data: schemas.OutdoorBatteryCreate):
    obj = models.OutdoorBattery(**data.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def get_outdoor_batteries(db: Session, site_session_id: int):
    return db.query(models.OutdoorBattery).filter_by(site_session_id=site_session_id).all()

def update_outdoor_battery(db: Session, id: int, data: dict):
    obj = db.query(models.OutdoorBattery).filter_by(id=id).first()
    if obj:
        for k, v in data.items():
            setattr(obj, k, v)
        db.commit()
        db.refresh(obj)
    return obj

def delete_outdoor_battery(db: Session, id: int):
    obj = db.query(models.OutdoorBattery).filter_by(id=id).first()
    if obj:
        db.delete(obj)
        db.commit()
    return obj
