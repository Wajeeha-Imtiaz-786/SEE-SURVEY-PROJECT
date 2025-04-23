from typing import Optional
from pydantic import BaseModel
from schemas.site_information import SiteInformation
from schemas.site_location import SiteLocation
from schemas.site_access import SiteAccess

class SiteSessionBase(BaseModel):
    pass

class SiteSessionCreate(SiteSessionBase):
    pass

class SiteSession(SiteSessionBase):
    id: int
    site_location: Optional[SiteLocation]
    site_information: Optional[SiteInformation]
    site_access: Optional[SiteAccess]

    class Config:
        orm_mode = True
