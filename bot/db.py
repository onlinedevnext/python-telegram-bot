from pymongo import MongoClient
import os
from datetime import datetime

client = MongoClient(os.getenv("MONGODB_URI"))
db = client["filebot"]
collection = db["files"]

def save_file(unique_id, file_id, file_name, user_id):
    data = {
        "unique_id": unique_id,
        "file_id": file_id,
        "file_name": file_name,
        "user_id": user_id,
        "created_at": datetime.utcnow()
    }
    collection.insert_one(data)

def get_file_by_unique_id(unique_id):
    return collection.find_one({"unique_id": unique_id})
