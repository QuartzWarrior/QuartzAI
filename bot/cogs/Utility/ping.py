from nextcord.ext import commands
import nextcord
from utils.cooldown import cooldown_slash


class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @nextcord.slash_command(name="ping", description="Get Quartz's Latency")
    @cooldown_slash(seconds=2)
    async def pings(self, ctx):
        embed = nextcord.Embed(title="Quartz Latency", description=f"> **Latency:** ``{self.bot.latency * 1000:.0f}``ms", color=nextcord.Color.purple())
        await ctx.send(embed=embed)    

    @commands.command(name="ping")
    async def pingp(self, ctx):
        embed = nextcord.Embed(title="Quartz Latency", description=f"> **Latency:** ``{self.bot.latency * 1000:.0f}``ms", color=nextcord.Color.purple())
        await ctx.reply(embed=embed)        
                
                                
def setup(bot):
    bot.add_cog(Ping(bot))
