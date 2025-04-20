from pyrogram import Client
import os

bot = Client("sender", api_id=int(os.getenv("API_ID")), api_hash=os.getenv("API_HASH"), bot_token=os.getenv("TELEGRAM_BOT_TOKEN"))

async def send_file(file_id: str, user_id: int):
    async with bot:
        await bot.send_document(chat_id=user_id, document=file_id)
