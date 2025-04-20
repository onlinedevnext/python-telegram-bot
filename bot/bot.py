from pyrogram import Client, filters
from pyrogram.types import Message
from bot.db import save_file
import uuid
import os

bot = Client("my_bot", api_id=int(os.getenv("API_ID")), api_hash=os.getenv("API_HASH"), bot_token=os.getenv("TELEGRAM_BOT_TOKEN"))
BASE_URL = os.getenv("BASE_URL")

@bot.on_message(filters.document | filters.video | filters.audio)
async def handle_file(client: Client, message: Message):
    file_id = message.document.file_id if message.document else (
              message.video.file_id if message.video else message.audio.file_id)
    file_name = message.document.file_name if message.document else (
                message.video.file_name if message.video else message.audio.file_name)

    user_id = message.from_user.id
    unique_id = str(uuid.uuid4())[:8]

    # Save to MongoDB
    save_file(unique_id, file_id, file_name, user_id)

    # Create link
    link = f"{BASE_URL}/api/file/{unique_id}"
    await message.reply_text(f"✅ Your file is saved!\nShare this link:\n{link}")
