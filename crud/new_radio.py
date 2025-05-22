from sqlalchemy.orm import Session
from fastapi import HTTPException
from models import new_radio as models
from schemas import new_radio as schemas


# -------- New Radio Installation --------
def create_new_radio_installation(db: Session, data: schemas.NewRadioInstallationCreate):
    obj = models.NewRadioInstallation(**data.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def get_new_radio_installations(db: Session, site_session_id: int):
    return db.query(models.NewRadioInstallation).filter_by(site_session_id=site_session_id).all()

def get_new_radio_installation(db: Session, id: int):
    return db.query(models.NewRadioInstallation).filter_by(id=id).first()

def update_new_radio_installation(db: Session, id: int, data: schemas.NewRadioInstallationUpdate):
    obj = get_new_radio_installation(db, id)
    if not obj:
        raise HTTPException(status_code=404, detail="Installation not found")
    for key, value in data.dict().items():
        setattr(obj, key, value)
    db.commit()
    db.refresh(obj)
    return obj

def delete_new_radio_installation(db: Session, id: int):
    obj = get_new_radio_installation(db, id)
    if not obj:
        raise HTTPException(status_code=404, detail="Installation not found")
    db.delete(obj)
    db.commit()
    return {"detail": "Deleted"}


# -------- New Antenna --------
def create_new_antenna(db: Session, data: schemas.NewAntennaCreate):
    obj = models.NewAntenna(**data.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def get_new_antennas(db: Session, site_session_id: int):
    return db.query(models.NewAntenna).filter_by(site_session_id=site_session_id).all()

def get_new_antenna(db: Session, id: int):
    return db.query(models.NewAntenna).filter_by(id=id).first()

def update_new_antenna(db: Session, id: int, data: schemas.NewAntennaUpdate):
    obj = get_new_antenna(db, id)
    if not obj:
        raise HTTPException(status_code=404, detail="Antenna not found")
    for key, value in data.dict().items():
        setattr(obj, key, value)
    db.commit()
    db.refresh(obj)
    return obj

def delete_new_antenna(db: Session, id: int):
    obj = get_new_antenna(db, id)
    if not obj:
        raise HTTPException(status_code=404, detail="Antenna not found")
    db.delete(obj)
    db.commit()
    return {"detail": "Deleted"}


# -------- New Radio Unit --------
def create_new_radio_unit(db: Session, data: schemas.NewRadioUnitCreate):
    obj = models.NewRadioUnit(**data.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def get_new_radio_units(db: Session, site_session_id: int):
    return db.query(models.NewRadioUnit).filter_by(site_session_id=site_session_id).all()

def get_new_radio_unit(db: Session, id: int):
    return db.query(models.NewRadioUnit).filter_by(id=id).first()

def update_new_radio_unit(db: Session, id: int, data: schemas.NewRadioUnitUpdate):
    obj = get_new_radio_unit(db, id)
    if not obj:
        raise HTTPException(status_code=404, detail="Radio unit not found")
    for key, value in data.dict().items():
        setattr(obj, key, value)
    db.commit()
    db.refresh(obj)
    return obj

def delete_new_radio_unit(db: Session, id: int):
    obj = get_new_radio_unit(db, id)
    if not obj:
        raise HTTPException(status_code=404, detail="Radio unit not found")
    db.delete(obj)
    db.commit()
    return {"detail": "Deleted"}


# -------- New FPFH --------
def create_new_fpfh(db: Session, data: schemas.NewFPFHCreate):
    obj = models.NewFPFH(**data.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def get_new_fpfhs(db: Session, site_session_id: int):
    return db.query(models.NewFPFH).filter_by(site_session_id=site_session_id).all()

def get_new_fpfh(db: Session, id: int):
    return db.query(models.NewFPFH).filter_by(id=id).first()

def update_new_fpfh(db: Session, id: int, data: schemas.NewFPFHUpdate):
    obj = get_new_fpfh(db, id)
    if not obj:
        raise HTTPException(status_code=404, detail="FPFH not found")
    for key, value in data.dict().items():
        setattr(obj, key, value)
    db.commit()
    db.refresh(obj)
    return obj

def delete_new_fpfh(db: Session, id: int):
    obj = get_new_fpfh(db, id)
    if not obj:
        raise HTTPException(status_code=404, detail="FPFH not found")
    db.delete(obj)
    db.commit()
    return {"detail": "Deleted"}


# -------- GPS --------
def create_gps(db: Session, data: schemas.GPSCreate):
    obj = models.NewGPS(**data.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def get_new_gps_records(db: Session, site_session_id: int):
    return db.query(models.NewGPS).filter_by(site_session_id=site_session_id).all()

def get_gps(db: Session, id: int):
    return db.query(models.NewGPS).filter_by(id=id).first()

def update_gps(db: Session, id: int, data: schemas.GPSUpdate):
    obj = get_gps(db, id)
    if not obj:
        raise HTTPException(status_code=404, detail="GPS record not found")
    for key, value in data.dict().items():
        setattr(obj, key, value)
    db.commit()
    db.refresh(obj)
    return obj

def delete_gps(db: Session, id: int):
    obj = get_gps(db, id)
    if not obj:
        raise HTTPException(status_code=404, detail="GPS record not found")
    db.delete(obj)
    db.commit()
    return {"detail": "Deleted"}

 #Generic CRUD pattern
def create_new_radio_installation(db: Session, data: schemas.NewRadioInstallationCreate):
    obj = models.NewRadioInstallation(**data.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def get_new_radio_installations(db: Session, site_session_id: int):
    return db.query(models.NewRadioInstallation).filter_by(site_session_id=site_session_id).all()


def create_new_antenna(db: Session, data: schemas.NewAntennaCreate):
    obj = models.NewAntenna(**data.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def get_new_antennas(db: Session, site_session_id: int):
    return db.query(models.NewAntenna).filter_by(site_session_id=site_session_id).all()


def create_new_radio_unit(db: Session, data: schemas.NewRadioUnitCreate):
    obj = models.NewRadioUnit(**data.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def get_new_radio_units(db: Session, site_session_id: int):
    return db.query(models.NewRadioUnit).filter_by(site_session_id=site_session_id).all()


def create_new_fpfh(db: Session, data: schemas.NewFPFHCreate):
    obj = models.NewFPFH(**data.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def get_new_fpfhs(db: Session, site_session_id: int):
    return db.query(models.NewFPFH).filter_by(site_session_id=site_session_id).all()


def create_new_gps(db: Session, data: schemas.GPSCreate):
    obj = models.NewGPS(**data.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def get_new_gps_records(db: Session, site_session_id: int):
    return db.query(models.NewGPS).filter_by(site_session_id=site_session_id).all()
