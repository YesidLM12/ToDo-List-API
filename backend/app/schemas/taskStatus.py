from pydantic import BaseModel
from typing import Literal


class TaskStatusUpdate(BaseModel):
    status: Literal['pending', 'in-progress', 'completed']
