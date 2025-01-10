from pydantic import BaseModel
from enum import Enum

class UserRole(str, Enum):
    USER = "USER"
    ADMIN = "ADMIN"


class UserCreate(BaseModel):
    username: str
    password: str

class UserResponse(BaseModel):
    id: int
    username: str
    is_active: bool
    role: UserRole

    class Config:
        orm_mode = True
