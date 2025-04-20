from pymongo import MongoClient
from config import MONGODB_URI

client = MongoClient(MONGODB_URI)
db = client['telegram_bot']
file_links = db['file_links']

def save_file(user_id, file_id, unique_id):
    file_links.insert_one({
        "user_id": user_id,
        "file_id": file_id,
        "unique_id": unique_id
    })

def get_file_by_unique_id(unique_id):
    return file_links.find_one({"unique_id": unique_id})
