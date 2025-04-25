# handlers/learn.py
import json
from telegram import Update
from telegram.ext import ContextTypes

with open("lore_data.json", "r", encoding="utf-8") as f:
    lore_data = json.load(f)

async def learn(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    for key, value in lore_data.items():
        await update.message.reply_text(f"{key}:\n{value}\n")
