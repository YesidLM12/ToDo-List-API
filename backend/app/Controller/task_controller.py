
import json
from fastapi import FastAPI
from app.schemas.task_schema import Task, TaskCreate


def addTask(task: TaskCreate):
    if len(task.description) < 3:
        return {'error': 'Description task must be more tha 3 characters'}
    try:
        try:
            with open('tasks.json', 'r', encoding='utf-8') as D:
                data = json.load(D)
        except (FileNotFoundError, json.JSONDecodeError):
            data = []

        new_task = Task(id=len(data) + 1, **task.model_dump())
        data.append(new_task.model_dump())

        with open('tasks.json', 'w', encoding='utf-8') as D:
            json.dump(data, D, ensure_ascii=False, indent=2)
    except Exception as e:
        print(e)

    return new_task


def showTasks():
    try:
        with open('tasks.json', 'r', encoding='utf-8') as D:
            data = json.load(D)
    except (FileNotFoundError, json.JSONDecodeError):
        data = []

    if data:
        return data


def in_progress():
    try:
        with open('tasks.json', 'r', encoding='utf-8') as D:
            data = json.load(D)
    except (FileNotFoundError, json.JSONDecodeError):
        data = []

    task_in_progress = [task for task in data if task.get(
        'status') == 'in-progress']

    return task_in_progress


def done():
    try:
        with open('tasks.json', 'r', encoding='utf-8') as D:
            data = json.load(D)
    except (FileNotFoundError, json.JSONDecodeError):
        data = []

    task_done = [task for task in data if task.get('status') == 'done']
    return task_done


def pendind():
    try:
        with open('tasks.json', 'r', encoding='utf-8') as D:
            data = json.load(D)
    except (FileNotFoundError, json.JSONDecodeError):
        data = []

    task_pending = [task for task in data if task.get('status') == 'pending']
    return task_pending

## todo implemetar la funciones para marcar los status
