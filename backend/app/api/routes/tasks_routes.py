
from bson import ObjectId
from fastapi import APIRouter, Depends
from app.Controller.task_controller import addTask, delete, show_for_status, showTasks, update_task, update_task_status
from app.schemas.task_schema import StatusUpdate, Task, TaskCreate
from app.utils.auth import verify_jwt_token

router = APIRouter()


@router.get('/')
def get_tasks(current_user: dict = Depends(verify_jwt_token)):
    return showTasks()


@router.patch('/{id}')
def uptdate_task(id: str, description: str, current_user: dict = Depends(verify_jwt_token)):
    return update_task(id, description)


@router.get('/for-status')
def get_task_for_status(status: str, current_user: dict = Depends(verify_jwt_token)):
    return show_for_status(status)


@router.patch('/status/{id}')
def set_status(id: str, update: StatusUpdate, current_user: dict = Depends(verify_jwt_token)):
    return update_task_status(id, update.status)


@router.post('/')
def create_task(task: TaskCreate, current_user: dict = Depends(verify_jwt_token)):
    return addTask(task)


@router.delete('/{id}')
def delete_task(id: str, current_user: dict = Depends(verify_jwt_token)):
    return delete(id)
