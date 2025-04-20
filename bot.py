import uuid
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from config import BOT_TOKEN, BASE_URL
from db import save_file

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Send /getfile <file_id> to generate a private link!")

async def get_file(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) == 0:
        await update.message.reply_text("Usage: /getfile <file_id>")
        return

    file_id = context.args[0]
    user_id = update.effective_user.id
    unique_id = str(uuid.uuid4())

    save_file(user_id=user_id, file_id=file_id, unique_id=unique_id)
    url = f"{BASE_URL}/file/{unique_id}"
    await update.message.reply_text(f"Your private download link:\n{url}")

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("getfile", get_file))

if __name__ == "__main__":
    app.run_polling()
