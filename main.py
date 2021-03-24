import discord
import os
import requests
import json
from serverping import keep_alive
import random



client = discord.Client()


#BETTERPERSON ARRAY
#bbp source: https://www.inc.com/john-rampton/15-ways-to-become-a-better-person.html
bpchoices = ['Compliment Yourself!', 'Dont Make Excuses!', 'Let Go Of Anger!', 'Practice Forgiveness!', 'Be Honest And Direct!', 'Be Helpful!', 'Listen To Others!', 'Act Locally!', 'Always Be Polite!', 'Be Yourself!', 'Be Open To Change!', 'Be Respectful!', 'Dont Show Up Empty-Handed!', 'Educate Yourself!', 'Suprise People!']


#ENGOURAGE ARRAY
encouragements = [
  'You shine!',
  'You make me smile!',
  'Im so proud of you!',
  'You are special!',
  'You are unique!',
  'I believe in you!',
  'You have a great attitude!',
  'Keep up the good work!',
  'Youre a shining star',
  'Youre so talented!',
  'You are incredible',
  'You are so kind'
]

headers = {
    'x-rapidapi-key': "dad-jokes.p.rapidapi.com",
    'x-rapidapi-host': "x-rapidapi-key"
    }



@client.event
async def on_ready():
  print('Bot is online on {0.user}'.format(client))
  game = discord.Game("!zen help")
  await client.change_presence(status=discord.Status.idle, activity=game)

url = "https://dad-jokes.p.rapidapi.com/random/joke"

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = "**" + json_data[0]['q'] + "** *-" + json_data[0]['a'] + "*"
  return(quote)

def get_puppy():
  response = requests.get("https://dog.ceo/api/breeds/image/random")
  embed_data = json.loads(response.text)
  string=embedpic = embed_data['message']
  e = discord.Embed(title= 'Doggo Picture')
  e.set_image(url=embedpic)
  e.set_footer(text= "This is what you wanted 😃")
  return(e)



@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if message.author.bot:
    return

  msg = message.content


  
  #INSPIRE CMD
  if msg.startswith('!zen inspire'):
    quote = get_quote()
    quote_text = '**__Quote:__**\n> {}'.format(quote)
    await message.channel.send(quote_text)

  #DOGPIC CMD
  if msg.startswith('!zen doggo'):
    embed = get_puppy()
    await message.channel.send(embed=embed)
  

  #BOTINFO CMD
  if msg.startswith('!zen info'):
    formattext = '**ℹ  __Info__  ℹ**\n \n ⏳ __*Date of start:*__ `2021 march 21st`\n 😊 __*Made with:*__ \n \n **Love, Replit and UptimeRobot \n __Lines of code: 143.__**'
    await message.channel.send('>>> {}'.format(formattext))


  #BOTINVITE CMD
  if msg.startswith('!zen invite'):
    invitetext = '✉ __**Invite for this bot:**__ ✉ \n https://discord.com/api/oauth2/authorize?client_id=823215287499096154&permissions=27648&scope=bot'
    await message.channel.send('>>> {}'.format(invitetext))


  #HELP CMD
  if msg.startswith("!zen help"):
    helptext = '__**Commands:**__ \n 🌸 `!zen inspire` ** - sends an inspirational quote. ** \n ℹ `!zen info` ** - shows the info of the bot. ** \n ✉ `!zen invite` ** - sends an invite for the bot. ** \n 💝`!zen gift` ** - gifts love to someone you tag. ** \n 👤 `!zen better` ** - helps you become a better person. ** \n 🐶 `!zen doggo` ** -picture of cute doggos. ** \n ❤ `!zen encourage` ** -sends an inspirational encouragement**'
    await message.channel.send('>>> {}'.format(helptext))
  


  #GIFT CMD
  if msg.startswith("!zen gift"):
    if(msg.split("!zen gift",1)[1] == ""):
      await message.channel.send('>>> Specify a 👤 **__person__** 👤 to gift something!')
      return
    gifttext = "Someone 💝 __**loves**__ 💝 you, " + msg.split("!zen gift ",1)[1]
    await message.channel.send('>>> {}'.format(gifttext))


  #BETTERPERSON CMD
  if msg.startswith("!zen better"): 
    await message.channel.send('>>> 🌺 **-** ' + random.choice(bpchoices) + ' **-** 🌺 ')


  #ENCOURAGE CMD
  if msg.startswith("!zen encourage"):
    await message.channel.send('>>> ❤ **-  ' + random.choice(encouragements) + '  -** ❤')


  #MEME CMD
  if msg.startswith("!zen meme"):
    response = requests.get(url, headers=headers)
    r= response.text
    await message.channel.send(r)
    #await message.channel.send(f">>> **{r['setup']}**\n||{r['punchline']}||")


  #COINFLIP CMD
  if msg.startswith("!zen coinflip"):
    outcomes = ['Tails', 'Heads']
    await message.channel.send(f"> You got **{random.choice(outcomes)}**.")


#BOTONTIME
keep_alive()
client.run(os.getenv('TOKEN'))