import discord
from discord.ext import commands

TOKEN = 'NDg3MDY0MzE3MDQ1NTA2MDUx.DntY5w.SoP9AsxOoJRtrTrtUeaSVeJQo6E'

client = commands.Bot(command_prefix = '.')

def log(event, fn = 'log'):
    file = open(fn, 'a+')
    file.write(event)
    file.write('\n')
    file.close()
    return (event)

@client.event
async def on_ready():
    print('I am ready to receive')

@client.event
async def on_message(message):
    author = message.author
    content = message.content
    entry = f'{author}: {content}'
    # log(message, fn = 'msg-log')
    print(entry)
    dump(message)

client.run(TOKEN)
