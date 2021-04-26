import discord
import os
import requests
import json
import random
from keep_alive import keep_alive


client = discord.Client()

Araaa = ["/ara", "/araara", "/Araara", "/AraAra" "ara ara", "awa awa", "ara", "Ara!", "ara!", "ARA", "ARA ARA", "AWA AWA", "/ARA", "/ARAARA", "/ARA ARA"]
NoAra = ["pain", "NO", "None for you", "Never!", "504 Bad Gateway: I hit you now", "Nooooo", "aspdijspdisj", "sdosdjsoidj", "dfgdjkfg", "Aughhh", "a-- no", "ばか やろ!", "バカ."]
Nyaaa = ["NYA", "nyan", "nyan nyan", "nya nya", "NYAAA", "nyanya", "nya", "/nya", "/nyanya", "/NYANYA", "/NYA", "/NYAN", "/nyannyan", "/NYANNYAN", "nyaaaa", "NYA NYA", "NYANYA"]
NoNya = ["No nyas for you", "don't wanna", "no u" "Are you satisfied?", "hahahahahah funny", "Keep at it", "Next", "Not free!", "ahhhhh no", "ふざけるな!", "バカ.", "geez", "Nooooo", "You first", "ジーーー, じーーー", "nya~"]
Ihy = ["#cancelled", "Shutuuup", "shshjsjkjdjd", "asdiojdsdjlsd", "..I love you too.", "Pfffft", "Shushhh!", "Noooo", "Awww I love me too", "404 Error: lol", "400 Error Bad Request: Reciprocate love module not found.", "Uhm, ok", "sure", "...", "Sylvain is true husbando, not u", "ばか やろ!", "バカ.", "No", "Sad", "What did you expect?", "Does your name start with S and end with an N? Two syllables? Rhymes with Sylvain?", "Sorry no room", "wow", "sldklsajjksdjf", "*stares in displeased*", "*slow clap*", "uh huh"]
Boba = ["Finish your boba!", "Go get one right now", "Sounds like you need another", "DRINK", "Boba time!", "100% yes", "#facts"]
Yum = ["curry", "curryyy", "Curry", "Curry!"]
Curry = ["curryyyyy", "Oooo yum!", "Craving some now", "Curry!? Where!", "Food!", "おいしい~"]
Advisor = ["Boba, it's all you need.", "Life's tough but a bed is soft y'know.", "Go to sleep. At 2AM.", "Ask yourself this: Will you survive?", "*sigh* You just never learn huh.", "Hmmm idk.", "You come to me for help? rip", "Go to sleep!", "Drink water.", "Whatever it is you need to do just do it. No excuse!"]
Twitch = ["now live on Twitch", "deepsealily is now"]
Live = ["@liliherd your reaper is live!", "Come watch the stream @liliherd !", "Grab your bobas @liliherd because the show is starting !"]
# configure @liliherd role mention instead of @everyone
Test = ["hey Lilibot", "hi Lilibot"]

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

    if any(word in msg for word in Twitch):
      await message.channel.send(random.choice(Live))
    
    if msg.startswith('/ily'):
        await message.channel.send(random.choice(Ihy))
    
    if msg.startswith('baaa'):
      await message.channel.send('Baaaa~')

    if any(word in msg for word in Nyaaa):
      await message.channel.send(random.choice(NoNya))

    if msg.startswith('/advice'):
      await message.channel.send(random.choice(Advisor))

    if any(word in msg for word in Araaa):
      await message.channel.send(random.choice(NoAra))
    
    if any(word in msg for word in Yum):
      await message.channel.send(random.choice(Curry))
  
keep_alive()
client.run(os.getenv('TOKEN'))