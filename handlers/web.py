from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Welcome to Tobyworld Lore</h1><p>This is the Guardian Web Panel</p>"

@app.route("/learn")
def learn():
    with open("Toadgod-tweets.txt", "r", encoding="utf-8") as f:
        content = f.read()
    return f"<pre>{content[:3000]}</pre><p>...(truncated)</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
