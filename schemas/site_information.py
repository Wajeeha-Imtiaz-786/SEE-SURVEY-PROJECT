from pydantic import BaseModel
from typing import List, Optional

class SiteInformationBase(BaseModel):
    site_location_id: int
    site_area: Optional[str] = None
    site_ownership: Optional[str] = None
    shared_site: Optional[bool] = None
    telecom_operators: Optional[List[str]] = None
    ac_power_sharing: Optional[bool] = None
    dc_power_sharing: Optional[bool] = None
    site_topology: Optional[str] = None
    site_type: Optional[str] = None
    planned_scope: Optional[List[str]] = None
    existing_rack_location: Optional[List[str]] = None
    planned_rack_location: Optional[List[str]] = None
    existing_technology: Optional[List[str]] = None

class SiteInformationCreate(SiteInformationBase):
    pass

class SiteInformationUpdate(BaseModel):
    site_area: Optional[str] = None
    site_ownership: Optional[str] = None
    shared_site: Optional[bool] = None
    telecom_operators: Optional[List[str]] = None
    ac_power_sharing: Optional[bool] = None
    dc_power_sharing: Optional[bool] = None
    site_topology: Optional[str] = None
    site_type: Optional[str] = None
    planned_scope: Optional[List[str]] = None
    existing_rack_location: Optional[List[str]] = None
    planned_rack_location: Optional[List[str]] = None
    existing_technology: Optional[List[str]] = None

class SiteInformationOut(SiteInformationBase):
    id: int

    class Config:
        from_attributes = True

class SiteInformation(BaseModel):
    name: str
    description: str
