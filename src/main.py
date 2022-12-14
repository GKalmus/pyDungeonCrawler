## Autor: Gert Kalmus

import sys
sys.path.insert(1,'../lib/')
import colorsESC as esc

import player

import json

import discord
from discord.ext import commands
import datetime
import random

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

def Player(playerID):
    return player.Player(playerID)




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

@bot.command() # Väljastab "Memberi" pildi(Member on kas, kirja autor v pingitu)
async def testimine(ctx):
    member = ctx.message.author
    person = member.display_avatar

    ##Output
    await ctx.send(f"{person}.")

    print(output(ctx.message.author, f"{prefix}testimine {member}"))
    ##  

@bot.command() # Väljastab Mängja stat kaardi
async def info(ctx, member: discord.Member= None):
    ##Member - vaatab, kas kedagi on pingitud selle käsuga, kui ei ole siis ta võtab memberiks autori ise
    messageauthor = ctx.message.author
    if not member:
        member = messageauthor
    
    ##Player - võtab memberi info ja muudab nime
    playerInfo = Player(str(member.id))
    if playerInfo.name == "name":
        playerInfo.setName(str(member)[:-5])
 
    ##Embed - enesest mõistetav, eesti keeles manus
    embed=discord.Embed(title="Player card", description=f"**HP**:{playerInfo.health}\n **Status**: {playerInfo.status}")
    embed.set_author(name=f"{member}", icon_url=f"{member.display_avatar}")
    embed.set_footer(text=f"Küsis {ctx.message.author}")
    embed.add_field(name="Stats", value=f"**LvL**: {playerInfo.level}\n **XP**: {playerInfo.xp}", inline=True)
    embed.add_field(name="Attributes", value=f"**ATK**: {playerInfo.attack}\n **DEF**: {playerInfo.defence}", inline=True)

    ##Output - väljastab manuse
    await ctx.send(embed=embed)
    print(output(ctx.message.author, f"{prefix}info {member}"))

@bot.command()
async def attack(ctx, member: discord.Member= None):
    ##Member - vaatab, kas kedagi on pingitud selle käsuga, kui ei ole siis ta võtab memberiks autori ise
    messageauthor = ctx.message.author
    embed = discord.Embed(title="Attack")
    embed.set_footer(text=f"Küsis {ctx.message.author}")
    if not member:
        member = messageauthor

    ##Player info
    target = Player(str(member.id))
    target.setName(str(member)[:-5])
    attacker = Player(str(messageauthor.id))
    attacker.setName(str(messageauthor)[:-5])

    ##Arvutused
    targetHPthen = int(target.health)
    target.damage(attacker.attack)
    targetHPnow = int(target.health)
    dmgReceived = targetHPthen - targetHPnow

    ##Embed
    embed.add_field(name= f"{attacker.name} attacked {target.name}",value=f"**Damage received**: {dmgReceived}")
    
    ##Output
    await ctx.send(embed=embed)

@bot.command()
async def heal(ctx, member: discord.Member= None):
    ##Member - vaatab, kas kedagi on pingitud selle käsuga, kui ei ole siis ta võtab memberiks autori ise
    messageauthor = ctx.message.author
    embed = discord.Embed(title="Heal")
    embed.set_footer(text=f"Küsis {ctx.message.author}")
    if not member:
        member = messageauthor

    ##Player info
    target = Player(str(member.id))
    target.setName(str(member)[:-5])
    healer = Player(str(messageauthor.id))
    healer.setName(str(messageauthor)[:-5])

    ##Arvutused
    targetHPthen = int(target.health)
    if targetHPthen == 0:
        target.revive()
    else:
        target.setHealth(targetHPthen + healer.attack)
    targetHPnow = int(target.health)
    hpHealed = targetHPnow - targetHPthen

    ##Embed
    embed.add_field(name= f"{healer.name} healed {target.name}",value=f"**Health received**: {hpHealed}")
    
    ##Output
    await ctx.send(embed=embed)


@bot.command()##XP saamine igapäevaselt (random)
@commands.cooldown(1, 86400, commands.BucketType.user)
async def daily(ctx):
    author = ctx.message.author
    player = Player(str(author.id))
    player.setName(str(author)[:-5])
    if player.status == "Alive" or player.status == "Immortal":
        x=random.randint(1, 100)
        player.getXp(x)
        await ctx.send(f"{author.mention} said {x} XP-d juurde. Nüüd on sinu XP {player.xp}")
    else:
        await ctx.send(f"{author.mention} oled surnud. Surnud ei saa XP-d")



try:
    tokenFail = open("..\\token.txt","r", encoding="UTF-8")
    bot.run(tokenFail.read())
    tokenFail.close()
except:
    print("Sul puudub token.txt fail")

