import discord
import asyncio
from discord.ui import Button, View
from mybot import bot
from dotenv import load_dotenv
import os
from separation_image import position, check_image

@bot.command()
async def test(ctx, arg):
    await ctx.send(arg)

@bot.command()
async def 개인기록(ctx, pos):
    button = Button(label="업로드", style=discord.ButtonStyle.primary)
    
    async def button_callback(interaction):
        await interaction.response.send_message("사진을 업로드 해주세요. (최대 5장).", ephemeral=True)

        # Wait for the user to send an attachment
        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel and m.attachments

        try:
            message = await bot.wait_for('message', check=check, timeout=60)
            if message.attachments:
                
                for attachment in message.attachments[:5]:
                    print(attachment)
                    print(attachment.filename)
                    if attachment.filename.endswith(('png', 'jpg', 'jpeg')):
                        file_path = os.path.join('./user_image', attachment.filename)
                        await attachment.save(file_path)
                        filename = './user_image' + '/' +  attachment.filename
                        print(filename)
                        if (check_image(filename)):
                            await ctx.send(f'업로드 되었습니다! {attachment.filename}')
                    else:
                        await ctx.send(f'{attachment.filename} : 유효하지 않은 사진입니다!')

        except asyncio.TimeoutError:
            await ctx.send("업로드 시간이 초과되었습니다!")

    pos = position(pos)
    await ctx.send(pos)
    
    button.callback = button_callback

    # Create a view and add the button
    view = View()
    view.add_item(button)

    await ctx.send("Click the button to upload photos.", view=view)


bot.run(os.environ['DISCORD_TOKEN'])
