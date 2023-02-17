#string metods

import discord
from discord.ext import commands


intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='>>>', intents=intents)

#                                   ___ STRING METODS ___
@bot.command()                          # ascii
async def ascii(ctx, s):
    await ctx.send(f'\'{s}\'')

@bot.command()                          # capitalize
async def capitalize(ctx, s):
    z = s.capitalize()
    await ctx.send(z)

@bot.command()                          # lower
async def lower(ctx, s):
    z = s.lower()
    await ctx.send(z)


@bot.command()                          # upper
async def upper(ctx, s):
    z = s.upper()
    await ctx.send(z)

@bot.command()                          # casefold
async def casefold(ctx, s):
    z = s.casefold()
    await ctx.send(z)

@bot.command()                          # center
async def center(ctx, s, n1: int, n2=' '):
    z = s.center(n1, n2)
    await ctx.send(z)

@bot.command()                          # encode
async def encode(ctx, s):
    z = s.encode()
    await ctx.send(z)

@bot.command()                          # endswith
async def endswith(ctx, s, x):
    z = s.endswith(x)
    await ctx.send(z)

@bot.command()                          # find
async def find(ctx, s, x, start=0, end=-1):
    z = s.find(x, start, end)
    await ctx.send(z)

@bot.command()                          # expandtabs
async def expandtabs(ctx, s, tabsize: int):
    try:
        s1 = s.expandtabs(tabsize)
    except ValueError as e:
        await ctx.send(e)
    else:
        await ctx.send(s1)

@bot.command()
async def nothing(ctx):
    await ctx.send('nothing')