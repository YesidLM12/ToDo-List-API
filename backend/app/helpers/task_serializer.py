
def task_serializer(task) -> dict:
    return {
        id: str(task['_id']),
        'description': task['description'],
        'status': task['status'],
        'completed': task['completed']
    }
