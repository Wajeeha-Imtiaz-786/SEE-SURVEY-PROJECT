from pydantic import BaseModel
from typing import Optional
from decimal import Decimal

class SiteLocationBase(BaseModel):
    site_id: str
    site_name: str
    region: str
    city: str
    longitude: Decimal
    latitude: Decimal
    site_elevation: Optional[Decimal] = None
    address: str

class SiteLocationCreate(SiteLocationBase):
    pass

class SiteLocationOut(SiteLocationBase):
    id: int

    class Config:
        from_attributes = True
