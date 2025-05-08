from pydantic import BaseModel
from typing import Optional

class SiteAccessBase(BaseModel):
    #site_session_id: int  # NEW
    site_location_id: int # Foreign key to SiteLocation
    access_permission: Optional[bool] = None
    crane_access_time: Optional[dict] = None
    site_access_contact: Optional[str] = None
    site_access_phone: Optional[str] = None
    available_access_time: Optional[dict] = None
    road_access: str
    gated_fence: str
    keys_required: str
    key_types: Optional[dict] = None
    key_contact_person: Optional[str] = None
    key_contact_phone: Optional[str] = None
    material_access: Optional[dict] = None
    stair_lift_height: Optional[float] = None
    stair_lift_width: Optional[float] = None
    stair_lift_depth: Optional[float] = None

class SiteAccessCreate(SiteAccessBase):
    pass

class SiteAccess(SiteAccessBase):
    id: int

    class Config:
        from_attributes = True
