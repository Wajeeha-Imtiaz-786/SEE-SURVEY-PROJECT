from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from database import get_db
from crud import crud_room
from crud.crud_room import (
    create_room_info, create_room_preparation, create_ran,
    create_transmission_mw, get_all_transmission_mw,
    get_mw_links_by_transmission_id, get_all_room_info, get_all_room_preparations, get_all_ran,
    update_transmission_mw, delete_transmission_mw,
    update_mw_link, delete_mw_link,
    create_dc_power_system, create_blvd_cb_load, get_blvd_cb_loads_by_dc_id,
    update_blvd_cb_load, delete_blvd_cb_load,
    create_llvd_cb_load, get_llvd_cb_loads_by_dc_id,
    update_llvd_cb_load, delete_llvd_cb_load,
    create_pdu_cb_load, get_pdu_cb_loads_by_dc_id,
    update_pdu_cb_load, delete_pdu_cb_load
)
from schemas.room import (
    RoomInfoCreate, RoomInfoOut,
    RoomPreparationCreate, RoomPreparationOut,
    RANCreate, RANOut,
    TransmissionMWCreate, TransmissionMWOut,
    MWLinkOut, MWLinkUpdate,
    DCPowerSystemCreate, DCPowerSystem as DCPowerSystemOut,
    BLVDCBLoadCreate, BLVDCBLoadOut,
    LLVDCBLoadCreate, LLVDCBLoadOut,
    PDUCBLoadCreate, PDUCBLoadOut
)
from models.room import RoomInfo, RoomPreparation, RAN, BLVDCBLoad

router = APIRouter(prefix="/room", tags=["Room"])

# ---------- RoomInfo ----------
@router.post("/info", response_model=RoomInfoOut)
def add_room_info(room_info: RoomInfoCreate, db: Session = Depends(get_db)):
    return create_room_info(db, room_info)

@router.get("/info", response_model=List[RoomInfoOut])
def list_room_info(db: Session = Depends(get_db)):
    return get_all_room_info(db)

@router.put("/info/{id}", response_model=RoomInfoOut)
def update_room_info(id: int, room_info: RoomInfoCreate, db: Session = Depends(get_db)):
    db_room_info = db.query(RoomInfo).filter(RoomInfo.id == id).first()
    if not db_room_info:
        raise HTTPException(status_code=404, detail="RoomInfo not found")
    for key, value in room_info.dict().items():
        setattr(db_room_info, key, value)
    db.commit()
    db.refresh(db_room_info)
    return db_room_info

@router.delete("/info/{id}")
def delete_room_info(id: int, db: Session = Depends(get_db)):
    db_room_info = db.query(RoomInfo).filter(RoomInfo.id == id).first()
    if not db_room_info:
        raise HTTPException(status_code=404, detail="RoomInfo not found")
    db.delete(db_room_info)
    db.commit()
    return {"detail": "RoomInfo deleted"}


# ---------- RoomPreparation ----------
@router.post("/preparation", response_model=RoomPreparationOut)
def add_room_preparation(room_preparation: RoomPreparationCreate, db: Session = Depends(get_db)):
    return create_room_preparation(db, room_preparation)

@router.get("/preparation", response_model=List[RoomPreparationOut])
def list_room_preparations(db: Session = Depends(get_db)):
    return get_all_room_preparations(db)

@router.put("/preparation/{id}", response_model=RoomPreparationOut)
def update_room_preparation(id: int, room_preparation: RoomPreparationCreate, db: Session = Depends(get_db)):
    db_room_preparation = db.query(RoomPreparation).filter(RoomPreparation.id == id).first()
    if not db_room_preparation:
        raise HTTPException(status_code=404, detail="RoomPreparation not found")
    for key, value in room_preparation.dict().items():
        setattr(db_room_preparation, key, value)
    db.commit()
    db.refresh(db_room_preparation)
    return db_room_preparation

@router.delete("/preparation/{id}")
def delete_room_preparation(id: int, db: Session = Depends(get_db)):
    db_room_preparation = db.query(RoomPreparation).filter(RoomPreparation.id == id).first()
    if not db_room_preparation:
        raise HTTPException(status_code=404, detail="RoomPreparation not found")
    db.delete(db_room_preparation)
    db.commit()
    return {"detail": "RoomPreparation deleted"}


# ---------- RAN ----------
@router.post("/ran", response_model=RANOut)
def add_ran(ran: RANCreate, db: Session = Depends(get_db)):
    return create_ran(db, ran)

@router.get("/ran", response_model=List[RANOut])
def list_ran(db: Session = Depends(get_db)):
    return get_all_ran(db)

@router.put("/ran/{id}", response_model=RANOut)
def update_ran(id: int, ran: RANCreate, db: Session = Depends(get_db)):
    db_ran = db.query(RAN).filter(RAN.id == id).first()
    if not db_ran:
        raise HTTPException(status_code=404, detail="RAN not found")
    for key, value in ran.dict().items():
        setattr(db_ran, key, value)
    db.commit()
    db.refresh(db_ran)
    return db_ran

@router.delete("/ran/{id}")
def delete_ran(id: int, db: Session = Depends(get_db)):
    db_ran = db.query(RAN).filter(RAN.id == id).first()
    if not db_ran:
        raise HTTPException(status_code=404, detail="RAN not found")
    db.delete(db_ran)
    db.commit()
    return {"detail": "RAN deleted"}


# ---------- Transmission MW ----------
@router.post("/transmission", response_model=TransmissionMWOut)
def add_transmission_mw(transmission_mw: TransmissionMWCreate, db: Session = Depends(get_db)):
    return create_transmission_mw(db, transmission_mw)

@router.get("/transmission", response_model=List[TransmissionMWOut])
def list_transmission_mw(db: Session = Depends(get_db)):
    return get_all_transmission_mw(db)

@router.put("/transmission/{id}", response_model=TransmissionMWOut)
def update_transmission_mw_record(id: int, transmission_mw: TransmissionMWCreate, db: Session = Depends(get_db)):
    return update_transmission_mw(db, id, transmission_mw)

@router.delete("/transmission/{id}")
def delete_transmission_mw_record(id: int, db: Session = Depends(get_db)):
    return delete_transmission_mw(db, id)


# ---------- MW Links ----------
@router.get("/transmission/{transmission_id}/mw-links", response_model=List[MWLinkOut])
def list_mw_links_for_transmission(transmission_id: int, db: Session = Depends(get_db)):
    return get_mw_links_by_transmission_id(db, transmission_id)

@router.put("/mw-link/{id}", response_model=MWLinkOut)
def update_mw_link_record(id: int, mw_link: MWLinkUpdate, db: Session = Depends(get_db)):
    return update_mw_link(db, id, mw_link)

@router.delete("/mw-link/{id}")
def delete_mw_link_record(id: int, db: Session = Depends(get_db)):
    return delete_mw_link(db, id)


@router.post("/", response_model=DCPowerSystemOut)
def create_dc_power(data: DCPowerSystemCreate, db: Session = Depends(get_db)):
    return crud_room.create_dc_power_system(db, data)


 #---------- PDU CB Load ----------
@router.post("/dc-power/pdu", response_model=PDUCBLoadOut)
def add_pdu_cb_load(data: PDUCBLoadCreate, db: Session = Depends(get_db)):
    return create_pdu_cb_load(db, data)

@router.get("/dc-power/pdu/{dc_power_system_id}", response_model=List[PDUCBLoadOut])
def get_pdu_cb_loads(dc_power_system_id: int, db: Session = Depends(get_db)):
    return get_pdu_cb_loads_by_dc_id(db, dc_power_system_id)

@router.put("/dc-power/pdu/{id}", response_model=PDUCBLoadOut)
def update_pdu_cb_load_endpoint(id: int, data: PDUCBLoadCreate, db: Session = Depends(get_db)):
    return update_pdu_cb_load(db, id, data)

@router.delete("/dc-power/pdu/{id}")
def delete_pdu_cb_load_endpoint(id: int, db: Session = Depends(get_db)):
    return delete_pdu_cb_load(db, id)

# ---------- LLVD CB Load ----------
@router.post("/dc-power/llvd", response_model=LLVDCBLoadOut)
def add_llvd_cb_load(data: LLVDCBLoadCreate, db: Session = Depends(get_db)):
    return create_llvd_cb_load(db, data)

@router.get("/dc-power/llvd/{dc_power_system_id}", response_model=List[LLVDCBLoadOut])
def get_llvd_cb_loads(dc_power_system_id: int, db: Session = Depends(get_db)):
    return get_llvd_cb_loads_by_dc_id(db, dc_power_system_id)

@router.put("/dc-power/llvd/{id}", response_model=LLVDCBLoadOut)
def update_llvd_cb_load_endpoint(id: int, data: LLVDCBLoadCreate, db: Session = Depends(get_db)):
    return update_llvd_cb_load(db, id, data)

@router.delete("/dc-power/llvd/{id}")
def delete_llvd_cb_load_endpoint(id: int, db: Session = Depends(get_db)):
    return delete_llvd_cb_load(db, id)

# ---------- BLVD CB Load ----------
@router.post("/dc-power/blvd", response_model=BLVDCBLoadOut)
def add_blvd_cb_load(data: BLVDCBLoadCreate, db: Session = Depends(get_db)):
    return create_blvd_cb_load(db, data)

@router.get("/dc-power/blvd/{dc_power_system_id}", response_model=List[BLVDCBLoadOut])
def get_blvd_cb_loads(dc_power_system_id: int, db: Session = Depends(get_db)):
    return get_blvd_cb_loads_by_dc_id(db, dc_power_system_id)

@router.put("/dc-power/blvd/{id}", response_model=BLVDCBLoadOut)
def update_blvd_cb_load_endpoint(id: int, data: BLVDCBLoadCreate, db: Session = Depends(get_db)):
    return update_blvd_cb_load(db, id, data)

@router.delete("/dc-power/blvd/{id}")
def delete_blvd_cb_load_endpoint(id: int, db: Session = Depends(get_db)):
    return delete_blvd_cb_load(db, id)
