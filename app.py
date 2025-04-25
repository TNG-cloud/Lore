import os
import logging
from flask import Flask, request
from handlers.start import handle_start
from handlers.learn import handle_learn
from handlers.ask import handle_ask
from handlers.poem import handle_poem

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")

def send_message(chat_id, text):
    import requests
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": text,
        "parse_mode": "Markdown"
    }
    requests.post(url, json=payload)

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()
    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"].get("text", "")

        if text.startswith("/start"):
            send_message(chat_id, handle_start())
        elif text.startswith("/learn"):
            response = handle_learn(text)
            send_message(chat_id, response)
        elif text.startswith("/ask"):
            response = handle_ask(text)
            send_message(chat_id, response)
        elif text.startswith("/poem"):
            response = handle_poem(text)
            send_message(chat_id, response)
        else:
            send_message(chat_id, "🌀 Unknown command. Try /start, /learn, /ask or /poem.")
    return "ok"
