#string metods

import discord
from discord.ext import commands


intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='>>>', intents=intents)

#                                   ___ STRING METODS ___

@bot.command()                          # ascii                 1
async def ascii(ctx, s):
    try:
        await ctx.send(s.ascii())
    except Exception as e:
        print(e)

@bot.command()                          # capitalize            2
async def capitalize(ctx, *args):
    try:
        s = ' '.join(args)
        z = s.capitalize()
        await ctx.send(z)
    except Exception as e:
        await ctx.send(e)

@bot.command()                          # lower                 3
async def lower(ctx, s):
    try:
        z = s.lower()
        await ctx.send(z)
    except Exception as e:
        await ctx.send(e)


@bot.command()                           # upper                4
async def upper(ctx, s):
    try:
        z = s.upper()
        await ctx.send(z)
    except Exception as e:
        await ctx.send(e)

@bot.command()                          # casefold              5
async def casefold(ctx, s):
    try:
        z = s.casefold()
        await ctx.send(z)
    except Exception as e:
        await ctx.send(e)

@bot.command()                          # center                6
async def center(ctx, s, n1: int, n2=' '):
    try:
        z = s.center(n1, n2)
        await ctx.send(z)
    except Exception as e:
        await ctx.send(e)

@bot.command()                          # encode                7
async def encode(ctx, s):
    try:
        z = s.encode()
        await ctx.send(z)
    except Exception as e:
        await ctx.send(e)

@bot.command()                          # endswith              8
async def endswith(ctx, s, x):
    z = s.endswith(x)
    await ctx.send(z)

@bot.command()                          # find                  9
async def find(ctx, s, x, start=0, end=-1):
    z = s.find(x, start, end)
    await ctx.send(z)

@bot.command()                          # expandtabs            10
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

@bot.command()                          # index                 11
async def index(ctx, s, *args):
    try:
        args = ' '.join(args)
        await ctx.send(args.index(s))
    except Exception as e:
        await ctx.send(e)

@bot.command()                          # isalnum               12
async def isalnum(ctx, s):
    try:
        await ctx.send(s.isalnum())
    except Exception as e:
        await ctx.send(e)

@bot.command()                          # isascii               13
async def isascii(ctx, s):
    try:
        await ctx.send(s.isascii())
    except Exception as e:
        await ctx.send(e)

@bot.command()                          # isdecimal             14
async def isdecimal(ctx, s):
    try:
        await ctx.send(s.isdecimal())
    except Exception as e:
        await ctx.send(e)

@bot.command()                           # isdigit              15
async def isdigit(ctx, s):
    try:
        await ctx.send(s.isdigit())
    except Exception as e:
        await ctx.send(e)

@bot.command()                          # isidentifier          16
async def isidentifier(ctx, s):
    try:
        await ctx.send(s.isidentifier())
    except Exception as e:
        await ctx.send(e)

@bot.command()                          # islower               17
async def islower(ctx, s):
    try:
        await ctx.send(s.islower())
    except Exception as e:
        await ctx.send(e)

@bot.command()                          # upper                 19
async def isupper(ctx, s):
    try:
        await ctx.send(s.isupper())
    except Exception as e:
        await ctx.send(e)

@bot.command()                          # isnumeric             20
async def isnumeric(ctx, s):
    try:
        await ctx.send(s.isnumeric())
    except Exception as e:
        await ctx.send(e)

@bot.command()                          # isprintable           21
async def isprintable(ctx, s):
    try:
        await ctx.send(s.isprintable())
    except Exception as e:
        await ctx.send(e)

@bot.command()                          # isspace               22
async def isspace(ctx, s):
    try:
        await ctx.send(s.isspace())
    except Exception as e:
        await ctx.send(e)

@bot.command()                          # istitle               23
async def istitle(ctx, s):
    try:
        await ctx.send(s.istitle())
    except Exception as e:
        await ctx.send(e)

@bot.command()                          # issuper               24
async def issuper(ctx, s):
    try:
        await ctx.send(s.issuper())
    except Exception as e:
        await ctx.send(e)

@bot.command()                          # partition             25
async def partition(ctx, center, *args):
    try:
        s = ' '.join(args)
        await ctx.send(s.partition(center))
    except Exception as e:
        await ctx.send(e)

@bot.command()                          # replace               26
async def replace(ctx, s1, s2, *args):
    try:
        args = ' '.join(args)
        await ctx.send(args.replace(s1, s2))
    except Exception as e:
        await ctx.send(e)
@bot.command()                          # lstrip                27
async def lstrip(ctx, *args):
    try:
        s = ' '.join(args)
        await ctx.send(s.lstrip())
    except Exception as e:
        await ctx.send(e)

@bot.command()                          # swapcase              28
async def swapcase(ctx, s):
    try:
        await ctx.send(s.swapcase())
    except Exception as e:
        await ctx.send(e)

@bot.command()                          # ljust                 29
async def ljust(ctx, s, num: int):
    try:
        await ctx.send(s.ljust(num))
    except Exception as e:
        await ctx.send(e)

@bot.command()                          # join                  30
async def join(ctx, s1, *args):
    try:
        z = s1.join(args)
        await ctx.send(z)
    except Exception as e:
        await ctx.send(e)

@bot.command()                          # zfill                 31
async def zfill(ctx, s, num):
    try:
        await ctx.send(s.zfill(num))
    except Exception as e:
        await ctx.send(e)

@bot.command()                          # splitlines            32
async def splitlines(ctx, *args):
    try:
        s = ' '.join(args)
        await ctx.send(s.splitlines())
    except Exception as e:
        await ctx.send(e)

@bot.command()                          # rstrip                33
async def rstrip(ctx, *args):
    try:
        s = ' '.join(args)
        await ctx.send(s.rstrip())
    except Exception as e:
        await ctx.send(e)

@bot.command()                          # rsplit                34
async def rsplit(ctx, *args):
    try:
        s = ' '.join(args)
        await ctx.send(s.lsplit)
    except Exception as e:
        await ctx.send(e)

@bot.command()                          # rpartition            35
async def rpartition(ctx, value, *args):
    try:
        args = ' '.join(args)
        await ctx.send(args.rpartition(value))
    except Exception as e:
        await ctx.send(e)

@bot.command()                          # split                 36
async def split(ctx, value, *args):
    try:
        args = ' '.join(args)
        await ctx.send(args.split(value))
    except Exception as e:
        await ctx.send(e)

@bot.command()                          # strip                 37
async def strip(ctx, *args):
    try:
        s = ' '.join(args)
        await ctx.send(s.strip)
    except Exception as e:
        await ctx.send(e)

@bot.command()                          # rjust                38
async def rjust(ctx, num, *args):
    try:
        s = ' '.join(args)
        await ctx.send(s.rjust(num))
    except Exception as e:
        await ctx.send(e)

@bot.command()                          # rindex               39
async def rindex(ctx, ind, *args):
    try:
        s = ' '.join(args)
        await ctx.send(s.rindex(ind))
    except Exception as e:
        await ctx.send(e)