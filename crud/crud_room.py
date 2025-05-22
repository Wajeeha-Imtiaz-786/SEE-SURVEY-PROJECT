from fastapi import HTTPException
from sqlalchemy.orm import Session
from models.room import (
    RoomInfo, RoomPreparation, RAN, TransmissionMW, MWLink,
    DCPowerSystem, BLVDCBLoad, LLVDCBLoad, PDUCBLoad
)
from schemas.room import (
    RoomInfoCreate, RoomInfoUpdate,
    RoomPreparationCreate, RoomPreparationUpdate,
    RANCreate, RANUpdate,
    TransmissionMWCreate, TransmissionMWUpdate, MWLinkCreate, MWLinkUpdate,
    DCSystemCreate, BLVDCBLoadCreate, LLVDCBLoadCreate, PDUCBLoadCreate
)


# ---------------- RoomInfo ----------------
def create_room_info(db: Session, data: RoomInfoCreate):
    db_obj = RoomInfo(**data.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def get_room_info(db: Session, id: int):
    return db.query(RoomInfo).filter(RoomInfo.id == id).first()

def get_all_room_info(db: Session):
    return db.query(RoomInfo).all()

def update_room_info(db: Session, id: int, data: RoomInfoUpdate):
    db_obj = db.query(RoomInfo).filter(RoomInfo.id == id).first()
    if not db_obj:
        raise HTTPException(status_code=404, detail="RoomInfo not found")
    for key, value in data.dict().items():
        setattr(db_obj, key, value)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def delete_room_info(db: Session, id: int):
    db_obj = db.query(RoomInfo).filter(RoomInfo.id == id).first()
    if not db_obj:
        raise HTTPException(status_code=404, detail="RoomInfo not found")
    db.delete(db_obj)
    db.commit()
    return {"detail": "RoomInfo deleted"}


# ---------------- RoomPreparation ----------------
def create_room_preparation(db: Session, data: RoomPreparationCreate):
    db_obj = RoomPreparation(**data.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def get_room_preparation(db: Session, id: int):
    return db.query(RoomPreparation).filter(RoomPreparation.id == id).first()

def get_all_room_preparations(db: Session):
    return db.query(RoomPreparation).all()

def update_room_preparation(db: Session, id: int, data: RoomPreparationUpdate):
    db_obj = db.query(RoomPreparation).filter(RoomPreparation.id == id).first()
    if not db_obj:
        raise HTTPException(status_code=404, detail="RoomPreparation not found")
    for key, value in data.dict().items():
        setattr(db_obj, key, value)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def delete_room_preparation(db: Session, id: int):
    db_obj = db.query(RoomPreparation).filter(RoomPreparation.id == id).first()
    if not db_obj:
        raise HTTPException(status_code=404, detail="RoomPreparation not found")
    db.delete(db_obj)
    db.commit()
    return {"detail": "RoomPreparation deleted"}


# ---------------- RAN ----------------
def create_ran(db: Session, data: RANCreate):
    db_obj = RAN(**data.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def get_ran(db: Session, id: int):
    return db.query(RAN).filter(RAN.id == id).first()

def get_all_ran(db: Session):
    return db.query(RAN).all()

def update_ran(db: Session, id: int, data: RANUpdate):
    db_obj = db.query(RAN).filter(RAN.id == id).first()
    if not db_obj:
        raise HTTPException(status_code=404, detail="RAN not found")
    for key, value in data.dict().items():
        setattr(db_obj, key, value)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def delete_ran(db: Session, id: int):
    db_obj = db.query(RAN).filter(RAN.id == id).first()
    if not db_obj:
        raise HTTPException(status_code=404, detail="RAN not found")
    db.delete(db_obj)
    db.commit()
    return {"detail": "RAN deleted"}


# ---------------- Transmission MW ----------------
def create_transmission_mw(db: Session, data: TransmissionMWCreate):
    mw_data = data.dict(exclude={"mw_links"})
    db_obj = TransmissionMW(**mw_data)
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    # Now add MWLink records if provided
    if data.mw_links:
        for link in data.mw_links:
            db_link = MWLink(**link.dict(), transmission_mw_id=db_obj.id)
            db.add(db_link)
        db.commit()
    return db_obj

def get_transmission_mw(db: Session, id: int):
    return db.query(TransmissionMW).filter(TransmissionMW.id == id).first()

def get_all_transmission_mw(db: Session):
    return db.query(TransmissionMW).all()

def update_transmission_mw(db: Session, id: int, data: TransmissionMWUpdate):
    db_obj = db.query(TransmissionMW).filter(TransmissionMW.id == id).first()
    if not db_obj:
        raise HTTPException(status_code=404, detail="TransmissionMW not found")
    for key, value in data.dict().items():
        setattr(db_obj, key, value)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def delete_transmission_mw(db: Session, id: int):
    db_obj = db.query(TransmissionMW).filter(TransmissionMW.id == id).first()
    if not db_obj:
        raise HTTPException(status_code=404, detail="TransmissionMW not found")
    db.delete(db_obj)
    db.commit()
    return {"detail": "TransmissionMW deleted"}


# ---------------- MW Link ----------------
def create_mw_link(db: Session, data: MWLinkCreate, transmission_mw_id: int):
    db_obj = MWLink(**data.dict(), transmission_mw_id=transmission_mw_id)
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def get_mw_link(db: Session, id: int):
    return db.query(MWLink).filter(MWLink.id == id).first()

def get_mw_links_by_transmission_id(db: Session, transmission_mw_id: int):
    """
    Get all MWLink records for a given TransmissionMW ID.
    """
    return db.query(MWLink).filter(MWLink.transmission_mw_id == transmission_mw_id).all()

def update_mw_link(db: Session, id: int, data: MWLinkUpdate):
    db_obj = db.query(MWLink).filter(MWLink.id == id).first()
    if not db_obj:
        raise HTTPException(status_code=404, detail="MWLink not found")
    for key, value in data.dict().items():
        setattr(db_obj, key, value)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def delete_mw_link(db: Session, id: int):
    db_obj = db.query(MWLink).filter(MWLink.id == id).first()
    if not db_obj:
        raise HTTPException(status_code=404, detail="MWLink not found")
    db.delete(db_obj)
    db.commit()
    return {"detail": "MWLink deleted"}


# ---------------- DC Power System ----------------
def create_dc_power_system(db: Session, data: DCSystemCreate):
    dc = DCPowerSystem(**data.dict(exclude={"blvd_cb_loads", "llvd_cb_loads", "pdu_cb_loads"}))
    db.add(dc)
    db.commit()
    db.refresh(dc)

    for cb in data.blvd_cb_loads:
        db.add(BLVDCBLoad(dc_power_system_id=dc.id, **cb.dict()))
    for cb in data.llvd_cb_loads:
        db.add(LLVDCBLoad(dc_power_system_id=dc.id, **cb.dict()))
    for cb in data.pdu_cb_loads:
        db.add(PDUCBLoad(dc_power_system_id=dc.id, **cb.dict()))

    db.commit()
    return dc

def create_blvd_cb_load(db: Session, data: BLVDCBLoadCreate):
    db_obj = BLVDCBLoad(**data.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def get_blvd_cb_loads_by_dc_id(db: Session, dc_power_system_id: int):
    """
    Get all BLVDCBLoad records for a given DC Power System ID.
    """
    return db.query(BLVDCBLoad).filter(BLVDCBLoad.dc_power_system_id == dc_power_system_id).all()

def update_blvd_cb_load(db: Session, id: int, data: BLVDCBLoadCreate):
    db_obj = db.query(BLVDCBLoad).filter(BLVDCBLoad.id == id).first()
    if not db_obj:
        raise HTTPException(status_code=404, detail="BLVDCBLoad not found")
    for key, value in data.dict().items():
        setattr(db_obj, key, value)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def delete_blvd_cb_load(db: Session, id: int):
    db_obj = db.query(BLVDCBLoad).filter(BLVDCBLoad.id == id).first()
    if not db_obj:
        raise HTTPException(status_code=404, detail="BLVDCBLoad not found")
    db.delete(db_obj)
    db.commit()
    return {"detail": "BLVDCBLoad deleted"}

def create_llvd_cb_load(db: Session, data: LLVDCBLoadCreate):
    db_obj = LLVDCBLoad(**data.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def get_llvd_cb_loads_by_dc_id(db: Session, dc_power_system_id: int):
    """
    Get all LLVDCBLoad records for a given DC Power System ID.
    """
    return db.query(LLVDCBLoad).filter(LLVDCBLoad.dc_power_system_id == dc_power_system_id).all()

def update_llvd_cb_load(db: Session, id: int, data: LLVDCBLoadCreate):
    db_obj = db.query(LLVDCBLoad).filter(LLVDCBLoad.id == id).first()
    if not db_obj:
        raise HTTPException(status_code=404, detail="LLVDCBLoad not found")
    for key, value in data.dict().items():
        setattr(db_obj, key, value)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def delete_llvd_cb_load(db: Session, id: int):
    db_obj = db.query(LLVDCBLoad).filter(LLVDCBLoad.id == id).first()
    if not db_obj:
        raise HTTPException(status_code=404, detail="LLVDCBLoad not found")
    db.delete(db_obj)
    db.commit()
    return {"detail": "LLVDCBLoad deleted"}

def create_pdu_cb_load(db: Session, data: PDUCBLoadCreate):
    db_obj = PDUCBLoad(**data.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def get_pdu_cb_loads_by_dc_id(db: Session, dc_power_system_id: int):
    """
    Get all PDUCBLoad records for a given DC Power System ID.
    """
    return db.query(PDUCBLoad).filter(PDUCBLoad.dc_system_id == dc_power_system_id).all()

def update_pdu_cb_load(db: Session, id: int, data: PDUCBLoadCreate):
    db_obj = db.query(PDUCBLoad).filter(PDUCBLoad.id == id).first()
    if not db_obj:
        raise HTTPException(status_code=404, detail="PDUCBLoad not found")
    for key, value in data.dict().items():
        setattr(db_obj, key, value)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def delete_pdu_cb_load(db: Session, id: int):
    db_obj = db.query(PDUCBLoad).filter(PDUCBLoad.id == id).first()
    if not db_obj:
        raise HTTPException(status_code=404, detail="PDUCBLoad not found")
    db.delete(db_obj)
    db.commit()
    return {"detail": "PDUCBLoad deleted"}
