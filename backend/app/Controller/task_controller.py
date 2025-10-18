
from app.schemas.task_schema import Task, TaskCreate

fake_db = []


def addTask(task: TaskCreate):
    if len(task.description) < 3:
        return {'error': 'Description task must be more tha 3 characters'}

    new_task = Task(id=len(fake_db) + 1, **task.model_dump())
    fake_db.append(new_task)
    return new_task

def showTasks():
    return fake_db

def in_progress():
    for t in fake_db:
        if t.get('status') == 'in-progress':
            return t

def done():
    for t in fake_db:
        if t.get('status') == 'done':
            return t
        