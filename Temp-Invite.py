from discord import colour
from discord.ext import commands
import discord
from discord_buttons_plugin import *
import asyncio

bot = commands.Bot(command_prefix="!")
buttons = ButtonsClient(bot)
sever_id = #본섭 아이디
channel_id = #링크가 보내질 채널 ID
token = ''

@buttons.click
async def buttonclick(ctx):
    link = await bot.get_channel(server_id).create_invite(max_uses=1,unique=True)
    a = await ctx.reply(f"{link}", flags=MessageFlags().EPHEMERAL)

@bot.command()
async def create(ctx):
        await buttons.send(
            embed=discord.Embed(title=f'보안 초대링크', description='버튼을 눌러 서버링크를 생성해주세요\nClick button to generate serverlink', color=0x5afb4a)
            channel = channel_id, 
            components = [
                ActionRow([
                    Button(
                        label="Generate serverlink", # 버튼이름
                        style=ButtonType().Success, # 버튼 색깔 설정
                        custom_id="buttonclick" # 고유 id (불러올때 쓰임)
                    )
                ])
            ]
        )

bot.run(token)
