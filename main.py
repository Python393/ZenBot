import discord
import os
import requests
import json
from serverping import keep_alive

client = discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))
  game = discord.Game("!zen help")
  await client.change_presence(status=discord.Status.idle, activity=game)



def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = "**" + json_data[0]['q'] + "** *-" + json_data[0]['a'] + "*"
  return(quote)



@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content
  
  if msg.startswith('!zen inspire'):
    quote = get_quote()
    quote_text = '**__Quote:__**\n> {}'.format(quote)
    await message.channel.send(quote_text)
  
  if msg.startswith('!zen info'):
    formattext = '**ℹ__  Info  __ℹ**\n \n ⏳ __*Date of start:*__ `**2021 march 21st**`\n 😊 __*Made with:*__ \n \n **Love, Replit and UptimeRobot**'
    await message.channel.send('>>> {}'.format(formattext))

  if msg.startswith('!zen invite'):
    invitetext = '✉__**Invite for this bot:**__ `https://discord.com/api/oauth2/authorize?client_id=823215287499096154&permissions=27648&scope=bot`'
    await message.channel.send('>>> {}'.format(invitetext))

  if msg.startswith("!zen help"):
    helptext = '__**Commands:**__ \n 🌸 `!zen inspire` ** - sends an inspirational quote. ** \n ℹ `!zen info` ** - shows the info of the bot. ** \n ✉ `!zen invite` ** - sends an invite for the bot. **'
    await message.channel.send('>>> {}'.format(helptext))
  

keep_alive()
client.run(os.getenv('TOKEN'))
