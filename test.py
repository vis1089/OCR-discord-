import discord
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv
import os

intents = discord.Intents.default()
intents.message_content = True

class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix="%",
            intents=intents.all(),
            sync_command=True,
            application_id=1274726455628009573
        )
        
    async def setup_hook(self):
        await bot.tree.sync()

    async def on_ready(self):
        print("ready!")
        
        activity = discord.Game("상태 메세지")
        await self.change_presence(status=discord.Status.online, activity=activity)

    @app_commands.command(name="ping")
    async def ping(self, ctx: commands.Context) -> None:
        await ctx.send("pong!")

load_dotenv()

bot_token = os.getenv("BOT_API")
print(bot_token)

bot = MyBot()
bot.run(bot_token)