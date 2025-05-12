from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from crud import project as crud_project
from schemas import project as schema_project
from database import get_db
from typing import List

router = APIRouter(
    tags=["Projects"]
)

@router.post("/", response_model=schema_project.ProjectOut)
def create_project(project: schema_project.ProjectCreate, db: Session = Depends(get_db)):
    return crud_project.create_project(db, project)

@router.get("/", response_model=List[schema_project.ProjectOut])
def get_projects(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud_project.get_projects(db, skip, limit)

@router.get("/{project_id}", response_model=schema_project.ProjectOut)
def get_project(project_id: int, db: Session = Depends(get_db)):
    db_project = crud_project.get_project(db, project_id)
    if db_project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    return db_project

@router.put("/{project_id}", response_model=schema_project.ProjectOut)
def update_project(project_id: int, updated_project: schema_project.ProjectUpdate, db: Session = Depends(get_db)):
    project = crud_project.update_project(db, project_id, updated_project)
    if project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    return project

@router.delete("/{project_id}", response_model=schema_project.ProjectOut)
def delete_project(project_id: int, db: Session = Depends(get_db)):
    project = crud_project.delete_project(db, project_id)
    if project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    return project
