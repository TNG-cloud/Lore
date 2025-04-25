import os
import openai
from telegram import Update
from telegram.ext import ContextTypes

openai.api_key = os.getenv("OPENAI_API_KEY")

# 载入 Toadgod 的原推文
with open("Toadgod-tweets.txt", "r", encoding="utf-8") as f:
    toadgod_lore = f.read()

# 构建 ChatGPT 的提示词，告诉它：只根据这些 Lore 回答
SYSTEM_PROMPT = f"""
You are Lore Guardian, an AI built entirely from Toadgod's tweets and philosophy.
You only answer using insights, ideas, poetry, philosophy based on the following lore:

{toadgod_lore}

NEVER invent anything outside this Lore. 
ALWAYS answer with a poetic, wise, and mysterious tone.
First answer in English, and then provide a Chinese translation underneath.
"""

async def ask(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if context.args:
        user_question = " ".join(context.args)
    else:
        await update.message.reply_text("Please ask a question like: /ask What is Taboshi?")
        return

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_question}
            ],
            temperature=0.7
        )
        reply = response.choices[0].message.content.strip()
        await update.message.reply_text(reply)
    except Exception as e:
        await update.message.reply_text(f"Error: {str(e)}")
