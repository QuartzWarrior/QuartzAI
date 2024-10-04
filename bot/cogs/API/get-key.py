import nextcord
from nextcord.ext import commands
from pymongo import MongoClient
import uuid
import os
from dotenv import load_dotenv
load_dotenv()

class APIKey(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.client = MongoClient(os.getenv('DBURL'))
        self.db = self.client['api']
        self.collection = self.db['api_keys']

    @nextcord.slash_command(name="get-key")
    async def get_key(self, ctx):
        user_id = str(ctx.user.id)
        user_data = self.collection.find_one({"user_id": user_id})

        if user_data:
            api_key = user_data['api_key']
            embed = nextcord.Embed(title="Quartz API Key", description=f"> Your Existing API Key: ||{api_key}||", color=nextcord.Color.purple())
            embed.set_footer(text="Please Contact Support For API Key Resets & Issues")
            await ctx.send(embed=embed, ephemeral=True)
        else:
            api_key = "quartz-" + str(uuid.uuid4())
            new_user_data = {"user_id": user_id, "api_key": api_key, "usage": 0}
            self.collection.insert_one(new_user_data)
            embed = nextcord.Embed(title="Quartz API Key", description=f"> Your New API Key: ||{api_key}||", color=nextcord.Color.purple())
            embed.set_footer(text="Please Contact Support For API Key Resets & Issues")
            await ctx.send(embed=embed, ephemeral=True)


    def cog_unload(self):
        self.client.close()


def setup(bot):
    bot.add_cog(APIKey(bot))
