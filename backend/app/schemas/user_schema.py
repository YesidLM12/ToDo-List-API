from typing import Optional
from pydantic import BaseModel, ConfigDict

class User(BaseModel):
    name: str
    email:str
    password: str
    
    model_config = ConfigDict(str_max_length=10)

class UserResponse(User):
    id: Optional[str] = None
    