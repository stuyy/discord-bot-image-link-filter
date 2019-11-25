import discord
import requests
import pytesseract
import os
from dotenv import load_dotenv
from io import BytesIO
from PIL import Image

client = discord.Client() # Instantiate Client class from discord.py

@client.event
async def on_ready():
    print('{} has logged in.'.format(client.user.display_name))

@client.event
async def on_message(message):
    if message.author.bot:
        return

    await check_attachment()
    '''
        Your text command checks all down below
    '''

async def check_attachment():
    pass
client.run(os.getenv("BOT_TOKEN"))