from typing import Optional
from pydantic import BaseModel

class SiteSessionBase(BaseModel):
    session_code: str
    description: Optional[str] = None

class SiteSessionCreate(SiteSessionBase):
    pass

class SiteSession(SiteSessionBase):
    id: int

    class Config:
        from_attributes = True
