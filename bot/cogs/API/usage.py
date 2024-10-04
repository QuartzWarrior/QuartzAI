import nextcord
from nextcord.ext import commands
from pymongo import MongoClient
import os
from dotenv import load_dotenv
load_dotenv()

class Usage(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.client = MongoClient(os.getenv('DBURL'))
        self.db = self.client['api']
        self.collection = self.db['api_keys']  

    @nextcord.slash_command(name="usage")
    async def usage(self, ctx):
        user_id = str(ctx.user.id)
        user_data = self.collection.find_one({"user_id": user_id})
        if user_data:
            usage_count = user_data.get('usage', 0)
            embed = nextcord.Embed(
                title="API Key Usage",
                description=f">  **Usage:** ``{usage_count}``",
                color=nextcord.Color.purple()
            )
            await ctx.send(embed=embed)
        else:
            error_embed = nextcord.Embed(
                title="Usage Error",
                description="> **You Do Not Have An API Key. Use `/get-key` To Generate One & Start Using Quartz AI Today!**",
                color=nextcord.Color.red()
            )
            await ctx.send(embed=error_embed)

    def cog_unload(self):
        self.client.close()
        
def setup(bot):
    bot.add_cog(Usage(bot))
