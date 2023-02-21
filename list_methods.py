# list_methods

import discord
from discord.ext import commands


intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='>>>', intents=intents)
@bot.command()                          # append                    № 1
async def append(ctx, obj, lst):
    try:
        await ctx.send(lst.append(obj))
    except Exception as e:
        await ctx.send(e)

@bot.command()                          # clear                     № 2
async def clear(ctx, lst):
    try:
        await ctx.send(lst.clear())
    except Exception as e:
        await ctx.send(e)

@bot.command()                          # copy                      № 3
async def copy(ctx, s):
    try:
        await ctx.send(s)
    except Exception as e:
        await ctx.send(e)

@bot.command()                          # extend                    № 4
async def extend(ctx, lst1, lst2):
    try:
        await ctx.send(lst1.extend(lst2))
    except Exception as e:
        await ctx.send(e)


@bot.command()                          # list_index                № 5
async def list_index(ctx, s, lst):
    try:
        await ctx.send(lst.index(s))
    except Exception as e:
        await ctx.send(e)


@bot.command()                          # list_count                № 6
async def list_count(ctx, s, lst):
    try:
        await ctx.send(lst.count(s))
    except Exception as e:
        await ctx.send(e)


@bot.command()                          # insert                    № 7
async def insert(ctx, obj, num, lst):
    try:
        await ctx.send(lst.instert(num, obj))
    except Exception as e:
        await ctx.send(e)


@bot.command()                          # pop                       № 8
async def pop(ctx, s, lst):
    try:
        await ctx.send(lst.pop(s))
    except Exception as e:
        await ctx.send(e)


@bot.command()                          # remove                    № 9
async def remove(ctx, s, lst):
    try:
        await ctx.send(lst.remove(s))
    except Exception as e:
        await ctx.send(e)


@bot.command()                          # reverse                    № 10
async def reverse(ctx, lst):
    try:
        await ctx.send(lst.reverse())
    except Exception as e:
        await ctx.send(e)


@bot.command()                          # sort                       № 11
async def sort(ctx, boolean, lst):
    try:
        await ctx.send(lst.sort(reverse=boolean))
    except Exception as e:
        await ctx.send(e)
