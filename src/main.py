import discord
from discord.ext import commands


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

###Definitsioonid###
def guildname():
    for guild in bot.guilds:
        yield guild.name

##
@bot.event
async def on_ready():
    ##Output
    ##Serveri nimekiri - Väljastab serverite nimekirja, kus bot on
    print("Serverid:", end=" ")
    for e in guildname():
        print(e, end=", ")
    print("\n")
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
    outputValue = f'{messageauthor} kasutas "{prefix}pilt {member}"'
    print(f"{timestamp()} {outputValue}")
    ##  


@bot.command()  #šabloon
async def spam(ctx, arg="Su ema on nunnu!!", amount=5):
    messageauthor = ctx.message.author
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


@bot.command() # Väljastab "Memberi" pildi(Member on kas, kirja autor v pingitu)
async def testimine(ctx):
    member = ctx.message.author
    messageauthor = member
    person = member.display_avatar
    ##Output
    await ctx.send(f"{person}.")
    outputValue = f'{messageauthor} kasutas "{prefix}testimine {member}"'
    print(f"{timestamp()} {outputValue}")
    ##  



tokenFail = open("token.txt","r", encoding="UTF-8")
bot.run(tokenFail.read())
tokenFail.close()