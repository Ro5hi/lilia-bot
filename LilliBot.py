import discord
import os
import requests
import json
import random
from keep_alive import keep_alive


client = discord.Client()

Araaa = ["/ara", "ara ara", "awa awa", "ara", "Ara!", "ara!"]
NoAra = ["pain", "NO", "None for you", "Never!", "504 Bad Gateway: I hit you now", "Nooooo", "aspdijspdisj", "sdosdjsoidj", "dfgdjkfg", "Aughhh", "a-- no"]
NoNya= ["No nyas for you", "..nya.", "Are you satisfied?", "hahahahahah funny", "Keep at it", "Next", "Not free!", "ahhhhh no"]
Ihy = ["#cancelled", "Shutuuup", "shshjsjkjdjd", "asdiojdsdjlsd", "..I love you too.", "Pfffft", "Shushhh!", "Noooo", "Awww I love me too", "404 Error: N o p e", "400 Error Bad Request: Reciprocate love module not found.", "Uhm, ok", "sure", "...", "Sylvain is true husbando, not u"]
Boba = ["Finish your boba!", "Go get one right now", "Sounds like you need another", "DRINK", "Boba time!"]
Yum = ["curry", "curryyy", "Curry", "Curry!"]
Curry = ["curryyyyy", "Oooo yum!", "Craving some now", "Curry!? Where!", "Food!"]

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
        await message.channel.send(random.choice(Boba))
    
    if msg.startswith('/ily'):
        await message.channel.send(random.choice(Ihy))
    
    if msg.startswith('baaa'):
      await message.channel.send('Baaaa~')

    if msg.startswith('/nya'):
      await message.channel.send(random.choice(NoNya))

    if any(word in msg for word in Araaa):
      await message.channel.send(random.choice(NoAra))
    
    if any(word in msg for word in Yum):
      await message.channel.send(random.choice(Curry))
  
keep_alive()
client.run(os.getenv('TOKEN'))