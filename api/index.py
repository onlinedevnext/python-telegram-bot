from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import PlainTextResponse
from bot.db import get_file_by_unique_id
from bot.bot_sender import send_file

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Telegram Bot is up 🔗 Send a file to get your custom URL."}

@app.get("/file/{unique_id}")
async def serve_file(unique_id: str, request: Request):
    data = get_file_by_unique_id(unique_id)
    if not data:
        raise HTTPException(status_code=404, detail="File not found.")

    await send_file(data["file_id"], data["user_id"])
    return PlainTextResponse("✅ File sent to your Telegram DM.")
