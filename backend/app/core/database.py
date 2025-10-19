from pymongo import MongoClient

MONGO_URL = 'mongodb://localhost:27017/'


client= MongoClient(MONGO_URL)
db = client['ToDoApp']
task_collection = db['tasks']
user_collection = db['users']