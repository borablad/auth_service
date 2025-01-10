from sqlalchemy.orm import Session
from app.db.user_crud import get_user_by_username, create_user
from app.core.security import verify_password

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
