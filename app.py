import os
from telegram.ext import ApplicationBuilder, CommandHandler
from handlers.start import start
from handlers.learn import learn
from handlers.ask import ask
from handlers.poem import poem

TOKEN = os.getenv("TELEGRAM_API_KEY")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("learn", learn))
app.add_handler(CommandHandler("ask", ask))
app.add_handler(CommandHandler("poem", poem))

if __name__ == "__main__":
    app.run_polling()

