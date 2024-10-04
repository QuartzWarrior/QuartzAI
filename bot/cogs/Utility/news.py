import nextcord
from nextcord.ext import commands

class News(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='news')
    async def news(self, ctx):
        allowed_user_id = 1254593641742209097  
        if ctx.author.id != allowed_user_id:
            return
        news_embed = nextcord.Embed(
            title="📣 | Quartz API",
            description="- We Are Proud To Announce That We Will Be Bringing Back Quartz AI\n- What Next?\n- I Will Be Working On V2 Of The API, Untill Then I Will Try Get V1 Online Untill V2 Releases.\n- We Look Forward To Bringing Back This API!",
            color=nextcord.Color.purple()
        )
        news_embed.set_footer(text='News Update from Quartz AI')
        await ctx.send(content="||@everyone||", embed=news_embed)


def setup(bot):
    bot.add_cog(News(bot))