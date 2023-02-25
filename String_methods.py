# string metods

import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='>>>', intents=intents)


#                                   ___ STRING METODS ___

@bot.command()  # capitalize           № 1
async def capitalize(ctx, *args):
    s = ' '.join(args)
    await ctx.send(s.capitalize())


@bot.command()  # lower                № 2
async def lower(ctx, s):
    await ctx.send(s.lower())


@bot.command()  # upper               № 3
async def upper(ctx, s):
    await ctx.send(s.upper())


@bot.command()  # casefold             № 4
async def casefold(ctx, s):
    await ctx.send(s.casefold())


@bot.command()  # center               № 5
async def center(ctx, s, n1: int, n2=' '):
    await ctx.send(s.center(n1, n2))


@bot.command()  # encode               № 6
async def encode(ctx, s):
    await ctx.send(s.encode())


@bot.command()  # endswith             № 7
async def endswith(ctx, s, x):
    await ctx.send(s.endswith(x))


@bot.command()  # find                 № 8
async def find(ctx, s, x, start=0, end=-1):
    try:
        await ctx.send(s.find(x, start, end))
    except Exception as e:
        await ctx.send(e)


@bot.command()  # expandtabs           № 9
async def expandtabs(ctx, s, tabsize: int):
    try:
        s1 = s.expandtabs(tabsize)
        await ctx.send(s1)
    except Exception as e:
        await ctx.send(e)


@bot.command()  # index                № 10
async def index(ctx, s, *args):
    args = ' '.join(args)
    await ctx.send(args.index(s))


@bot.command()  # isalnum              № 11
async def isalnum(ctx, s):
    await ctx.send(s.isalnum())


@bot.command()  # isascii              № 12
async def isascii(ctx, s):
    await ctx.send(s.isascii())


@bot.command()  # isdecimal            № 13
async def isdecimal(ctx, s):
    await ctx.send(s.isdecimal())


@bot.command()  # isdigit             № 14
async def isdigit(ctx, s):
    await ctx.send(s.isdigit())


@bot.command()  # isidentifier         № 15
async def isidentifier(ctx, s):
    await ctx.send(s.isidentifier())


@bot.command()  # islower              № 16
async def islower(ctx, s):
    await ctx.send(s.islower())


@bot.command()  # upper                № 17
async def isupper(ctx, s):
    await ctx.send(s.isupper())


@bot.command()  # isnumeric            № 18
async def isnumeric(ctx, s):
    await ctx.send(s.isnumeric())


@bot.command()  # isprintable          № 19
async def isprintable(ctx, s):
    await ctx.send(s.isprintable())


@bot.command()  # isspace               # 20
async def isspace(ctx, s):
    await ctx.send(s.isspace())


@bot.command()  # istitle              № 21
async def istitle(ctx, s):
    await ctx.send(s.istitle())


@bot.command()  # issuper              № 22
async def issuper(ctx, s):
    await ctx.send(s.issuper())


@bot.command()  # partition            № 23
async def partition(ctx, num, *args):
    s = ' '.join(args)
    await ctx.send(s.partition(num))


@bot.command()  # replace              № 24
async def replace(ctx, s1, s2, *args):
    args = ' '.join(args)
    await ctx.send(args.replace(s1, s2))


@bot.command()  # lstrip               № 25
async def lstrip(ctx, *args):
    s = ' '.join(args)
    await ctx.send(s.lstrip())


@bot.command()  # swapcase             № 26
async def swapcase(ctx, *args):
    s = ' '.join(args)
    await ctx.send(s.swapcase())


@bot.command()  # ljust                № 27
async def ljust(ctx, s, num: int):
    await ctx.send(s.ljust(num))


@bot.command()  # join                 № 30
async def join(ctx, s1, *args):
    await ctx.send(s1.join(args))


@bot.command()  # zfill                № 31
async def zfill(ctx, s, num):
    await ctx.send(s.zfill(num))


@bot.command()  # splitlines           № 32
async def splitlines(ctx, *args):
    s = ' '.join(args)
    await ctx.send(s.splitlines())


@bot.command()  # rstrip               № 33
async def rstrip(ctx, *args):
    s = ' '.join(args)
    await ctx.send(s.rstrip())


@bot.command()  # rsplit               № 34
async def rsplit(ctx, *args):
    s = ' '.join(args)
    await ctx.send(s.rsplit)


@bot.command()  # rpartition           № 35
async def rpartition(ctx, value, *args):
    args = ' '.join(args)
    await ctx.send(args.rpartition(value))


@bot.command()  # split                № 36
async def split(ctx, value, *args):
    args = ' '.join(args)
    await ctx.send(args.split(value))


@bot.command()  # strip                № 37
async def strip(ctx, *args):
    s = ' '.join(args)
    await ctx.send(s.strip)


@bot.command()  # rjust               № 38
async def rjust(ctx, num, *args):
    s = ' '.join(args)
    await ctx.send(s.rjust(num))


@bot.command()  # rindex              № 39
async def rindex(ctx, ind, *args):
    s = ' '.join(args)
    await ctx.send(s.rindex(ind))


@bot.command()  # count              № 40
async def count(ctx, s, *args):
    s1 = ' '.join(args)
    await ctx.send(s1.count(s))


@bot.command()  # startswith          № 41
async def startswith(ctx, start, *args):
    s = ' '.join(args)
    await ctx.send(s.startswith(start))


@bot.command()  # isalpha             № 42
async def isalpha(ctx, *args):
    s = ' '.join(args)
    await ctx.send(s.isalpha())
