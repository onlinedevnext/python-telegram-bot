from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import PlainTextResponse
from db import get_file_by_unique_id
from bot_sender import send_file

app = FastAPI()

@app.get("/file/{unique_id}")
async def serve_file(unique_id: str, request: Request):
    data = get_file_by_unique_id(unique_id)
    if not data:
        raise HTTPException(status_code=404, detail="Invalid or expired link.")

    user_id = data["user_id"]
    file_id = data["file_id"]

    await send_file(file_id, user_id)
    return PlainTextResponse("✅ File sent to your Telegram DM. Check your messages!")
