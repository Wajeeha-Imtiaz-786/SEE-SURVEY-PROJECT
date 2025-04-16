from pydantic import BaseModel
from typing import Optional

class ProjectBase(BaseModel):
    project_name: str
    description: Optional[str] = None

class ProjectCreate(ProjectBase):
    pass

class ProjectUpdate(BaseModel):
    project_name: Optional[str] = None
    description: Optional[str] = None

class ProjectResponse(ProjectBase):
    project_id: int

    class Config:
        from_attributes = True  # Updated for Pydantic v2
