from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from schemas import outdoor as schemas
from crud import outdoor as crud

router = APIRouter(prefix="/outdoor", tags=["Outdoor"])

# ----------- Outdoor General Layout Info -----------
@router.post("/general-layout/", response_model=schemas.OutdoorGeneralLayoutInfo)
def create_general_layout(data: schemas.OutdoorGeneralLayoutInfoCreate, db: Session = Depends(get_db)):
    return crud.create_outdoor_general_layout_info(db, data)

@router.get("/general-layout/{site_session_id}", response_model=List[schemas.OutdoorGeneralLayoutInfo])
def get_general_layout(site_session_id: int, db: Session = Depends(get_db)):
    return crud.get_outdoor_general_layout_info(db, site_session_id)

@router.put("/general-layout/{id}", response_model=schemas.OutdoorGeneralLayoutInfo)
def update_general_layout(id: int, data: dict, db: Session = Depends(get_db)):
    obj = crud.update_outdoor_general_layout_info(db, id, data)
    if not obj:
        raise HTTPException(status_code=404, detail="Not found")
    return obj

@router.delete("/general-layout/{id}")
def delete_general_layout(id: int, db: Session = Depends(get_db)):
    obj = crud.delete_outdoor_general_layout_info(db, id)
    if not obj:
        raise HTTPException(status_code=404, detail="Not found")
    return {"ok": True}

# ----------- Outdoor Cabinet -----------
@router.post("/cabinet/", response_model=schemas.OutdoorCabinet)
def create_cabinet(data: schemas.OutdoorCabinetCreate, db: Session = Depends(get_db)):
    return crud.create_outdoor_cabinet(db, data)

@router.get("/cabinet/{site_session_id}", response_model=List[schemas.OutdoorCabinet])
def get_cabinets(site_session_id: int, db: Session = Depends(get_db)):
    return crud.get_outdoor_cabinets(db, site_session_id)

@router.put("/cabinet/{id}", response_model=schemas.OutdoorCabinet)
def update_cabinet(id: int, data: dict, db: Session = Depends(get_db)):
    obj = crud.update_outdoor_cabinet(db, id, data)
    if not obj:
        raise HTTPException(status_code=404, detail="Not found")
    return obj

@router.delete("/cabinet/{id}")
def delete_cabinet(id: int, db: Session = Depends(get_db)):
    obj = crud.delete_outdoor_cabinet(db, id)
    if not obj:
        raise HTTPException(status_code=404, detail="Not found")
    return {"ok": True}

# ----------- Cabinet CB Load -----------
@router.post("/cabinet-cb-load/", response_model=schemas.CabinetCBLoad)
def create_cb_load(data: schemas.CabinetCBLoadCreate, db: Session = Depends(get_db)):
    return crud.create_cabinet_cb_load(db, data)

@router.get("/cabinet-cb-load/{cabinet_id}", response_model=List[schemas.CabinetCBLoad])
def get_cb_loads(cabinet_id: int, db: Session = Depends(get_db)):
    return crud.get_cabinet_cb_loads(db, cabinet_id)

@router.put("/cabinet-cb-load/{id}", response_model=schemas.CabinetCBLoad)
def update_cb_load(id: int, data: dict, db: Session = Depends(get_db)):
    obj = crud.update_cabinet_cb_load(db, id, data)
    if not obj:
        raise HTTPException(status_code=404, detail="Not found")
    return obj

@router.delete("/cabinet-cb-load/{id}")
def delete_cb_load(id: int, db: Session = Depends(get_db)):
    obj = crud.delete_cabinet_cb_load(db, id)
    if not obj:
        raise HTTPException(status_code=404, detail="Not found")
    return {"ok": True}

# ----------- Outdoor MW Link -----------
@router.post("/mw-link/", response_model=schemas.OutdoorMWLink)
def create_mw_link(data: schemas.OutdoorMWLinkCreate, db: Session = Depends(get_db)):
    return crud.create_outdoor_mw_link(db, data)

@router.get("/mw-link/{site_session_id}", response_model=List[schemas.OutdoorMWLink])
def get_mw_links(site_session_id: int, db: Session = Depends(get_db)):
    return crud.get_outdoor_mw_links(db, site_session_id)

@router.put("/mw-link/{id}", response_model=schemas.OutdoorMWLink)
def update_mw_link(id: int, data: dict, db: Session = Depends(get_db)):
    obj = crud.update_outdoor_mw_link(db, id, data)
    if not obj:
        raise HTTPException(status_code=404, detail="Not found")
    return obj

@router.delete("/mw-link/{id}")
def delete_mw_link(id: int, db: Session = Depends(get_db)):
    obj = crud.delete_outdoor_mw_link(db, id)
    if not obj:
        raise HTTPException(status_code=404, detail="Not found")
    return {"ok": True}

# ----------- Outdoor DC Rectifier -----------
@router.post("/dc-rectifier/", response_model=schemas.OutdoorDCRectifier)
def create_dc_rectifier(data: schemas.OutdoorDCRectifierCreate, db: Session = Depends(get_db)):
    return crud.create_outdoor_dc_rectifier(db, data)

@router.get("/dc-rectifier/{site_session_id}", response_model=List[schemas.OutdoorDCRectifier])
def get_dc_rectifiers(site_session_id: int, db: Session = Depends(get_db)):
    return crud.get_outdoor_dc_rectifiers(db, site_session_id)

@router.put("/dc-rectifier/{id}", response_model=schemas.OutdoorDCRectifier)
def update_dc_rectifier(id: int, data: dict, db: Session = Depends(get_db)):
    obj = crud.update_outdoor_dc_rectifier(db, id, data)
    if not obj:
        raise HTTPException(status_code=404, detail="Not found")
    return obj

@router.delete("/dc-rectifier/{id}")
def delete_dc_rectifier(id: int, db: Session = Depends(get_db)):
    obj = crud.delete_outdoor_dc_rectifier(db, id)
    if not obj:
        raise HTTPException(status_code=404, detail="Not found")
    return {"ok": True}

# ----------- Outdoor Battery -----------
@router.post("/battery/", response_model=schemas.OutdoorBattery)
def create_battery(data: schemas.OutdoorBatteryCreate, db: Session = Depends(get_db)):
    return crud.create_outdoor_battery(db, data)

@router.get("/battery/{site_session_id}", response_model=List[schemas.OutdoorBattery])
def get_batteries(site_session_id: int, db: Session = Depends(get_db)):
    return crud.get_outdoor_batteries(db, site_session_id)

@router.put("/battery/{id}", response_model=schemas.OutdoorBattery)
def update_battery(id: int, data: dict, db: Session = Depends(get_db)):
    obj = crud.update_outdoor_battery(db, id, data)
    if not obj:
        raise HTTPException(status_code=404, detail="Not found")
    return obj

@router.delete("/battery/{id}")
def delete_battery(id: int, db: Session = Depends(get_db)):
    obj = crud.delete_outdoor_battery(db, id)
    if not obj:
        raise HTTPException(status_code=404, detail="Not found")
    return {"ok": True}
