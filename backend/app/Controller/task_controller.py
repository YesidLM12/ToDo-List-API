import json
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


def show_for_status(status: str):
    try:
        with open('tasks.json', 'r', encoding='utf-8') as D:
            data = json.load(D)
    except (FileNotFoundError, json.JSONDecodeError):
        return {'error': 'No tasks avaliable'}

    task_status = [task for task in data if task.get(
        'status') == status]

    if len(task_status) > 0:
        return task_status
    else:
        return {'error': 'No tasks avaliable'}


def update_task_status(id: int, status: str):
    try:
        with open('tasks.json', 'r', encoding='utf-8') as D:
            data = json.load(D)
    except (FileNotFoundError, json.JSONDecodeError):
        return {'error': 'No tasks avaliable'}

    found = False
    for task in data:
        if task.get('id') == id:
            task['status'] = status
            found = True
            break

    if found:
        with open('tasks.json', 'w', encoding='utf-8') as D:
            json.dump(data, D, indent=2, ensure_ascii=False)
        return {'message': 'Status update succesfully'}
    else:
        return {'error': 'Task not found'}


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
