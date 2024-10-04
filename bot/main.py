import nextcord
from nextcord.ext import commands
import glob
import os
from utils.cogs import load_cogs
from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv
load_dotenv('.env')
uri = os.getenv("DBURL")

bot = commands.Bot(command_prefix="q!", intents=nextcord.Intents.all())

client = MongoClient(uri)
try:
    client.admin.command('ping')
    print("Connected")
except Exception as e:
    print(e)

load_cogs(bot)
bot.run(os.getenv('TOKEN'))