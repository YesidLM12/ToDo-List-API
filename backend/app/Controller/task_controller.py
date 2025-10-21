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


def update_task(id: str, description: str):
    id = id.strip()
    result = task_collection.update_one(
        {'_id': ObjectId(id)},
        {'$set': {'description': description}}
    )

    if result.modified_count == 1:
        return {"message": "Task updated successfully"}
    else:
        return {"error": "Task not found or status unchanged"}


def delete(id: str):
    task_collection.delete_one({'_id': id})
    return {'message': 'Task delete succesfully'}
