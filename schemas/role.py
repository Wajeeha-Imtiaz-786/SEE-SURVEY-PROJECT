from pydantic import BaseModel
from enum import Enum as PyEnum
from pydantic import BaseModel

# Enum class for roles
class UserRoleEnum(str, PyEnum):
    Admin = "Admin"
    Manager = "Manager"
    Engineer = "Engineer"
    Viewer = "Viewer"

# Shared base schema
class RoleBase(BaseModel):
    project_id: int
    user_id: int
    user_role: UserRoleEnum

# For creating a role
class RoleCreate(RoleBase):
    pass

# For updating a role
class RoleUpdate(BaseModel):
    project_id: int | None = None
    user_id: int | None = None
    user_role: UserRoleEnum | None = None

# For returning a role (includes ID)

class RoleOut(BaseModel):
    role_id: int
    project_id: int
    user_id: int
    user_role: str

    class Config:
        from_attributes = True  # for SQLAlchemy ORM

    