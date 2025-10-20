from typing import Optional
from pydantic import BaseModel, EmailStr, Field

class User(BaseModel):
    name: str = Field(..., min_length=2, max_length=50)
    email: EmailStr
    password: str = Field(..., min_length=6)
    createdAt: Optional[str] = None


class UserLogin(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=6)
    