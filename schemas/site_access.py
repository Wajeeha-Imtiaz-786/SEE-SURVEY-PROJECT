from pydantic import BaseModel
from typing import List, Optional


class SiteAccessBase(BaseModel):
    site_location_id: int
    access_permission: Optional[bool] = None
    crane_access_time: Optional[List[str]] = None
    site_access_contact: Optional[str] = None
    site_access_phone: Optional[str] = None
    available_access_time: Optional[List[str]] = None
    road_access: Optional[str] = None
    gated_fence: Optional[str] = None
    keys_required: Optional[str] = None
    key_types: Optional[List[str]] = None
    key_contact_person: Optional[str] = None
    key_contact_phone: Optional[str] = None
    material_access: Optional[List[str]] = None
    stair_lift_height: Optional[float] = None
    stair_lift_width: Optional[float] = None
    stair_lift_depth: Optional[float] = None


class SiteAccessCreate(SiteAccessBase):
    pass


class SiteAccess(SiteAccessBase):
    id: int

    class Config:
        from_attributes = True
