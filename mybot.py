import discord
from discord.ext import commands

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

bot = MyBot()