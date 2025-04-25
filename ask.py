# handlers/ask.py
from telegram import Update
from telegram.ext import ContextTypes

async def ask(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "This feature will let you ask questions soon. Stay tuned!"
    )
