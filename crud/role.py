from sqlalchemy.orm import Session
from models.role import Role
from schemas.role import RoleCreate, RoleUpdate

def create_role(db: Session, role_data: RoleCreate):
    db_role = Role(**role_data.model_dump())  # Pydantic v2
    db.add(db_role)
    db.commit()
    db.refresh(db_role)
    return db_role

def get_role_by_id(db: Session, role_id: int):
    return db.query(Role).filter(Role.role_id == role_id).first()

def get_roles_by_project(db: Session, project_id: int):
    return db.query(Role).filter(Role.project_id == project_id).all()

def update_role(db: Session, role_id: int, role_update: RoleUpdate):  # <-- Add type hint here
    db_role = db.query(Role).filter(Role.role_id == role_id).first()
    if db_role:
        for key, value in role_update.model_dump(exclude_unset=True).items():  # <-- model_dump()
            setattr(db_role, key, value)
        db.commit()
        db.refresh(db_role)
    return db_role

def delete_role(db: Session, role_id: int):
    db_role = db.query(Role).filter(Role.role_id == role_id).first()
    if db_role:
        db.delete(db_role)
        db.commit()
    return db_role
