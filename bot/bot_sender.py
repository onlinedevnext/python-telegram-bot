import httpx
from config import BOT_TOKEN

API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendDocument"

async def send_file(file_id: str, user_id: int):
    async with httpx.AsyncClient() as client:
        await client.post(API_URL, data={
            "chat_id": user_id,
            "document": file_id
        })
