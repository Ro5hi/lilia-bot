import discord
import os
import requests
import json
import random

client = discord.Client()

Nope = ["/ara", "ara ara"]

Bad = ["pain", "NO"]

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    msg = message.content

    if msg.startswith('/boba'):
        await message.channel.send('Finish your boba!')
        
    if msg.startswith('baaa'):
      await message.channel.send('Baaaa~')
      
    if msg.startswith('/nya'):
        await.message.channel.send('No free nyas, sorry~')
               
    if any(word in msg for word in Nope):
        await.message.channel.send(random.choice(Bad))

client.run(os.getenv('TOKEN'))