import discord
from discord.ext import commands


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

###Definitsioonid###

def faililug(nimekiri, fail):
    for rida in fail:
        animi = rida.strip("\n")
        nimekiri.append(animi)

def timestamp():
    return datetime.datetime.now()

def chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]

def guildname():
    for guild in bot.guilds:
        yield guild.name

##
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(
        type=discord.ActivityType.playing,
        name="Vi sitter här i Venten och spelar lite DotA", )
    )
    ##Output
    ##Serveri nimekiri - Väljastab serverite nimekirja, kus bot on
    print("Serverid:", end=" ")
    for e in guildname():
        print(e, end=", ")
    print("\n")
    ##

@bot.command() # Väljastab "Memberi" pildi(Member on kas, kirja autor v pingitu)
async def suema(ctx, arg):
      await ctx.send(f'{arg}, ma panin teda')


@bot.command()  #šabloon
async def spam(ctx, arg="Su ema on nunnu!!", amount=5):
    messageauthor = ctx.message.author
    aint = 0
    i = 0
    ##Output'
    while amount >= aint:
        t = ''
        while len(t) < 1800:
            i+=1
            t += str(i)+ " "+str(arg) + "\n"
        await ctx.send(f"{t}")
        aint += 1


tokenFail = open("token.txt","r", encoding="UTF-8")
bot.run(tokenFail.read())
tokenFail.close()

