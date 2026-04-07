from flask import Flask, request
from pyrogram import Client
import os

app = Flask(__name__)

bot = Client(
    "bot",
    api_id=int(os.environ.get("API_ID")),
    api_hash=os.environ.get("API_HASH"),
    bot_token=os.environ.get("BOT_TOKEN")
)

@app.route("/")
def home():
    return "GameNova Running ✅"

@app.route("/score", methods=["POST"])
def score():
    data = request.json
    print("Score Data:", data)
    return {"ok": True}

if __name__ == "__main__":
    bot.start()
    app.run(host="0.0.0.0", port=10000)
