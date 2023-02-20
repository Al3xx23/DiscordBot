# list_methods

import discord
from discord.ext import commands


intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='>>>', intents=intents)
@bot.command()
async def append(ctx, lst, obj):
    try:
        await ctx.send(lst.append(obj))
    except Exception as e:
        await ctx.send(e)

@bot.command()
async def clear(ctx, lst):
    try:
        await ctx.send(lst.clear())
    except Exception as e:
        await ctx.send(e)

@bot.command()
async def count(ctx, lst, obj):
    try:
        await ctx.send(lst.count(obj))
    except Exception as e:
        await ctx.send(e)

@bot.command()
async def copy(ctx, s):
    try:
        await ctx.send(s)
    except Exception as e:
        await ctx.send(e)

@bot.command()
async def extend(ctx, lst1, lst2):
    try:
        await ctx.send(lst1.extend(lst2))
    except Exception as e:
        await ctx.send(e)
