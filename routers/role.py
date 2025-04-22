from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from database import get_db
from models.role import Role
from schemas.role import RoleCreate, RoleUpdate, RoleOut
from crud import role as role_crud  # alias to avoid name conflict

router = APIRouter(
    prefix="/roles",
    tags=["Roles"]
)

# Create a new role
@router.post("/", response_model=RoleOut, status_code=status.HTTP_201_CREATED)
def create_role(role_data: RoleCreate, db: Session = Depends(get_db)):
    return role_crud.create_role(db, role_data)

# Get a role by ID
@router.get("/{role_id}", response_model=RoleOut)
def get_role(role_id: int, db: Session = Depends(get_db)):
    role = role_crud.get_role_by_id(db, role_id)
    if not role:
        raise HTTPException(status_code=404, detail="Role not found")
    return role

# Get all roles for a specific project
@router.get("/project/{project_id}", response_model=List[RoleOut])
def get_roles_by_project(project_id: int, db: Session = Depends(get_db)):
    return role_crud.get_roles_by_project(db, project_id)

# Update a role
@router.put("/{role_id}", response_model=RoleOut)
def update_role(role_id: int, role_data: RoleUpdate, db: Session = Depends(get_db)):
    role = role_crud.update_role(db, role_id, role_data)
    if not role:
        raise HTTPException(status_code=404, detail="Role not found")
    return role

# Delete a role
@router.delete("/{role_id}", response_model=RoleOut)
def delete_role(role_id: int, db: Session = Depends(get_db)):
    role = role_crud.delete_role(db, role_id)
    if not role:
        raise HTTPException(status_code=404, detail="Role not found")
    return role
