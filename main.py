import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print('{0.user} is here!'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('/boba'):
        await message.channel.send('Finish my boba!')

client.run(os.getenv)