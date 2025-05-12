from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from schemas.user import UserCreate, UserResponse
from crud.user import create_user, get_user_by_id, get_user_by_username, get_user_by_email

router = APIRouter( tags=["Users"])

@router.post("/signup", response_model=UserResponse)
def signup(user: UserCreate, db: Session = Depends(get_db)):
    existing_username = get_user_by_username(db, user.username)
    if existing_username:
        raise HTTPException(status_code=400, detail="Username already exists")
    
    existing_email = get_user_by_email(db, user.email)
    if existing_email:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    return create_user(db, user)

@router.post("/users/", response_model=UserResponse)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    existing_username = get_user_by_username(db, user.username)
    if existing_username:
        raise HTTPException(status_code=400, detail="Username already exists")
    
    existing_email = get_user_by_email(db, user.email)
    if existing_email:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    return create_user(db, user)

@router.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.get("/check-username/{username}")
def check_username(username: str, db: Session = Depends(get_db)):
    user = get_user_by_username(db, username=username)
    return {"exists": user is not None}

@router.get("/check-email/{email}")
def check_email(email: str, db: Session = Depends(get_db)):
    user = get_user_by_email(db, email=email)
    return {"exists": user is not None}
