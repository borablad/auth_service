from sqlalchemy.orm import Session
from app.db.user_crud import get_user_by_username, create_user
from app.core.security import verify_password
from fastapi import Depends, HTTPException
from app.models.user import User, UserRole

def authenticate_user(db: Session, username: str, password: str):
    user = get_user_by_username(db, username)
    if not user:
        return None
    if not verify_password(password, user.hashed_password):
        return None
    return user

def register_user(db: Session, user_data):
    if get_user_by_username(db, user_data.username):
        raise ValueError("User already exists")
    return create_user(db, user_data)

def get_current_user(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    try:
        payload = decode_access_token(token)
        username = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid authentication")
        user = get_user_by_username(db, username)
        if not user:
            raise HTTPException(status_code=401, detail="Invalid authentication")
        return user
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid authentication")

def is_admin(current_user: User = Depends(get_current_user)):
    if current_user.role != UserRole.ADMIN:
        raise HTTPException(status_code=403, detail="Not enough permissions")