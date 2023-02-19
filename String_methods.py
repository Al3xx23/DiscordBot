#string metods

import discord
from discord.ext import commands


intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='>>>', intents=intents)

#                                   ___ STRING METODS ___

@bot.command()                          # ascii
async def ascii(ctx, s):
    try:
        await ctx.send(s.ascii())
    except Exception as e:
        print(e)

@bot.command()                          # capitalize
async def capitalize(ctx, *args):
    try:
        s = ' '.join(args)
        z = s.capitalize()
        await ctx.send(z)
    except Exception as e:
        await ctx.send(e)

@bot.command()                          # lower
async def lower(ctx, s):
    try:
        z = s.lower()
        await ctx.send(z)
    except Exception as e:
        await ctx.send(e)


@bot.command()                           # upper
async def upper(ctx, s):
    try:
        z = s.upper()
        await ctx.send(z)
    except Exception as e:
        await ctx.send(e)

@bot.command()                          # casefold
async def casefold(ctx, s):
    try:
        z = s.casefold()
        await ctx.send(z)
    except Exception as e:
        await ctx.send(e)

@bot.command()                          # center
async def center(ctx, s, n1: int, n2=' '):
    try:
        z = s.center(n1, n2)
        await ctx.send(z)
    except Exception as e:
        await ctx.send(e)

@bot.command()                          # encode
async def encode(ctx, s):
    try:
        z = s.encode()
        await ctx.send(z)
    except Exception as e:
        await ctx.send(e)

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

@bot.command()                          # index
async def index(ctx, s, *args):
    try:
        args = ' '.join(args)
        await ctx.send(args.index(s))
    except Exception as e:
        await ctx.send(e)

@bot.command()                          # isalnum
async def isalnum(ctx, s):
    try:
        await ctx.send(s.isalnum())
    except Exception as e:
        await ctx.send(e)

@bot.command()                          # isascii
async def isascii(ctx, s):
    try:
        await ctx.send(s.isascii())
    except Exception as e:
        await ctx.send(e)

@bot.command()                          # isdecimal
async def isdecimal(ctx, s):
    try:
        await ctx.send(s.isdecimal())
    except Exception as e:
        await ctx.send(e)

@bot.command()                           # isdigit
async def isdigit(ctx, s):
    try:
        await ctx.send(s.isdigit())
    except Exception as e:
        await ctx.send(e)

@bot.command()                          # isidentifier
async def isidentifier(ctx, s):
    try:
        await ctx.send(s.isidentifier())
    except Exception as e:
        await ctx.send(e)

@bot.command()                          # islower
async def islower(ctx, s):
    try:
        await ctx.send(s.islower())
    except Exception as e:
        await ctx.send(e)

@bot.command()                          # upper
async def isupper(ctx, s):
    try:
        await ctx.send(s.isupper())
    except Exception as e:
        await ctx.send(e)

@bot.command()                          # isnumeric
async def isnumeric(ctx, s):
    try:
        await ctx.send(s.isnumeric())
    except Exception as e:
        await ctx.send(e)

@bot.command()                          #isprintable
async def isprintable(ctx, s):
    try:
        await ctx.send(s.isprintable())
    except Exception as e:
        await ctx.send(e)

@bot.command()                          # isspace
async def isspace(ctx, s):
    try:
        await ctx.send(s.isspace())
    except Exception as e:
        await ctx.send(e)

@bot.command()                          # istitle
async def istitle(ctx, s):
    try:
        await ctx.send(s.istitle())
    except Exception as e:
        await ctx.send(e)

@bot.command()                          # issuper
async def issuper(ctx, s):
    try:
        await ctx.send(s.issuper())
    except Exception as e:
        await ctx.send(e)

@bot.command()                          # partition
async def partition(ctx, center, *args):
    try:
        s = ' '.join(args)
        await ctx.send(s.partition(center))
    except Exception as e:
        await ctx.send(e)

@bot.command()                          # replace
async def replace(ctx, s1, s2, *args):
    try:
        args = ' '.join(args)
        await ctx.send(args.replace(s1, s2))
    except Exception as e:
        await ctx.send(e)
@bot.command()                          # lstrip
async def lstrip(ctx, *args):
    try:
        s = ' '.join(args)
        await ctx.send(s.lstrip())
    except Exception as e:
        await ctx.send(e)

@bot.command()                          # swapcase
async def swapcase(ctx, s):
    try:
        await ctx.send(s.swapcase())
    except Exception as e:
        await ctx.send(e)

@bot.command()                          # ljust
async def ljust(ctx, s, num: int):
    try:
        await ctx.send(s.ljust(num))
    except Exception as e:
        await ctx.send(e)

@bot.command()                          # join
async def join(ctx, s1, *args):
    try:
        z = s1.join(args)
        await ctx.send(z)
    except Exception as e:
        await ctx.send(e)