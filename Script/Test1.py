import youtube_dl
import discord, asyncio, os
from discord.ext import commands

#봇 토큰
Token = "ODkyNjIxODA4OTQyMDYzNjI2.YVPk1w.Abv4ZQoEm06SDhj0f9vH3eJD8Ts"

#봇 상태
game = discord.Game("명령어 !탁 도움 ")

#봇 명령어
bot = commands.Bot(command_prefix='!탁 ', status=discord.Status.online,activity=game)

#텍스트기능 예제
@bot.command(Func1str=[''])
async def Func1(func1):
    await func1.send(f'{func1.author.mention}')



#인사
@bot.command(aliases1=['인사','안녕','ㅎㅇ','하이','안녕하세요'])
async def 인사(ctx):
    await ctx.send(f'{ctx.author.mention} 하이')

#응애
@bot.command(aliases3=['응애'])
async def 응애(mamma):
    await mamma.send(f'{mamma.author.mention} 맘마줘')

#텍스트 기능 예제
@bot.command(Dice=['주사위'])
async def RollDice(rolldice, number:int):
    await rolldice.send(f'주사위를 굴려{random.randint(1,int(number))}이(가) 나왔습니다')
@RollDice.error
async def Dice_error(rolldice,error):
    await rolldice.send('오류!!!')


#도움말
@bot.command(aliases2=['명령어','도움','help','h'])
async def 도움(help1):
    embed_help = discord.Embed(title="명령어",description="부탁봇 명령어입니다", color=0x4432a8)
    embed_help.add_field(name="기본명령어" ,value="!인사 : 부탁이랑 인사합니다\n!명령어 : 부탁이 명령어\n!응애 : 응애!!",inline=False)
    embed_help.add_field(name="미니게임" ,value="!주사위 [숫자] : [ ]면주사위를 굴립니다",inline=False)
    embed_help.add_field(name="채널입장/퇴장",value="!입장 / !퇴장",inline=False)
    embed_help.add_field(name="음악재생" ,value="!play [URL] : 음악재생 \n!stop : 일시정지 \n!resume : 다시재생\n!reset : 음악멈춤",inline=False)
    await help1.send(embed=embed_help)





#@bot.command(aliases4=['입장'])
#async def 음악입장(MusicJoin):
#    await MusicJoin.author.voice.channel.connect()
#@bot.command(aliases5=['퇴장'])
#async def 음악퇴장(MusicOut):
#    await MusicOut.disconnect()

#실행
bot.run(Token)
