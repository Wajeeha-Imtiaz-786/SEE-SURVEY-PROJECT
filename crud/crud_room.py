from sqlalchemy.orm import Session
from models.room import RoomInfo, RoomPreparation, RAN
from schemas.room import RoomInfoCreate, RoomPreparationCreate, RANCreate

def create_room_info(db: Session, room_info: RoomInfoCreate):
    db_room_info = RoomInfo(**room_info.dict())
    db.add(db_room_info)
    db.commit()
    db.refresh(db_room_info)
    return db_room_info

def create_room_preparation(db: Session, room_preparation: RoomPreparationCreate):
    db_room_preparation = RoomPreparation(**room_preparation.dict())
    db.add(db_room_preparation)
    db.commit()
    db.refresh(db_room_preparation)
    return db_room_preparation

def create_ran(db: Session, ran: RANCreate):
    db_ran = RAN(**ran.dict())
    db.add(db_ran)
    db.commit()
    db.refresh(db_ran)
    return db_ran

def get_all_room_info(db: Session):
    return db.query(RoomInfo).all()

def get_all_room_preparations(db: Session):
    return db.query(RoomPreparation).all()

def get_all_ran(db: Session):
    return db.query(RAN).all()
