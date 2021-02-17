import discord
from dotenv import load_dotenv
import os
import json
import random
from discord.ext import commands, tasks
from discord.ext.commands import cooldown, CommandOnCooldown
from discord.ext.commands.cooldowns import BucketType

class Currency(commands.Cog):
    def __init__(self, client):
        self.client = client



    @commands.command()
    @commands.cooldown(1, 120, commands.BucketType.user)
    async def find(self,ctx):
        try:
            global r
            r = int(float(random.randint(1,100))/2)
            if r == 0:
                return await ctx.send(embed=discord.Embed(title="You suck, you didn't find any nuts.", color=0xe0ad53))
            if r == 1:
                return await ctx.send(embed=discord.Embed(title="You found a nut!", color=0xe0ad53))
            if r == 50:
                return await ctx.send(embed=discord.Embed(title="You found 50 nuts! Woah...", color=0xe0ad53))
            else:
                return await ctx.send(embed=discord.Embed(title="You found " + str(r) + " nuts!", color=0xe0ad53))
        except Exception as error: 
            raise error

    @find.error
    async def find_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(embed=discord.Embed(title="Woah slow down, buddy.", description = f"Your puny body is still recovering from the last expedition. You should rest for {int(error.retry_after)} more seconds.", color=0xd60000))

    @commands.command()
    async def search(self, ctx):
        await find.invoke(ctx)

def setup(client):
    client.add_cog(Currency(client))