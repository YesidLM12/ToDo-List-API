from fastapi import APIRouter
from app.Controller.task_controller import addTask, in_progress, showTasks, done
from app.schemas.task_schema import Task, TaskCreate

router = APIRouter()

fake_db = []


@router.get('/', response_model=list[Task])
def get_tasks():
    return showTasks()


@router.get('/in-progress', response_model=list[Task])
def get_task_in_progress():
    return in_progress()


@router.get('/pending', response_model=list[Task])
def get_task_done():
    return done()


@router.post('/', response_model=Task)
def create_task(task: TaskCreate):
    return addTask(task)
