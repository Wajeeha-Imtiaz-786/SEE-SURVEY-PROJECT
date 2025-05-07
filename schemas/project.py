from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class ProjectBase(BaseModel):
    project_name: str
    mu: Optional[str] = None
    ct: Optional[str] = None

class ProjectCreate(ProjectBase):
    user_id: int

class ProjectUpdate(ProjectBase):
    pass

class ProjectOut(ProjectBase):
    project_id: int
    user_id: int
    created_at: datetime

    class Config:
        from_attributes = True  # Updated from 'orm_mode'
        validate_by_name = True  # Updated from 'allow_population_by_field_name'
