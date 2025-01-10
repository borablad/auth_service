from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db  # Добавьте эту строку
from app.services.auth_service import authenticate_user, create_user
from app.schemas.auth import UserCreate
from app.core.security import create_access_token


router = APIRouter()

@router.post("/login")
def login(username: str, password: str, db: Session = Depends(get_db)):
    user = authenticate_user(db, username, password)
    if not user:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    access_token = create_access_token({"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    new_user = create_user(db, user)
    return new_user

@router.get("/users", summary="Get all users", description="Endpoint accessible only by admins.")
def get_all_users(db: Session = Depends(get_db), current_user: User = Depends(is_admin)):
    users = db.query(User).all()
    return users