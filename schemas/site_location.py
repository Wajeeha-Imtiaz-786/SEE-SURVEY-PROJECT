from pydantic import BaseModel
from typing import Optional
from decimal import Decimal

class SiteLocationBase(BaseModel):
    site_id: str
    site_name: str
    region: str
    city: str
    operator: str
    longitude: Decimal
    latitude: Decimal
    site_elevation: Optional[Decimal] = None
    address: str

class SiteLocationCreate(SiteLocationBase):
    pass

class SiteLocationUpdate(BaseModel):
    site_id: Optional[str] = None
    site_name: Optional[str] = None
    region: Optional[str] = None
    city: Optional[str] = None
    operator: Optional[str] = None
    longitude: Optional[Decimal] = None
    latitude: Optional[Decimal] = None
    site_elevation: Optional[Decimal] = None
    address: Optional[str] = None

class SiteLocationOut(SiteLocationBase):
    id: int

    class Config:
        from_attributes = True

class SiteLocation(BaseModel):
    latitude: float
    longitude: float
    address: str
    operator: Optional[str] = None  # Added operator field
