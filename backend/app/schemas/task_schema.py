from pydantic import BaseModel, ConfigDict

class Task(BaseModel):
    title: str
    description: str
    
    model_config = ConfigDict(str_min_length=2, str_max_length=30)
    