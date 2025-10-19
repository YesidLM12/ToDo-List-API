from pydantic import BaseModel, ConfigDict
from typing import Optional

class TaskBase(BaseModel):
    description: str
    status: str = 'pending'
    completed: bool = False
    
    model_config = ConfigDict(str_min_length=2, str_max_length=30)

class TaskCreate(TaskBase):
    pass

class Task(TaskBase):
    id: Optional[str] = None
    