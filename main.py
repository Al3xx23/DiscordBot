import discord
from discord.ext import commands
import TOKEN
import String_methods as sm
import Python_functions as pf

TOKEN = TOKEN.TOKEN

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='>>>', intents=intents)

String_methods = [
    sm.ascii, sm.find, sm.center, sm.casefold, sm.lower, sm.upper, sm.endswith, sm.encode,
    sm.expandtabs, sm.index, sm.isalnum, sm.isdigit, sm.isdecimal, sm.isidentifier, sm.islower,
    sm.isupper, sm.partition, sm.replace, sm.lstrip, sm.swapcase, sm.isprintable, sm.istitle,
    sm.ljust, sm.join, sm.isspace, sm.issuper
]

Python_functions = [
    pf.abs, pf.bhelp, pf.credits, pf.pow, pf.print, pf.range, pf.tuple, pf.sum, pf.cls, pf.bool
]


for x in range(len(String_methods)):
    bot.add_command(String_methods[x])

for i in range(len(Python_functions)):
    bot.add_command(Python_functions[i])

bot.run(TOKEN)