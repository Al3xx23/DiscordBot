# Python Functions

import discord
from discord.ext import commands

help_message = ''''>>>print (argument) : prints argument
>>>credits : prints all spacial thanks and spacial list
>>>abs : prints absolute value of number ( |-10| = 10 )
>>>ascii
>>>'''

credits_message = '''spacial thanks to "LateNever", "Rolpend FOX", "Gekou" and "FLOPPY" for supporting! special list:
Eirelly, Vertuoz, danolex, MR kotovsky, gd news, samifying, xender game, Fancy's game, dolphy, vectozavr, WOS, nexus, Dorami, meganeko and teminite
ooo (c)Alex23 the creator! ooo'''

intents = discord.Intents.default()
intents.message_content = True
TOKEN = ['MY_TOKEN']
bot = commands.Bot(command_prefix='>>>', intents=intents)

@bot.command()                      # print
async def print(ctx, *arg):
    x = ' '.join(arg)
    await ctx.send(x)

@bot.command()                      # bhelp
async def bhelp(ctx):
    await ctx.reply(help_message)

@bot.command()                      # credits
async def credits(ctx):
    await ctx.reply(credits_message)

@bot.command()                      # abs
async def abs(ctx, num):
    try:
        num = int(num)
    except ValueError:
        await ctx.send(Exception)
    else:
        if num < 0:
            await ctx.send(str(num)[1:])
        else:
            await ctx.send(num)

@bot.command()                      # pow
async def pow(ctx, x, y):
    try:
        x = int(x)
        y = int(y)
    except ValueError:
        await ctx.send(Exception)
    else:
        await ctx.send(x**y)

def range1(x):
    lst = []
    i = 0
    j = 0
    while i != x:
        lst.append(str(i))
        i+= 1

    while j != x:
        lst[int(j)] = int(j)
        j+= 1
    return lst
@bot.command()                  # range
async def range(ctx, x):
    try:
        x = int(x)
    except ValueError:
        await ctx.send(Exception)
    else:
        await ctx.send(range1(x))

@bot.command()                  # tuple
async def tuple(ctx, *args):
    await ctx.send(args)

@bot.command()
async def sum(ctx, *args):
    await ctx.send(sum(args))

