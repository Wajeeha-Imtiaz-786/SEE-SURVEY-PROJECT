from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from crud.role import create_role
from schemas.role import RoleCreate, RoleResponse

router = APIRouter(prefix="/roles", tags=["Roles"])

@router.post("/", response_model=RoleResponse)
def add_role(role: RoleCreate, db: Session = Depends(get_db)):
    return create_role(db, role)
