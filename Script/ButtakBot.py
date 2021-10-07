import discord
from discord.ext import commands

apps = commands.Bot(command_prefix='/')

@apps.event
async def on_ready():
    print('로그인중 해당 서버: ')
    print(apps.user.name)
    print('연결성공')
    await apps.change_presence(status=discord.status.online, activity=None)

    apps.run('ODkyNjIxODA4OTQyMDYzNjI2.YVPk1w.Abv4ZQoEm06SDhj0f9vH3eJD8Ts')