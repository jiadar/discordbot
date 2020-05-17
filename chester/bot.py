import discord
from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv("TOKEN")

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    print(f"Received message: {message.content}")
    # if message.author == client.user:
    #     return

    if message.content.startswith('hello'):
        await message.channel.send('Hello from the bot!')

client.run(TOKEN)
