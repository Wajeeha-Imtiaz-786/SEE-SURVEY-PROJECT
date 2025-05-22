from sqlalchemy.orm import Session
from models import new_radio as models
from schemas import new_radio as schemas

from pydantic import BaseModel
from typing import Optional


# ---------- New Radio Installation ----------
class NewRadioInstallationBase(BaseModel):
    site_session_id: int
    band: Optional[str]
    technology: Optional[str]
    configuration: Optional[str]
    radio_quantity: Optional[int]
    remarks: Optional[str]

class NewRadioInstallationCreate(NewRadioInstallationBase):
    pass

class NewRadioInstallationUpdate(NewRadioInstallationBase):
    pass

class NewRadioInstallation(NewRadioInstallationBase):
    id: int

    class Config:
        orm_mode = True

class NewRadioInstallationOut(BaseModel):
    id: int
    site_session_id: int
    band: Optional[str]
    technology: Optional[str]
    configuration: Optional[str]
    radio_quantity: Optional[int]
    remarks: Optional[str]

    class Config:
        orm_mode = True


# ---------- New Antenna ----------
class NewAntennaBase(BaseModel):
    site_session_id: int
    band: Optional[str]
    technology: Optional[str]
    antenna_type: Optional[str]
    antenna_quantity: Optional[int]
    remarks: Optional[str]

class NewAntennaCreate(NewAntennaBase):
    pass

class NewAntennaUpdate(NewAntennaBase):
    pass

class NewAntenna(NewAntennaBase):
    id: int

    class Config:
        orm_mode = True

class NewAntennaOut(BaseModel):
    id: int
    site_session_id: int
    band: Optional[str]
    technology: Optional[str]
    antenna_type: Optional[str]
    antenna_quantity: Optional[int]
    remarks: Optional[str]

    class Config:
        orm_mode = True


# ---------- New Radio Unit ----------
class NewRadioUnitBase(BaseModel):
    site_session_id: int
    radio_unit_type: Optional[str]
    band: Optional[str]
    quantity: Optional[int]
    remarks: Optional[str]

class NewRadioUnitCreate(NewRadioUnitBase):
    pass

class NewRadioUnitUpdate(NewRadioUnitBase):
    pass

class NewRadioUnit(NewRadioUnitBase):
    id: int

    class Config:
        orm_mode = True

class NewRadioUnitOut(BaseModel):
    id: int
    site_session_id: int
    radio_unit_type: Optional[str]
    band: Optional[str]
    quantity: Optional[int]
    remarks: Optional[str]

    class Config:
        orm_mode = True


# ---------- New FPFH ----------
class NewFPFHBase(BaseModel):
    site_session_id: int
    band: Optional[str]
    fpfh_type: Optional[str]
    quantity: Optional[int]
    remarks: Optional[str]

class NewFPFHCreate(NewFPFHBase):
    pass

class NewFPFHUpdate(NewFPFHBase):
    pass

class NewFPFH(NewFPFHBase):
    id: int

    class Config:
        orm_mode = True

class NewFPFHOut(BaseModel):
    id: int
    site_session_id: int
    band: Optional[str]
    fpfh_type: Optional[str]
    quantity: Optional[int]
    remarks: Optional[str]

    class Config:
        orm_mode = True


# ---------- GPS ----------
class GPSBase(BaseModel):
    site_session_id: int
    gps_type: Optional[str]
    gps_quantity: Optional[int]
    remarks: Optional[str]

class GPSCreate(GPSBase):
    pass

class GPSUpdate(GPSBase):
    pass

class GPS(GPSBase):
    id: int

    class Config:
        orm_mode = True

# ---------- GPS ----------
class GPSBase(BaseModel):
    site_session_id: int
    gps_type: Optional[str]
    quantity: Optional[int]
    remarks: Optional[str]

class GPSCreate(GPSBase):
    pass

class GPSUpdate(GPSBase):
    pass

class GPS(GPSBase):
    id: int

    class Config:
        orm_mode = True

class GPSOut(BaseModel):
    id: int
    site_session_id: int
    gps_type: Optional[str]
    gps_quantity: Optional[int]
    remarks: Optional[str]

    class Config:
        orm_mode = True