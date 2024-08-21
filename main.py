from mybot import bot
from dotenv import load_dotenv
import os

load_dotenv()

bot_token = os.getenv("BOT_API")

bot.run(bot_token)