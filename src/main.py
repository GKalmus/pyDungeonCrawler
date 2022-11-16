import discord
from discord.ext import commands

import datetime


intents = discord.Intents.default()
intents.message_content = True

prefix = "$"

bot = commands.Bot(command_prefix=prefix, intents=intents)

###Klassid### 
class bcolors: #https://stackoverflow.com/questions/287871/how-do-i-print-colored-text-to-the-terminal
    HEADER = '\033[95m'
    OKBLUE = '\u001b[34m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    MAGENTA = '\u001b[35m'



###Definitsioonid###
def guildname():
    for guild in bot.guilds:
        yield guild.name

def timestamp():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def output(arg, ctx):
    outputValue = f"{bcolors().MAGENTA}{ctx}{bcolors().ENDC} kasutas {bcolors().OKGREEN}'{arg}'{bcolors().ENDC}"
    valjend = f"{timestamp()} {bcolors().OKCYAN}KÄSK{bcolors().BOLD}     {outputValue}"
    return valjend

##
@bot.event
async def on_ready():
    ##Output 
    ##Serveri nimekiri - Väljastab serverite nimekirja, kus bot on
    serverid = f"{timestamp()} {bcolors().OKCYAN}INFO{bcolors().BOLD}     {bcolors().MAGENTA}Serverid: {bcolors().ENDC}"
    for e in guildname():
        serverid += f"{bcolors().OKGREEN}{e}{bcolors().ENDC}, "
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
    print(output(f"{prefix}pilt @{member}", ctx.message.author))

    ##  

@bot.command()
async def algus(ctx):

    ##
    await ctx.send('> Siin on sinu algus')

    ##
    print(output(f"{prefix}algus", ctx.message.author))
    return


@bot.command()  #šabloon
async def spam(ctx, arg="Su ema on nunnu!!", amount=5):
    aint = 0
    i = 0

    ##Output
    while amount >= aint:
        t = ''
        while len(t) < 1800:
            i+=1
            t += str(i)+ " "+str(arg) + "\n"
        await ctx.send(f"{t}")
        aint += 1

    print(output(f"{prefix}spam {arg} {amount}", ctx.message.author))


@bot.command() # Väljastab "Memberi" pildi(Member on kas, kirja autor v pingitu)
async def testimine(ctx):
    member = ctx.message.author
    person = member.display_avatar
    ##Output
    await ctx.send(f"{person}.")

    print(output(f"{prefix}testimine {member}", ctx.message.author))
    ##  



tokenFail = open("..\\token.txt","r", encoding="UTF-8")
bot.run(tokenFail.read())
tokenFail.close()