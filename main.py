import discord
from discord.ext import commands
import TOKEN
import String_methods as sm
import Python_functions as pf
import list_methods as lm
import Key_Words as kw

TOKEN = TOKEN.TOKEN

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='>>>', intents=intents)

String_methods = [
    sm.ascii, sm.find, sm.center, sm.casefold, sm.lower, sm.upper, sm.endswith, sm.encode,
    sm.expandtabs, sm.index, sm.isalnum, sm.isdigit, sm.isdecimal, sm.isidentifier, sm.islower,
    sm.isupper, sm.partition, sm.replace, sm.lstrip, sm.swapcase, sm.isprintable, sm.istitle,
    sm.ljust, sm.join, sm.isspace, sm.issuper, sm.rpartition, sm.rjust, sm.zfill, sm.rstrip,
    sm.strip, sm.split, sm.splitlines, sm.rsplit, sm.rindex, sm.capitalize, sm.isascii, sm.isnumeric
]

Python_functions = [
    pf.abs, pf.bhelp, pf.credits, pf.pow, pf.print, pf.range, pf.tuple, pf.sum, pf.cls, pf.bool
]

list_methods = [
    lm.append, lm.clear, lm.count, lm.copy, lm.extend
]

Key_Words = [
    kw.true, kw.false, kw.Raise
]

for x in range(len(String_methods)):
    bot.add_command(String_methods[x])

for i in range(len(Python_functions)):
    bot.add_command(Python_functions[i])

for z in range(len(list_methods)):
    bot.add_command(list_methods[z])

for a in range(len(Key_Words)):
    bot.add_command(Key_Words[a])

bot.run(TOKEN)