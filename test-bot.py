import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('/boba'):
        await message.channel.send('Finish your boba!')
        
    if message.content.startswith('baaa'):
      await message.channel.send('Baaaa~')

client.run(os.getenv('TOKEN'))