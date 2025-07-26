import discord
import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == 'こんにちは':
        await message.channel.send('こんにちは＠bot')

if BOT_TOKEN:
    client.run(BOT_TOKEN)
else:
    print('BOT_TOKENが設定されていません。')