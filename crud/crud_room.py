from sqlalchemy.orm import Session
from models.room import RoomInfo, RoomPreparation, RAN, TransmissionMW, MWLink
from schemas.room import RoomInfoCreate, RoomPreparationCreate, RANCreate, TransmissionMWCreate, MWLinkCreate
from sqlalchemy.orm import Session
from fastapi import HTTPException
from models.room import TransmissionMW, MWLink
from schemas.room import TransmissionMWCreate, MWLinkUpdate
from sqlalchemy.orm import Session
from models.room import DCPowerSystem, BLVDCBLoad, LLVDCBLoad, PDUCBLoad
from schemas.room import DCPowerSystemCreate


# ---------------- RoomInfo ----------------
def create_room_info(db: Session, room_info: RoomInfoCreate):
    db_room_info = RoomInfo(**room_info.dict())
    db.add(db_room_info)
    db.commit()
    db.refresh(db_room_info)
    return db_room_info


# ---------------- RoomPreparation ----------------
def create_room_preparation(db: Session, room_preparation: RoomPreparationCreate):
    db_room_preparation = RoomPreparation(**room_preparation.dict())
    db.add(db_room_preparation)
    db.commit()
    db.refresh(db_room_preparation)
    return db_room_preparation


# ---------------- RAN ----------------
def create_ran(db: Session, ran: RANCreate):
    db_ran = RAN(**ran.dict())
    db.add(db_ran)
    db.commit()
    db.refresh(db_ran)
    return db_ran


# ---------------- TransmissionMW ----------------
def create_transmission_mw(db: Session, transmission_mw: TransmissionMWCreate):
    mw_data = transmission_mw.dict(exclude={"mw_links"})
    db_transmission_mw = TransmissionMW(**mw_data)
    db.add(db_transmission_mw)
    db.commit()
    db.refresh(db_transmission_mw)

    # Handle MWLink creation
    for link in transmission_mw.mw_links:
        db_link = MWLink(**link.dict(), transmission_mw_id=db_transmission_mw.id)
        db.add(db_link)

    db.commit()
    db.refresh(db_transmission_mw)
    return db_transmission_mw


def get_all_transmission_mw(db: Session):
    return db.query(TransmissionMW).all()


# ---------------- MWLink ----------------
def create_mw_link(db: Session, mw_link: MWLinkCreate, transmission_mw_id: int):
    db_mw_link = MWLink(**mw_link.dict(), transmission_mw_id=transmission_mw_id)
    db.add(db_mw_link)
    db.commit()
    db.refresh(db_mw_link)
    return db_mw_link


def get_mw_links_by_transmission_id(db: Session, transmission_mw_id: int):
    return db.query(MWLink).filter(MWLink.transmission_mw_id == transmission_mw_id).all()


# ---------------- Getters for All ----------------
def get_all_room_info(db: Session):
    return db.query(RoomInfo).all()

def get_all_room_preparations(db: Session):
    return db.query(RoomPreparation).all()

def get_all_ran(db: Session):
    return db.query(RAN).all()

# --------- Transmission MW ---------
def update_transmission_mw(db: Session, id: int, transmission_data: TransmissionMWCreate):
    db_record = db.query(TransmissionMW).filter(TransmissionMW.id == id).first()
    if not db_record:
        raise HTTPException(status_code=404, detail="TransmissionMW not found")
    for key, value in transmission_data.dict().items():
        setattr(db_record, key, value)
    db.commit()
    db.refresh(db_record)
    return db_record

def delete_transmission_mw(db: Session, id: int):
    db_record = db.query(TransmissionMW).filter(TransmissionMW.id == id).first()
    if not db_record:
        raise HTTPException(status_code=404, detail="TransmissionMW not found")
    db.delete(db_record)
    db.commit()
    return {"detail": "TransmissionMW deleted"}


# --------- MW Link ---------
def update_mw_link(db: Session, id: int, mw_link_data: MWLinkUpdate):
    db_link = db.query(MWLink).filter(MWLink.id == id).first()
    if not db_link:
        raise HTTPException(status_code=404, detail="MWLink not found")
    for key, value in mw_link_data.dict().items():
        setattr(db_link, key, value)
    db.commit()
    db.refresh(db_link)
    return db_link

def delete_mw_link(db: Session, id: int):
    db_link = db.query(MWLink).filter(MWLink.id == id).first()
    if not db_link:
        raise HTTPException(status_code=404, detail="MWLink not found")
    db.delete(db_link)
    db.commit()
    return {"detail": "MWLink deleted"}

# ---------------- DC Power System ----------------
def create_dc_power_system(db: Session, data: DCPowerSystemCreate):
    dc = DCPowerSystem(
        site_session_id=data.site_session_id,
        existing_dc_equipment_vendor=data.existing_dc_equipment_vendor,
        existing_dc_power_rack=data.existing_dc_power_rack,
        existing_rectifier_modules=data.existing_rectifier_modules,
        rectifier_module_model=data.rectifier_module_model,
        rectifier_module_capacity=data.rectifier_module_capacity,
        free_slots_new_rectifier=data.free_slots_new_rectifier,
        is_blvd_available=data.is_blvd_available,
        blvd_has_free_cbs=data.blvd_has_free_cbs,
        is_llvd_available=data.is_llvd_available,
        llvd_has_free_cbs=data.llvd_has_free_cbs,
        is_pdu_available=data.is_pdu_available,
        pdu_has_free_cbs=data.pdu_has_free_cbs,
        battery_strings=data.battery_strings,
        battery_type=data.battery_type,
        battery_vendor=data.battery_vendor,
        total_battery_capacity=data.total_battery_capacity,
    )
    db.add(dc)
    db.commit()
    db.refresh(dc)

    for cb in data.blvd_cb_loads:
        db.add(BLVDCBLoad(dc_power_system_id=dc.id, label=cb.label, capacity=cb.capacity))

    for cb in data.llvd_cb_loads:
        db.add(LLVDCBLoad(dc_power_system_id=dc.id, label=cb.label, capacity=cb.capacity))

    for cb in data.pdu_cb_loads:
        db.add(PDUCBLoad(dc_power_system_id=dc.id, label=cb.label, capacity=cb.capacity))

    db.commit()
    return dc
