import discord
from discord.ext import commands
from discord.ext.commands import Bot
from discord.utils import get
import youtube_dl
from discord.ext import commands
from discord.utils import get
from discord import FFmpegPCMAudio
from youtube_dl import YoutubeDL
import asyncio
import time as t
import random as r
import urllib.request
import re
import json

import os

#discord.opus.load_opus()

bot: Bot = commands.Bot(command_prefix='!')


loljs = {}




def is_connected(ctx):
    voice_client = get(ctx.bot.voice_clients, guild=ctx.guild)
    return voice_client and voice_client.is_connected()


@bot.command(pass_context=True, brief="skips a song")
async def skip(ctx):
    voice = get(bot.voice_clients, guild=ctx.guild)
    voice.stop()



@bot.command(pass_context=True, brief="loop a song")
async def loopq(ctx):
    global loljs
    if not str(ctx.guild.id) in loljs:
        loljs[str(ctx.guild.id)] = {}
        loljs[str(ctx.guild.id)]['loop'] = False
        loljs[str(ctx.guild.id)]['que'] = []
        loljs[str(ctx.guild.id)]["crp"] = 0

    loljs[str(ctx.guild.id)]['loop'] = True
    #print(loljs[str(ctx.guild.id)]['loop'])


@bot.command(pass_context=True, brief="stops loop a song")
async def loopqd(ctx):
    global loljs
    if not str(ctx.guild.id) in loljs:
        loljs[str(ctx.guild.id)] = {}
        loljs[str(ctx.guild.id)]['loop'] = False
        loljs[str(ctx.guild.id)]['que'] = []
        loljs[str(ctx.guild.id)]["crp"] = 0

    loljs[str(ctx.guild.id)]['loop'] = False




@bot.command(pass_context=True, brief="stops all music")
async def oof(ctx):
    global loljs
    voice = get(bot.voice_clients, guild=ctx.guild)

    if not str(ctx.guild.id) in loljs:
        loljs[str(ctx.guild.id)] = {}
        loljs[str(ctx.guild.id)]['loop'] = False
        loljs[str(ctx.guild.id)]['que'] = []



    loljs[str(ctx.guild.id)]['que'] = None
    try:
        voice.stop()
    except:
        pass


@bot.command(pass_context=True, brief="test command/ping command")
async def hello(ctx):
    await ctx.channel.send("hello")


@bot.command(pass_context=True)
async def connect(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()


@bot.command(pass_context=True, brief="disconects bot from voice channel")
async def d(ctx):
    server = ctx.message.guild.voice_client
    await server.disconnect()


@bot.command(brief="shows songs in que", help="just .que LOOOOL")
async def que(ctx, nam):
    nam = int(nam)
    global loljs
    n = 0
    if nam == None:
        n = 0
    if nam == 1:
        n = 0
    if nam == 2:
        n = 5
    if nam == 3:
        n = 10
    if nam == 4:
        n = 15





    qee = loljs[str(ctx.guild.id)]['que']

    embed = discord.Embed(title="QUE (:", description="Song que", color=0x00ff00)
    embed.set_author(name="VASABI", url="https://github.com/VASABIcz/idkmypythondiscordbot")

    try:
        embed.add_field(name=qee[0+n], value=1+n, inline=False)
    except:
        pass
    try:
        embed.add_field(name=qee[1+n], value=2+n, inline=False)
    except:
        pass
    try:
        embed.add_field(name=qee[2+n], value=3+n, inline=False)
    except:
        pass
    try:
        embed.add_field(name=qee[3+n], value=4+n, inline=False)
    except:
        pass
    try:
        embed.add_field(name=qee[4+n], value=5+n, inline=False)
    except:
        pass
    embed.set_footer(text="page<{}>".format(nam))
    await ctx.send(embed=embed)


@bot.command(brief="remove 1 specific song from que ", help=".r number of song (use .que)")
async def r(ctx, *, id):
    id = int(id)
    global loljs
    if not str(ctx.guild.id) in loljs:
        loljs[str(ctx.guild.id)] = {}
        loljs[str(ctx.guild.id)]['loop'] = False
        loljs[str(ctx.guild.id)]['que'] = []
    del loljs[str(ctx.guild.id)]['que'][int(id - 1)]


@bot.command(brief="cringe", help="cringe")
async def cringe(ctx):
    await ctx.channel.send("https://tenor.com/view/joy-emoji-gamer-moment-gif-15953868")


@bot.command(brief="Plays a single video, from a youtube URL", help="song name or URL")
async def dump(ctx):
    global loljs

    if not str(ctx.guild.id) in loljs:
        loljs[str(ctx.guild.id)] = {}
        loljs[str(ctx.guild.id)]['loop'] = False
        loljs[str(ctx.guild.id)]['que'] = []
        loljs[str(ctx.guild.id)]["crp"] = 0
    id = ctx.author.id

    try:
        with open('save.json', 'r+') as f:
            filee = json.load(f)
    except:
        with open('save.json', 'w+') as f:
            f.write('{}')
            filee = json.load(f)

    if not str(id) in filee:
        filee[str(id)] = {}
        filee[str(id)]['que'] = []
    filee[str(id)]['que'] = loljs[str(ctx.guild.id)]['que']
    #print(filee[str(id)]['que'])

    with open('save.json', 'w') as f:
        json.dump(filee, f)


@bot.command(brief="Plays a single video, from a youtube URL", help="song name or URL")
async def load(ctx, ):
    global loljs

    if not str(ctx.guild.id) in loljs:
        loljs[str(ctx.guild.id)] = {}
        loljs[str(ctx.guild.id)]['loop'] = False
        loljs[str(ctx.guild.id)]['que'] = []
        loljs[str(ctx.guild.id)]["crp"] = 0
    id = ctx.author.id

    try:
        with open('save.json', 'r+') as f:
            filee = json.load(f)
    except:
        with open('save.json', 'w+') as f:
            f.write('{}')
            filee = json.load(f)

    loljs[str(ctx.guild.id)]['que'] = filee[str(id)]['que']
    #print(loljs[str(ctx.guild.id)]['que'])

    with open('save.json', 'w') as f:
        json.dump(filee, f)
    await ctx.invoke(bot.get_command('p'), urlee="fb51rdf6vb1f5b4rdf1bf51rfg4d")

# TODO Bug fix
# TODO embed
# TODO link  cache DONE
# TODO make all extracrion on start ASI NE LIK SE SMAZE PO CASE
@bot.command(brief="Plays a single video, from a youtube URL", help="song name or URL")
async def p(ctx, *, urlee):
    global loljs
    if not str(ctx.guild.id) in loljs:
        loljs[str(ctx.guild.id)] = {}
        loljs[str(ctx.guild.id)]['loop'] = False
        loljs[str(ctx.guild.id)]['que'] = []

    # ==========================================================================================================================
    # ==========================================================================================================================
    YDL_OPTIONS = {'default_search': 'auto', 'format': 'bestaudio', 'noplaylist': 'true', 'quiet': 'true'}
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
                      'options': '-vn'}
    # ==========================================================================================================================
    # ==========================================================================================================================
    if urlee != "fb51rdf6vb1f5b4rdf1bf51rfg4d":


        with YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(urlee, download=False)
            #print(info)
            try:
                urlee = info['entries'][0]['webpage_url']
            except:
                urlee = info['webpage_url']

        if loljs[str(ctx.guild.id)]['que'] is None:
            loljs[str(ctx.guild.id)]['que'] = []


        loljs[str(ctx.guild.id)]['que'].append(urlee)

    else:
        pass
    if loljs[str(ctx.guild.id)]['que'] is None:
        loljs[str(ctx.guild.id)]['que'] = []
    if not is_connected(ctx):
        channel = ctx.author.voice.channel
        await channel.connect()
    voice = get(bot.voice_clients, guild=ctx.guild)



    while loljs[str(ctx.guild.id)]['que'] is not None:
        if not voice.is_playing():
            with YoutubeDL(YDL_OPTIONS) as ydl:
                # print(loljs[str(ctx.guild.id)]['loop'])
                if loljs[str(ctx.guild.id)]['loop'] == True:
                    lenght = len(loljs[str(ctx.guild.id)]['que'])
                    try:
                        try:
                            info = ydl.extract_info(loljs[str(ctx.guild.id)]['que'][loljs[str(ctx.guild.id)]["crp"]], download=False)
                            #print(info)
                        except:
                            await asyncio.sleep(1.5)
                            info = ydl.extract_info(loljs[str(ctx.guild.id)]['que'][loljs[str(ctx.guild.id)]["crp"]], download=False)
                            #print(info)
                    except:
                        pass

                    loljs[str(ctx.guild.id)]["crp"] += 1
                    if loljs[str(ctx.guild.id)]["crp"] == lenght:
                        loljs[str(ctx.guild.id)]["crp"] = 0
                    if loljs[str(ctx.guild.id)]['que'] == None:
                        loljs[str(ctx.guild.id)]['que'] = []
                else:
                    try:
                        try:
                            info = ydl.extract_info(loljs[str(ctx.guild.id)]['que'][0], download=False)
                            #print(info)
                        except:
                            await asyncio.sleep(3)
                            info = ydl.extract_info(loljs[str(ctx.guild.id)]['que'][0], download=False)
                            #print(info)
                    except:
                        pass
                    try:
                        del loljs[str(ctx.guild.id)]['que'][0]
                    except:
                        pass
                    if loljs[str(ctx.guild.id)]['que'] == None:
                        loljs[str(ctx.guild.id)]['que'] = []
                try:
                    try:
                        URL = info['entries'][0]['url']
                        URL_s = info['entries'][0]['webpage_url']
                        tit = info['entries'][0]['title']
                        thumb = info['entries'][0]['thumbnail']

                    except:
                        URL = info['url']
                        URL_s = info['webpage_url']
                        tit = info['title']
                        thumb = info['thumbnail']
                except:
                    pass

            info = None
            try:
                voice.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
                voice.is_playing()
                embed = discord.Embed(title=tit, url=URL_s, description="Now playing:", color=0x00ff00)
                embed.set_author(name="VASABI", url="https://github.com/VASABIcz/idkmypythondiscordbot")
                embed.set_thumbnail(url=thumb)
                await ctx.send(embed=embed)
                URL = None
                URL_s = None
                tit = None
                thumb = None
            except:
                pass







        else:
            try:
                await ctx.send("")
            except:
                pass

@bot.event
async def on_message(message):
    if message.content == "야":
        await message.channel.send("왜")
    if message.content == "ㅎㅇ":
        await message.channel.send("ㅂ2")
    if message.content == "!효":
        await message.channel.send("효오오오오오오오오오오오오오오오오")
    if message.content == "!효빡이":
        await message.channel.send("ㅇㅈ")

    #임베드
    if message.content == "임베드내놔":
        embed = discord.Embed(colour=discord.Colour.red(), title="제목", description="설명")
        embed.set_thumbnail(url="https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2F20160123_158%2Fnoonssm_1453542521621yQQEd_JPEG%2FTaylor_Daniel_%25C0%25CF%25B7%25AF%25BD%25BA%25C6%25AE12.jpg&type=sc960_832")
        embed.set_image(url="https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2F20121223_78%2Fekrtmgnsxm25_13562686938748CePa_JPEG%2F%25C0%25CF%25B7%25AF%25BD%25BA%25C6%25AE21.jpg&type=sc960_832")
        embed.set_footer(text=message.author, icon_url=message.author.avatar_url)
        embed.add_field(name="필드 제목", value="필드 설명", inline=False) #inline이 False라면 다음줄로 넘긴다.
        await message.channel.send(embed=embed)
    
    if message.content.startswith(f"!채널메세지"):
        ch = client.get_channel(int(message.content[7:25]))
        await ch.send(message.content[26:])

    if message.content == '내정보': #메세지 내용이 "내정보" 라면 user 변수를 자식으로 정하는 것
        user = message.author
        date = datetime.datetime.utcfromtimestamp(((int(user.id) >> 22) + 1420070400000) / 1000)
        await message.channel.send(f"{message.author.mention}의 가입일 : {date.year}/{date.month}/{date.day}")
        await message.channel.send(f"{message.author.mention}의 이름 / 아이디 / 닉네임 : {user.name} / {user.id} / {user.display_name}")
        await message.channel.send(message.author.avatar_url)



@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

access_token = os.environ["BOT_TOKEN"]
bot.run(access_token)
