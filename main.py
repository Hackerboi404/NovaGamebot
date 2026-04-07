from flask import Flask
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import os

app = Flask(__name__)

bot = Client(
    "bot",
    api_id=int(os.environ.get("API_ID")),
    api_hash=os.environ.get("API_HASH"),
    bot_token=os.environ.get("BOT_TOKEN")
)

@bot.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text(
        "🎮 Play NovaGame Lumberjack!",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("Play 🎮", callback_game="NovaGame")]
        ])
    )

@app.route("/")
def home():
    return "Game running!"

if __name__ == "__main__":
    bot.start()
    app.run(host="0.0.0.0", port=10000)
