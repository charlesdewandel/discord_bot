# Work with Python 3.6
import discord

TOKEN = 'your token'

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    # dialogues
    if message.content.startswith('salut'):
        await message.author.send('👋')
        await message.channel.send("salut")
    if message.content.startswith('fdp'):
        await message.channel.send("parle mieux où je t'éjectes !")
    if message.content.startswith('Alz'):
        await message.channel.send("voilà soumets-toi")
    if message.content.startswith('sur fortnite'):
        await message.channel.send("warzone est mieux")
    

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)