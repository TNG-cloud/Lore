# handlers/poem.py
from telegram import Update
from telegram.ext import ContextTypes

async def poem(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    with open("templates/poem.txt", "r", encoding="utf-8") as file:
        poem_content = file.read()
    await update.message.reply_text(poem_content)
