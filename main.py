import discord
from discord.ext import commands
import TOKEN
import String_methods
import Python_functions

TOKEN = TOKEN.TOKEN

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='>>>', intents=intents)

bot.add_command(String_methods.ascii)
bot.add_command(String_methods.find)
bot.add_command(String_methods.capitalize)
bot.add_command(String_methods.center)
bot.add_command(String_methods.casefold)
bot.add_command(String_methods.lower)
bot.add_command(String_methods.upper)
bot.add_command(String_methods.endswith)
bot.add_command(String_methods.encode)
bot.add_command(String_methods.expandtabs)


bot.add_command(Python_functions.abs)
bot.add_command(Python_functions.bhelp)
bot.add_command(Python_functions.credits)
bot.add_command(Python_functions.pow)
bot.add_command(Python_functions.print)
bot.add_command(Python_functions.range)
bot.add_command(Python_functions.tuple)
bot.add_command(Python_functions.sum)

#nothing
#ok

bot.run(TOKEN)