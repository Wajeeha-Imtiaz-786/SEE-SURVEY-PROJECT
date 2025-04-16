from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class UserBase(BaseModel):
    username: str
    email: str
    first_name: str
    last_name: str
    phone: str
    title: str
    nid: str

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    first_name: str
    last_name: str
    password: str

    class Config:
        from_attributes = True

class UserUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    phone: Optional[str] = None
    title: Optional[str] = None
    nid: Optional[str] = None
    password: Optional[str] = None

class UserResponse(BaseModel):
    id: int = Field(alias="user_id")
    username: str
    email: str
    phone: Optional[str] = None
    title: Optional[str] = None
    nid: Optional[str] = None

    class Config:
        from_attributes = True
        allow_population_by_field_name = True
