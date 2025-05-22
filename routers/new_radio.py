from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
import crud.new_radio as crud
import schemas.new_radio as schemas

router = APIRouter(prefix="/new-radio", tags=["New Radio"])


# -------- New Radio Installation --------
@router.post("/installation/", response_model=schemas.NewRadioInstallationOut)
def create_installation(data: schemas.NewRadioInstallationCreate, db: Session = Depends(get_db)):
    return crud.create_new_radio_installation(db, data)

@router.get("/installation/{installation_id}", response_model=schemas.NewRadioInstallationOut)
def get_installation(installation_id: int, db: Session = Depends(get_db)):
    return crud.get_new_radio_installation(db, installation_id)

@router.put("/installation/{installation_id}", response_model=schemas.NewRadioInstallationOut)
def update_installation(installation_id: int, data: schemas.NewRadioInstallationUpdate, db: Session = Depends(get_db)):
    return crud.update_new_radio_installation(db, installation_id, data)

@router.delete("/installation/{installation_id}")
def delete_installation(installation_id: int, db: Session = Depends(get_db)):
    return crud.delete_new_radio_installation(db, installation_id)


# -------- New Antenna --------
@router.post("/antenna/", response_model=schemas.NewAntennaOut)
def create_antenna(data: schemas.NewAntennaCreate, db: Session = Depends(get_db)):
    return crud.create_new_antenna(db, data)

@router.get("/antenna/{antenna_id}", response_model=schemas.NewAntennaOut)
def get_antenna(antenna_id: int, db: Session = Depends(get_db)):
    return crud.get_new_antenna(db, antenna_id)

@router.put("/antenna/{antenna_id}", response_model=schemas.NewAntennaOut)
def update_antenna(antenna_id: int, data: schemas.NewAntennaUpdate, db: Session = Depends(get_db)):
    return crud.update_new_antenna(db, antenna_id, data)

@router.delete("/antenna/{antenna_id}")
def delete_antenna(antenna_id: int, db: Session = Depends(get_db)):
    return crud.delete_new_antenna(db, antenna_id)


# -------- New Radio Unit --------
@router.post("/radio-unit/", response_model=schemas.NewRadioUnitOut)
def create_radio_unit(data: schemas.NewRadioUnitCreate, db: Session = Depends(get_db)):
    return crud.create_new_radio_unit(db, data)

@router.get("/radio-unit/{unit_id}", response_model=schemas.NewRadioUnitOut)
def get_radio_unit(unit_id: int, db: Session = Depends(get_db)):
    return crud.get_new_radio_unit(db, unit_id)

@router.put("/radio-unit/{unit_id}", response_model=schemas.NewRadioUnitOut)
def update_radio_unit(unit_id: int, data: schemas.NewRadioUnitUpdate, db: Session = Depends(get_db)):
    return crud.update_new_radio_unit(db, unit_id, data)

@router.delete("/radio-unit/{unit_id}")
def delete_radio_unit(unit_id: int, db: Session = Depends(get_db)):
    return crud.delete_new_radio_unit(db, unit_id)


# -------- New FPFH --------
@router.post("/fpfh/", response_model=schemas.NewFPFHOut)
def create_fpfh(data: schemas.NewFPFHCreate, db: Session = Depends(get_db)):
    return crud.create_new_fpfh(db, data)

@router.get("/fpfh/{fpfh_id}", response_model=schemas.NewFPFHOut)
def get_fpfh(fpfh_id: int, db: Session = Depends(get_db)):
    return crud.get_new_fpfh(db, fpfh_id)

@router.put("/fpfh/{fpfh_id}", response_model=schemas.NewFPFHOut)
def update_fpfh(fpfh_id: int, data: schemas.NewFPFHUpdate, db: Session = Depends(get_db)):
    return crud.update_new_fpfh(db, fpfh_id, data)

@router.delete("/fpfh/{fpfh_id}")
def delete_fpfh(fpfh_id: int, db: Session = Depends(get_db)):
    return crud.delete_new_fpfh(db, fpfh_id)


# -------- GPS --------
@router.post("/gps/", response_model=schemas.GPSOut)
def create_gps(data: schemas.GPSCreate, db: Session = Depends(get_db)):
    return crud.create_gps(db, data)

@router.get("/gps/{gps_id}", response_model=schemas.GPSOut)
def get_gps(gps_id: int, db: Session = Depends(get_db)):
    return crud.get_gps(db, gps_id)

@router.put("/gps/{gps_id}", response_model=schemas.GPSOut)
def update_gps(gps_id: int, data: schemas.GPSUpdate, db: Session = Depends(get_db)):
    return crud.update_gps(db, gps_id, data)

@router.delete("/gps/{gps_id}")
def delete_gps(gps_id: int, db: Session = Depends(get_db)):
    return crud.delete_gps(db, gps_id)
