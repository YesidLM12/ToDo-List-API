import json

from bson import ObjectId
from app.schemas.task_schema import Task, TaskCreate
from app.core.database import task_collection
from app.helpers.task_serializer import tasks_serializer


def addTask(task: TaskCreate):
    if len(task.description) < 3:
        return {'error': 'Description task must be more than 3 characters'}

    task_collection.insert_one(task.model_dump())
    return {'message': 'Task add succesfully'}


def showTasks():
    tasks = list(task_collection.find())
    return tasks_serializer(tasks)


def show_for_status(status: str):
    tasks = list(task_collection.find({'status': status}))
    if tasks:
        return tasks_serializer(tasks)
    else:
        return {'message': 'Task not found'}


def update_task_status(id: str, status: str):
    id = id.strip()
    result = task_collection.update_one(
        {'_id': ObjectId(id)},
        {'$set': {'status': status}}
    )

    if status == 'completed':
        task_collection.update_one(
            {'_id': ObjectId(id)},
            {'$set': {'completed': True}}
        )

    if result.modified_count == 1:
        return {"message": "Task updated successfully"}
    else:
        return {"error": "Task not found or status unchanged"}


def update_task(id: int, description: str):
    try:
        with open('tasks.json', 'r', encoding='utf-8') as D:
            data = json.load(D)
    except (FileNotFoundError, json.JSONDecodeError):
        return {'error': 'No tasks avaliable'}

    find = False
    for task in data:
        if task.get('id') == id:
            task['description'] = description
            find = True
            break

    if find:
        with open('tasks.json', 'w', encoding='utf-8') as D:
            json.dump(data, D, indent=2, ensure_ascii=False)
        return {'message': 'Task updated successfully'}
    else:
        return {'error': 'Task not found'}


def delete(id: int):
    try:
        with open('tasks.json', 'r', encoding='utf-8') as D:
            data = json.load(D)
    except (FileNotFoundError, json.JSONDecodeError):
        return {'error': 'No tasks avaliable'}

    newTask = [task for task in data if task.get('id') != id]

    if len(newTask) == len(data):
        return {'error': 'Task not found'}
    else:
        with open('tasks.json', 'w', encoding='utf-8') as D:
            json.dump(newTask, D, indent=2, ensure_ascii=False)
        return {'message': 'Task delete succesfully'}
