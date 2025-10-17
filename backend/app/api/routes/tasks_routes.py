from fastapi import APIRouter
from schemas.task_schema import Task,TaskCreate

router = APIRouter()

fake_db = []

@router.get('/',response_model=list[Task])
def get_tasks():
    return fake_db
