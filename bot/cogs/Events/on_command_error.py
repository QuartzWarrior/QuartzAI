import nextcord
from nextcord.ext import commands


class on_command_error(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
     if isinstance(error, PermissionError):
         pass
     else:
         pass
        
        
def setup(bot):
    bot.add_cog(on_command_error(bot))