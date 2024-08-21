from mybot import bot

class command():
    def __init__(self):
        pass
        
    @bot.command()
    async def test(ctx, arg):
        await ctx.on_message(arg)
    