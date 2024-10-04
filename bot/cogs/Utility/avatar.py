from nextcord.ext import commands
import nextcord
from utils.cooldown import cooldown_slash


class Avatar(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @nextcord.slash_command(name="avatar", description="Get A Users Avatar")
    @cooldown_slash(seconds=2)
    async def avatars(self, ctx, user: nextcord.Member = None):
        if user == None:
            user = ctx.user
        else:
            user = user
        if user.avatar.url == None:
            embed = nextcord.Embed(title="Avatar Error", description="> **This User Does Not Have An Avatar Uploaded.**", color=nextcord.Color.red())
            await ctx.send(embed=embed)
        else:
            embed = nextcord.Embed(title=f"{user.name}'s Avatar", color=nextcord.Color.purple())
            embed.set_image(url=user.avatar.url)
            await ctx.send(embed=embed)
 
    @commands.command(name="avatar", description="Get A Users Avatar")
    async def avatarp(self, ctx, user: nextcord.Member = None):
        if user == None:
            user = ctx.user
        else:
            user = user
        if user.avatar.url == None:
            embed = nextcord.Embed(title="Avatar Error", description="> **This User Does Not Have An Avatar Uploaded.**", color=nextcord.Color.red())
            await ctx.reply(embed=embed)
        else:
            embed = nextcord.Embed(title=f"{user.name}'s Avatar", color=nextcord.Color.purple())
            embed.set_image(url=user.avatar.url)
            await ctx.reply(embed=embed)                
                                
def setup(bot):
    bot.add_cog(Avatar(bot))