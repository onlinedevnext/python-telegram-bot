import os
from dotenv import load_dotenv

# Load from .env in dev / local
load_dotenv()

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
MONGO_URI = os.getenv("MONGODB_URI")
BASE_URL = os.getenv("BASE_URL")
