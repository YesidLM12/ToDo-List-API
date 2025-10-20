from pymongo import MongoClient

from backend.app.core.config import Settings

client = MongoClient(Settings.MONGO_URI)
db = client['ToDoApp']
task_collection = db['tasks']
user_collection = db['users']
