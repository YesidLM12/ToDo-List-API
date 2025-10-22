import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr, Field

class User(BaseModel):
    username: str = Field(..., min_length=2, max_length=50)
    email: EmailStr
    password: str = Field(..., min_length=6, max_length=72)


class UserLogin(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=6)
    