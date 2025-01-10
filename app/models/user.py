from sqlalchemy import Column, Enum as SQLAlchemyEnum
from enum import Enum

class UserRole(str, Enum):
    USER = "USER"
    ADMIN = "ADMIN"

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    role = Column(SQLAlchemyEnum(UserRole), default=UserRole.USER)
