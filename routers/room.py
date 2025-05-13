from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from crud.crud_room import (
    create_room_info, create_room_preparation, create_ran,
    get_all_room_info, get_all_room_preparations, get_all_ran
)
from schemas.room import RoomInfoCreate, RoomInfoOut, RoomPreparationCreate, RoomPreparationOut, RANCreate, RANOut
from models.room import RoomInfo, RoomPreparation, RAN

router = APIRouter(prefix="/room", tags=["Room"])

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
