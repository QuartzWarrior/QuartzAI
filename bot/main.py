import nextcord
from nextcord.ext import commands
import glob
import os
from utils.cogs import load_cogs
from dotenv import load_dotenv
load_dotenv('.env')

bot = commands.Bot(command_prefix="q!", intents=nextcord.Intents.all())

load_cogs(bot)
bot.run(os.getenv('TOKEN'))