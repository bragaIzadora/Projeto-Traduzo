from pymongo import MongoClient
import os

mongo_uri = os.getenv("MONGO_URI", "mongodb://localhost:27017")
db_name = os.getenv("DB_NAME", "test_db_traduzo")

client = MongoClient(mongo_uri)
db = client[db_name]