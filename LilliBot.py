import discord
import os
import requests
import json
import random
from keep_alive import keep_alive


client = discord.Client()

Nope = ["/ara", "ara ara"]
Ihy = ["#cancelled", "Shutuuup", "shshjsjkjdjd", "asdiojdsdjlsd", "..I love you too.", "Pfffft", "Shushhh!", "Noooo", "Awww I love me too", "404 Error", "101: Reciprocate love module not found", "Uhm, ok", "sure", "...", "Sylvain is true husbando, not u"]
Bad = ["pain", "NO", "None for you", "Never!"]

# def get_twitch():
#   response = requests.get("https://twitch.tv/deepsealily")
#   json_data = json.loads(response.text)
#   notif = json_data[0][t] 

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content

    if msg.startswith('/lili'):
      await message.channel.send('Hi, my name is LiliBot! My commands are /boba, /nya, and /ara. Discover the rest!')

    if msg.startswith('/boba'):
        await message.channel.send('Finish your boba!')
    
    if msg.startswith('/ily'):
        await message.channel.send(random.choice(Ihy))
    
    if msg.startswith('baaa'):
      await message.channel.send('Baaaa~')

    if msg.startswith('/nya'):
      await message.channel.send('No free nyas, sorry~')

    if any(word in msg for word in Nope):
      await message.channel.send(random.choice(Bad))
  
keep_alive()
client.run(os.getenv('TOKEN'))