import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')
        await message.channel.send('Sa oled lapsendatud')

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)

tokenFail = open("token.txt","r", encoding="UTF-8")
client.run(tokenFail.read())
tokenFail.close()

