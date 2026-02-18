from pydantic import BaseModel
from typing import Optional


class UserCreate(BaseModel):
    username: str
    email: str
    password: str
    phone: Optional[str] = None


class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    phone: Optional[str] = None
    is_active: bool

    class Config:
        from_attributes = True

