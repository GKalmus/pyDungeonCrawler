import sys
sys.path.insert(1,'../lib/')
import colorsESC as esc

import player

import json

import discord
from discord.ext import commands
import datetime

intents = discord.Intents.default()
intents.message_content = True

prefix = "$"

bot = commands.Bot(command_prefix=prefix, intents=intents)



###Definitsioonid###
def guildname():
    for guild in bot.guilds:
        yield guild.name

def timestamp():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def output(autor, arg):
    outputValue = f"{esc.fg().MAGENTA}{autor}{esc.util().RESET} kasutas {esc.fg().GREEN}'{arg}'{esc.util().RESET}"
    valjend = f"{esc.fg().GRAY}{timestamp()} {esc.util().BOLD}{esc.fg().CYAN}KÄSK{esc.util().RESET}     {outputValue}"
    return valjend



##
@bot.event
async def on_ready():
    ##Output 
    ##Serveri nimekiri - Väljastab serverite nimekirja, kus bot on
    serverid = f"{timestamp()} {esc.fg().CYAN}INFO{esc.util().RESET}     {esc.fg().MAGENTA}Serverid: {esc.util().RESET}"
    for e in guildname():
        serverid += f"{esc.fg().GREEN}'{e}'{esc.util().RESET}, "
    print(serverid)

    ##

@bot.command() # Väljastab "Memberi" pildi(Member on kas, kirja autor v pingitu)
async def pic(ctx, member: discord.Member = None):
    messageauthor = ctx.message.author
    if not member:
        member = messageauthor

    ##Embed
    show_avatar = discord.Embed(description=f"[{member}](%s)" % member.display_avatar, color=0x001eff)
    show_avatar.set_image(url="{}".format(member.display_avatar))
    show_avatar.set_footer(text=f'Küsis {ctx.message.author}')

    ##Output
    await ctx.send(embed=show_avatar)
    print(output(ctx.message.author, f"{prefix}pilt @{member}"))

    ##  

@bot.command()
async def algus(ctx):

    ##
    await ctx.send('> Siin on sinu algus')

    ##
    print(output(ctx.message.author, f"{prefix}algus"))
    return




@bot.command() # Väljastab "Memberi" pildi(Member on kas, kirja autor v pingitu)
async def testimine(ctx):
    member = ctx.message.author
    person = member.display_avatar

    ##Output
    await ctx.send(f"{person}.")

    print(output(ctx.message.author, f"{prefix}testimine {member}"))
    ##  

@bot.command()
async def profile(ctx):
    member = ctx.message.author
    playerInfo = player.Player(ctx.message.guild.id, member.id).getInfo()
    await ctx.send(playerInfo)

@bot.command()
async def info(ctx, member: discord.Member = None):
    messageauthor = ctx.message.author
    if not member:
        member = messageauthor
    playerInfo = player.Player(str(ctx.message.guild.id), str(member.id)).getStats()
    embed=discord.Embed(title="Player card")
    embed.set_thumbnail(url="{}".format(member.display_avatar))
    embed.set_footer(text=f'Küsis {ctx.message.author}')
    embed.add_field(name="Stats", value=f"LvL: {playerInfo['level']}\n XP: {playerInfo['xp']}", inline=True)
    embed.add_field(name="Attributes", value=f"ATK: {playerInfo['attack']}\n DEF: {playerInfo['defence']}", inline=True)
    ##Output
    await ctx.send(embed=embed)

@bot.command()
async def attack(ctx):
    return
    
    
  



tokenFail = open("..\\token.txt","r", encoding="UTF-8")
bot.run(tokenFail.read())
tokenFail.close()