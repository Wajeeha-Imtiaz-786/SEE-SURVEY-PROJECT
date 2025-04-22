from sqlalchemy.orm import Session
from models import project as project_model
from schemas import project as project_schema

def create_project(db: Session, project: project_schema.ProjectCreate):
    db_project = project_model.Project(
        user_id=project.user_id,
        project_name=project.project_name,
        mu=project.mu,
        ct=project.ct
    )
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project

def get_project(db: Session, project_id: int):
    return db.query(project_model.Project).filter(project_model.Project.project_id == project_id).first()

def get_projects(db: Session, skip: int = 0, limit: int = 100):
    return db.query(project_model.Project).offset(skip).limit(limit).all()

def update_project(db: Session, project_id: int, updated_data: project_schema.ProjectUpdate):
    project = get_project(db, project_id)
    if project:
        for field, value in updated_data.dict(exclude_unset=True).items():
            setattr(project, field, value)
        db.commit()
        db.refresh(project)
    return project

def delete_project(db: Session, project_id: int):
    project = get_project(db, project_id)
    if project:
        db.delete(project)
        db.commit()
    return project
