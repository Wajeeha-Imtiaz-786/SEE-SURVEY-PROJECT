from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from schemas import existing_radio as schemas
from crud import existing_radio as crud

router = APIRouter(prefix="/existing-radio", tags=["Existing Radio"])

# 1. Antenna Structure Info
@router.post("/antenna-structure/", response_model=schemas.AntennaStructureInfo)
def create_antenna_structure(data: schemas.AntennaStructureInfoCreate, db: Session = Depends(get_db)):
    return crud.create_antenna_structure_info(db, data)

@router.get("/antenna-structure/{site_session_id}", response_model=List[schemas.AntennaStructureInfo])
def get_antenna_structures(site_session_id: int, db: Session = Depends(get_db)):
    return crud.get_antenna_structure_info(db, site_session_id)

@router.put("/antenna-structure/{id}", response_model=schemas.AntennaStructureInfo)
def update_antenna_structure(id: int, data: dict, db: Session = Depends(get_db)):
    obj = crud.update_antenna_structure_info(db, id, data)
    if not obj:
        raise HTTPException(status_code=404, detail="Not found")
    return obj

@router.delete("/antenna-structure/{id}")
def delete_antenna_structure(id: int, db: Session = Depends(get_db)):
    obj = crud.delete_antenna_structure_info(db, id)
    if not obj:
        raise HTTPException(status_code=404, detail="Not found")
    return {"ok": True}

# 2. MW Antennas
@router.post("/mw-antenna/", response_model=schemas.MWAntennas)
def create_mw_antenna(data: schemas.MWAntennasCreate, db: Session = Depends(get_db)):
    return crud.create_mw_antenna(db, data)

@router.get("/mw-antenna/{site_session_id}", response_model=List[schemas.MWAntennas])
def get_mw_antennas(site_session_id: int, db: Session = Depends(get_db)):
    return crud.get_mw_antennas(db, site_session_id)

@router.put("/mw-antenna/{id}", response_model=schemas.MWAntennas)
def update_mw_antenna(id: int, data: dict, db: Session = Depends(get_db)):
    obj = crud.update_mw_antenna(db, id, data)
    if not obj:
        raise HTTPException(status_code=404, detail="Not found")
    return obj

@router.delete("/mw-antenna/{id}")
def delete_mw_antenna(id: int, db: Session = Depends(get_db)):
    obj = crud.delete_mw_antenna(db, id)
    if not obj:
        raise HTTPException(status_code=404, detail="Not found")
    return {"ok": True}

# 3. External DC PDU
@router.post("/external-dc-pdu/", response_model=schemas.ExternalDCPDU)
def create_external_dc_pdu(data: schemas.ExternalDCPDUCreate, db: Session = Depends(get_db)):
    return crud.create_external_dc_pdu(db, data)

@router.get("/external-dc-pdu/{site_session_id}", response_model=List[schemas.ExternalDCPDU])
def get_external_dc_pdus(site_session_id: int, db: Session = Depends(get_db)):
    return crud.get_external_dc_pdus(db, site_session_id)

@router.put("/external-dc-pdu/{id}", response_model=schemas.ExternalDCPDU)
def update_external_dc_pdu(id: int, data: dict, db: Session = Depends(get_db)):
    obj = crud.update_external_dc_pdu(db, id, data)
    if not obj:
        raise HTTPException(status_code=404, detail="Not found")
    return obj

@router.delete("/external-dc-pdu/{id}")
def delete_external_dc_pdu(id: int, db: Session = Depends(get_db)):
    obj = crud.delete_external_dc_pdu(db, id)
    if not obj:
        raise HTTPException(status_code=404, detail="Not found")
    return {"ok": True}

# 3.1. DC PDU CB/Fuse
@router.post("/dcpdu-cb-fuse/", response_model=schemas.DCPDUCBFuse)
def create_dcpdu_cb_fuse(data: schemas.DCPDUCBFuseCreate, db: Session = Depends(get_db)):
    return crud.create_dcpdu_cb_fuse(db, data)

@router.get("/dcpdu-cb-fuse/{pdu_id}", response_model=List[schemas.DCPDUCBFuse])
def get_dcpdu_cb_fuses(pdu_id: int, db: Session = Depends(get_db)):
    return crud.get_dcpdu_cb_fuses(db, pdu_id)

@router.put("/dcpdu-cb-fuse/{id}", response_model=schemas.DCPDUCBFuse)
def update_dcpdu_cb_fuse(id: int, data: dict, db: Session = Depends(get_db)):
    obj = crud.update_dcpdu_cb_fuse(db, id, data)
    if not obj:
        raise HTTPException(status_code=404, detail="Not found")
    return obj

@router.delete("/dcpdu-cb-fuse/{id}")
def delete_dcpdu_cb_fuse(id: int, db: Session = Depends(get_db)):
    obj = crud.delete_dcpdu_cb_fuse(db, id)
    if not obj:
        raise HTTPException(status_code=404, detail="Not found")
    return {"ok": True}

# 4. Radio Antennas
@router.post("/radio-antenna/", response_model=schemas.RadioAntenna)
def create_radio_antenna(data: schemas.RadioAntennaCreate, db: Session = Depends(get_db)):
    return crud.create_radio_antenna(db, data)

@router.get("/radio-antenna/{site_session_id}", response_model=List[schemas.RadioAntenna])
def get_radio_antennas(site_session_id: int, db: Session = Depends(get_db)):
    return crud.get_radio_antennas(db, site_session_id)

@router.put("/radio-antenna/{id}", response_model=schemas.RadioAntenna)
def update_radio_antenna(id: int, data: dict, db: Session = Depends(get_db)):
    obj = crud.update_radio_antenna(db, id, data)
    if not obj:
        raise HTTPException(status_code=404, detail="Not found")
    return obj

@router.delete("/radio-antenna/{id}")
def delete_radio_antenna(id: int, db: Session = Depends(get_db)):
    obj = crud.delete_radio_antenna(db, id)
    if not obj:
        raise HTTPException(status_code=404, detail="Not found")
    return {"ok": True}

# 5. Radio Units
@router.post("/radio-unit/", response_model=schemas.RadioUnit)
def create_radio_unit(data: schemas.RadioUnitCreate, db: Session = Depends(get_db)):
    return crud.create_radio_unit(db, data)

@router.get("/radio-unit/{site_session_id}", response_model=List[schemas.RadioUnit])
def get_radio_units(site_session_id: int, db: Session = Depends(get_db)):
    return crud.get_radio_units(db, site_session_id)

@router.put("/radio-unit/{id}", response_model=schemas.RadioUnit)
def update_radio_unit(id: int, data: dict, db: Session = Depends(get_db)):
    obj = crud.update_radio_unit(db, id, data)
    if not obj:
        raise HTTPException(status_code=404, detail="Not found")
    return obj

@router.delete("/radio-unit/{id}")
def delete_radio_unit(id: int, db: Session = Depends(get_db)):
    obj = crud.delete_radio_unit(db, id)
    if not obj:
        raise HTTPException(status_code=404, detail="Not found")
    return {"ok": True}

# 5.1. Radio Unit Port Connectivity
@router.post("/radio-unit-port-connectivity/", response_model=schemas.RadioUnitPortConnectivity)
def create_radio_unit_port_connectivity(data: schemas.RadioUnitPortConnectivityCreate, db: Session = Depends(get_db)):
    return crud.create_radio_unit_port_connectivity(db, data)

@router.get("/radio-unit-port-connectivity/{radio_unit_id}", response_model=List[schemas.RadioUnitPortConnectivity])
def get_radio_unit_port_connectivities(radio_unit_id: int, db: Session = Depends(get_db)):
    return crud.get_radio_unit_port_connectivities(db, radio_unit_id)

@router.put("/radio-unit-port-connectivity/{id}", response_model=schemas.RadioUnitPortConnectivity)
def update_radio_unit_port_connectivity(id: int, data: dict, db: Session = Depends(get_db)):
    obj = crud.update_radio_unit_port_connectivity(db, id, data)
    if not obj:
        raise HTTPException(status_code=404, detail="Not found")
    return obj

@router.delete("/radio-unit-port-connectivity/{id}")
def delete_radio_unit_port_connectivity(id: int, db: Session = Depends(get_db)):
    obj = crud.delete_radio_unit_port_connectivity(db, id)
    if not obj:
        raise HTTPException(status_code=404, detail="Not found")
    return {"ok": True}
