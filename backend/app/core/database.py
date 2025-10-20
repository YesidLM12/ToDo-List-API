from pymongo import MongoClient

from app.core.config import settings

client = MongoClient(settings.MONGO_URI)
db = client['todoapp']
task_collection = db['tasks']
user_collection = db['users']
