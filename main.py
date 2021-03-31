import discord
import os
import requests
import json
from serverping import keep_alive
import random
from discord_webhook import DiscordWebhook

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

badwords = ['fuck', 'shit', 'fag', 'piss', 'dick', 'ass', 'bitch', 'bastard', 'nigga', 'nigger']

channel = client.get_channel(823130492953296928) # replace with channel ID that you want to send to


@client.event
async def on_ready():
  print('Bot is online on {0.user}'.format(client))
  game = discord.Game(f"on {len(client.guilds)} servers! | !zen help")
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
  if message.author.bot:
    return
  if message.content.startswith('!zen list'):
    servers = list(client.guilds)
    await message.channel.send(f"Connected on {str(len(servers))} servers:")
    await message.channel.send('\n' .join(guild.name for guild in client.guilds))
    print(f'request.zenlist - {message.author}')

  if message.content.startswith('!zen ping'):
      if round(client.latency * 1000) <= 50:
        embed=discord.Embed(title="Pong", description=f":ping_pong: Pingpingpingpingping!\n My Latency Is {round(client.latency *1000)} Milliseconds!", color= 474747)
      elif round(client.latency * 1000) <= 100:
        embed=discord.Embed(title="Pong", description=f":ping_pong: Pingpingpingpingping!\n My Latency Is {round(client.latency *1000)} Milliseconds!", color= 474747)
      elif round(client.latency * 1000) <= 200:
        embed=discord.Embed(title="Pong", description=f":ping_pong: Pingpingpingpingping!\n My Latency Is {round(client.latency *1000)} Milliseconds!", color= 474747)
      else:
        embed=discord.Embed(title="Pong", description=f":ping_pong: Pingpingpingpingping!\n My Latency Is {round(client.latency *1000)} Milliseconds!", color= 474747)
      await message.channel.send(embed=embed)
      print(f'request.zenping - {message.author}')
      #await channel.send('zenping')

  
  if any(bad_word in message.content.strip().lower() for bad_word in badwords):
  #         await message.delete()
  #         await message.channel.send(f'>>> {message.author} , Please dont swear.')
           print(f'utils.profanity - {message.author}')
           #await channel.send('zenprofanity')

  msg = message.content

  
  #INSPIRE CMD
  if msg.startswith('!zen inspire'):
    quote = get_quote()
    quote_text = '**__Quote:__**\n> {}'.format(quote)
    await message.channel.send(quote_text)
    print(f'request.zeninspire - {message.author}')
    #await channel.send('zeninspire')

  #DOGPIC CMD
  if msg.startswith('!zen doggo'):
    embed = get_puppy()
    await message.channel.send(embed=embed)
    print(f'request.zendoggo - {message.author}')
    #await channel.send('zendog')
  

  #BOTINFO CMD
  if msg.startswith('!zen info'):
    formattext = '**`ℹ             Info              ℹ`**\n \n ⏳ __*Date of start:*__ ⌛ `2021 march 21st` \n \n 😊 **__*Made with:*__** \n **🤖 Love, Replit and UptimeRobot 🤖 \n 👩‍💻 __Lines of code: 145.__ 👩‍💻 \n \n`                                `**'
    await message.channel.send('>>> {}'.format(formattext))
    print(f'request.zeninfo - {message.author}')
    #await channel.send('zeninfo')


  #BOTINVITE CMD
  if msg.startswith('!zen invite'):
    invitetext = '✉ __**Invite for this bot:**__ ✉ \n https://discord.com/api/oauth2/authorize?client_id=823215287499096154&permissions=27648&scope=bot'
    await message.channel.send('>>> {}'.format(invitetext))
    print(f'request.zeninvite - {message.author}')
    #await channel.send('zeninvite')


  #HELP CMD
  if msg.startswith("!zen help"):
    helptext = '__**Commands:**__ \n **__Utility__** \n 🌸 `!zen inspire` ** - sends an inspirational quote. ** \n 💝`!zen gift` ** - gifts love to someone you tag. ** \n ❤ `!zen encourage` ** -sends an inspirational encouragement** \n 🐶 `!zen doggo` ** -picture of cute doggos. ** \n 👤 `!zen better` ** - helps you become a better person. ** \n 💵 `!zen coinflip` ** - heads or tails, the bot decides! ** \n \n __**Others**__ \n ℹ `!zen info` ** - shows the info of the bot. ** \n ✉ `!zen invite` ** - sends an invite for the bot. ** \n 💻 `!zen support` ** - shows the link for the support server ** \n ⬆ `!zen upvote` ** - shows the link to upvote this bot. **'
    await message.channel.send('>>> {}'.format(helptext))
    print(f'request.zenhelp - {message.author}')
    #await channel.send('zenhelp')
  


  #GIFT CMD
  if msg.startswith("!zen gift"):
    if(msg.split("!zen gift",1)[1] == ""):
      await message.channel.send('>>> Specify a 👤 **__person__** 👤 to gift something!')
      return
    gifttext = "Someone 💝 __**loves**__ 💝 you, " + msg.split("!zen gift ",1)[1]
    await message.channel.send('>>> {}'.format(gifttext))
    print(f'request.gift - {message.author}')
    #await channel.send('zengift')


  #BETTERPERSON CMD
  if msg.startswith("!zen better"): 
    await message.channel.send('>>> 🌺 **-** ' + random.choice(bpchoices) + ' **-** 🌺 ')
    print(f'request.zenbetter - {message.author}')
    #await channel.send('zenbetter')


  #ENCOURAGE CMD
  if msg.startswith("!zen encourage"):
    await message.channel.send('>>> ❤ **-  ' + random.choice(encouragements) + '  -** ❤')
    print(f'request.zenencourage - {message.author}')
    #await channel.send('zenencourage')



  #COINFLIP CMD
  if msg.startswith("!zen coinflip"):
    outcomes = ['Tails', 'Heads']
    await message.channel.send(f"> You got **{random.choice(outcomes)}**.")
    print(f'request.zencoinflip - {message.author}')
    #await channel.send('zencoinflip')


  
  if msg.startswith('!zen upvote'):
    await message.channel.send(f">>> {message.author.name}, we would be really happy if you would upvote our bot! 💝 \nhttps://discordbotlist.com/bots/zenbot/upvote")
    print(f'request.zenupvote - {message.author}')
    #await channel.send('zenupvote')



  if msg.startswith('!zen support'):
    await message.channel.send(f">>> {message.author.name}, if you need support, join this server: \nhttps://discord.gg/afbrVCGSs5")
    print(f'request.zensupport - {message.author}')
    #await channel.send('zensupport')





#BOTONTIME
keep_alive()
client.run(os.getenv('TOKEN'))