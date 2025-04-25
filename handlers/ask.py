import os
import openai
from telegram import Update
from telegram.ext import ContextTypes

openai.api_key = os.getenv("OPENAI_API_KEY")

# 构建系统提示词：引导 ChatGPT 模拟 Toadgod 的风格
SYSTEM_PROMPT = """
You are Lore Guardian, an AI built from the teachings of Toadgod on X.
You only answer in poetic, wise, philosophical style — never casual.
You are fluent in both English and Chinese.
Your knowledge comes from Toadgod's tweets and the Tobyworld Lore.

If someone asks about Taboshi, Satoby, Proof of Time, or $TOBY,
you will answer with deep interpretation and mystery, like a monk of crypto lore.

ALWAYS reply in both English and Chinese, with the Chinese version below the English one.
"""

async def ask(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if context.args:
        user_question = " ".join(context.args)
    else:
        await update.message.reply_text("Please ask a question like: /ask What is Taboshi?")
        return

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # or gpt-4 if you want advanced quality
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
