import nextcord
from nextcord.ext import commands


class Usage(commands.Cog):
    def __init__(self, bot):
        self.bot = bot



def setup(bot):
    bot.add_cog(Usage(bot))