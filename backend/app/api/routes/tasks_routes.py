
from fastapi import APIRouter
from app.Controller.task_controller import addTask, delete, show_for_status, showTasks, update_task, update_task_status
from app.schemas.task_schema import Task, TaskCreate

router = APIRouter()


@router.get('/', response_model=list[Task])
def get_tasks():
    return showTasks()


@router.patch('/{id}')
def uptdate_task(id: int, description: str):
    return update_task(id, description)


@router.get('/for-status', response_model=list[Task])
def get_task_for_status(status: str):
    return show_for_status(status)


@router.patch('/status/{id}')
def set_status(id: int, status: str):
    return update_task_status(id, status)


@router.post('/', response_model=Task)
def create_task(task: TaskCreate):
    return addTask(task)


@router.delete('/{id}')
def delete_task(id: int):
    return delete(id)
