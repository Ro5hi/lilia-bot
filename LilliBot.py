import discord
import os
import requests
import json
import random
from keep_alive import keep_alive


client = discord.Client()

Araaa = ["/ara", "/araara", "/Araara", "/AraAra" "ara ara", "awa awa", "ara", "Ara!", "ara!", "ARA", "ARA ARA", "AWA AWA", "/ARA", "/ARAARA", "/ARA ARA"]
NoAra = ["pain", "NO", "None for you", "Never!", "504 Bad Gateway: I hit you now", "Nooooo", "sjkskslj", "skdjsald", "sjksjkssjks", "Aughhh", "a-- no", "ばか やろ!", "バカ."]
Nyaaa = ["NYA", "nyan", "nyan nyan", "nya nya", "NYAAA", "nyanya", "nya", "/nya", "/nyanya", "/NYANYA", "/NYA", "/NYAN", "/nyannyan", "/NYANNYAN", "nyaaaa", "NYA NYA", "NYANYA"]
NoNya = ["No nyas for you", "don't wanna", "no u" "Are you satisfied?", "hahahahahah funny", "Keep at it", "Next", "Not free!", "ahhhhh no", "ふざけるな!", "バカ.", "geez", "Nooooo", "You first", "ジーーー, じーーー", "nya~"]
Ihy = ["#cancelled", "Shutuuup", "shshjsjkjdjd", "snjsjsnjsk", "..I love you too.", "Pfffft", "Shushhh!", "Noooo", "Awww I love me too", "404 Error: lol", "400 Error Bad Request: Reciprocate love module not found.", "Uhm, ok", "sure", "...", "Sylvain is true husbando, not u", "ばか やろ!", "バカ.", "No", "Sad", "What did you expect?", "Does your name start with S and end with an N? Two syllables? Rhymes with Sylvain?", "what", "Sorry no room", "wow", "sldklsajjksdjf", "*stares in displeased*", "*slow clap*", "uh huh"]
Boba = ["Finish your boba!", "Go get one right now", "Sounds like you need another", "DRINK", "Boba time!", "100%", "Yaaa"]
Yum = ["curry", "curryyy", "Curry", "Curry!"]
Curry = ["curryyyyy", "Oooo yum!", "Craving some now", "Curry!? Where!", "Food!", "おいしい~"]
Advisor = ["Boba, it's all you need.", "Life's tough but a bed is soft y'know.", "Go to sleep. At 2AM.", "Ask yourself this: Will you survive?", "*sigh* You just never learn huh.", "Hmmm idk.", "You come to me for help? rip", "Go to sleep!", "Drink water.", "Whatever it is you need to do just do it. No excuse!"]
Twitch = ["now live on Twitch", "deepsealily is now", "@liliherd"]
Live = ["@everyone your reaper is live!", "Your weekly dose of reaper is here @everyone!", "Come watch the stream @everyone !", "Grab your bobas @everyone because the show is starting!"]
Hello = ["Hello", "hello", "hi", "Hi", "Hey Lilibot", "Hi Lilibot", "/hello", "/hi"]
Goodbye = ["Good bye", "goodbye", "Goodbye", "Bye!", "bye", "see ya"]
Goodnight = ["gnight", "gnite", "Good night", "good night", "goodnight", "nai nai", "night night"]

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content
    username = str(message.author).split('#')[0]
    user_message = str(msg)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')

    if msg.startswith('/lili'):
      await message.channel.send('```Hi, my name is LiliBot! My commands are /lili, /boba, /nya, /advice, /ily, and /ara. Discover the rest!```')

    if msg.startswith('/boba'):
        await message.channel.send(random.choice(Boba))

    if message.channel.name == 'live-notifs':
      if any(word in msg for word in Twitch):
        await message.channel.send(random.choice(Live))
        return 
        
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

    if user_message.lower() == 'hello':
      await message.channel.send(f'Hello {username}!')
      return
    elif user_message.lower() == 'bye':
      await message.channel.send(f'See ya {username}!')
      return 
    elif user_message.lower() == 'good night':
      await message.channel.send(f'Good night {username}!')
      return 
  
keep_alive()
client.run(os.getenv('TOKEN'))