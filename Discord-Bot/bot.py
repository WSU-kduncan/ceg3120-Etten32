import os

import discord
import random
from dotenv import load_dotenv

load_dotenv()
#print(os.getenv('DISCORD_TOKEN'))
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]

    mmm_quotes = [
        'I’m not sure whether Poppy ate something, or something ate Poppy, but there’s a good deal of Poppy in this creature regardless. ',
        'Leave now, before it\'s too late...',
        'What a shame, they are so very useful. Why, did you know that if a beaver two feet long with a tail a foot and a half long can build a dam twelve feet high and six feet wide in two days, all you would need to build Boulder Dam is a beaver sixty-eight feet long with a fifty-one-foot tail?',
        'Seventeen!',
        'For his lady fair, Lancelot was able to endure whips, cuts, bruises, and all manner of incredible tortures and humiliations; but peanut butter and jelly, he could not have done.',
        'I’ve never driven one o’ these newfangled fescraft before, hee-hee. Back in my day they all had stick shifts.',
    ]

    if message.content == 'mmm':
        #response = random.choice(brooklyn_99_quotes)
        response = random.choice(mmm_quotes)
        await message.channel.send(response)

client.run(TOKEN)
