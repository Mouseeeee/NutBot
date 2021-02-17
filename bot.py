import discord
from dotenv import load_dotenv
import os
import json
import random
from discord.ext import commands, tasks
from discord.ext.commands import cooldown, CommandOnCooldown
from discord.ext.commands.cooldowns import BucketType

load_dotenv()

intents = discord.Intents.default()
intents.members = True
client = commands.AutoShardedBot(intents=intents, command_prefix =['n.'], case_insensitive=True)

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game("with nuts 🥴"))
    print("Logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.lower() == "nut":
        global r
        r = random.randint(1,3)
        if r == 1:
            await message.add_reaction("\N{CHESTNUT}")
        if r == 2:
            await message.add_reaction("\N{NUT AND BOLT}")
        if r == 3:
            await message.add_reaction("\N{PEANUTS}")

for filename in os.listdir(r"C:\Program Files\Microsoft VS Code\programs\NutBot\cogs"):
     if filename.endswith(".py"):
            client.load_extension(f'cogs.{filename[:-3]}')

client.run(os.getenv("TOKEN"))