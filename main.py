#
import discord
import os
import requests
import json
from serverping import keep_alive
import random

client = discord.Client()

#bbp source: https://www.inc.com/john-rampton/15-ways-to-become-a-better-person.html
bpchoices = ['Compliment Yourself!', 'Dont Make Excuses!', 'Let Go Of Anger!', 'Practice Forgiveness!', 'Be Honest And Direct!', 'Be Helpful!', 'Listen To Others!', 'Act Locally!', 'Always Be Polite!', 'Be Yourself!', 'Be Open To Change!', 'Be Respectful!', 'Dont Show Up Empty-Handed!', 'Educate Yourself!', 'Suprise People!']

@client.event
async def on_ready():
  print('Bot is online on {0.user}'.format(client))
  game = discord.Game("!zen help")
  await client.change_presence(status=discord.Status.idle, activity=game)
  

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

  msg = message.content
  
  if msg.startswith('!zen inspire'):
    quote = get_quote()
    quote_text = '**__Quote:__**\n> {}'.format(quote)
    await message.channel.send(quote_text)

  if msg.startswith('!zen doggo'):
    embed = get_puppy()
    await message.channel.send(embed=embed)
  
  if msg.startswith('!zen info'):
    formattext = '**ℹ  __Info__  ℹ**\n \n ⏳ __*Date of start:*__ `2021 march 21st`\n 😊 __*Made with:*__ \n \n **Love, Replit and UptimeRobot**'
    await message.channel.send('>>> {}'.format(formattext))

  if msg.startswith('!zen invite'):
    invitetext = '✉__**Invite for this bot:**__ `https://discord.com/api/oauth2/authorize?client_id=823215287499096154&permissions=27648&scope=bot`'
    await message.channel.send('>>> {}'.format(invitetext))

  if msg.startswith("!zen help"):
    helptext = '__**Commands:**__ \n 🌸 `!zen inspire` ** - sends an inspirational quote. ** \n ℹ `!zen info` ** - shows the info of the bot. ** \n ✉ `!zen invite` ** - sends an invite for the bot. ** \n 💝`!zen gift` ** - gifts love to someone you tag. ** \n 👤 `!zen better` ** - helps you become a better person. ** \n 🐶 `!zen doggo` ** -picture of cute doggos. **'
    await message.channel.send('>>> {}'.format(helptext))
  
  if msg.startswith("!zen gift"):
    if(msg.split("!zen gift",1)[1] == ""):
      await message.channel.send('>>> Specify a 👤 **__person__** 👤 to gift something!')
      return
    gifttext = "Someone 💝 __**loves**__ 💝 you, " + msg.split("!zen gift ",1)[1]
    await message.channel.send('>>> {}'.format(gifttext))

  if msg.startswith("!zen better"): 
    await message.channel.send('>>> 🌺 **-** ' + random.choice(bpchoices) + ' **-** 🌺 ')



keep_alive()
client.run(os.getenv('TOKEN'))
#