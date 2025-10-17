from pydantic import BaseModel, ConfigDict

class User(BaseModel):
    name: str
    email:str
    password: str
    
    model_config = ConfigDict(str_max_length=10)
    