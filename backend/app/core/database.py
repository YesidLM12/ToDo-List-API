from motor.motor_asyncio import AsyncIOMotorClient
import os

MONGO_URL = os.getenv('MONGO_URL')

client = AsyncIOMotorClient(MONGO_URL)

database = client.my_database
collection = database.my_collection