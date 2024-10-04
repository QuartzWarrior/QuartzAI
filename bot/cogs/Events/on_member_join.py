import nextcord
from nextcord.ext import commands

class on_member_join(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.welcome_channel_id = 1291254895118258247

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.get_channel(self.welcome_channel_id)
        if channel:
            embed = nextcord.Embed(title=f"Welcome {member.name}", description="> **Make Sure To Read The Server <#1290871802746245212>**\n> **API Support:** <#1291117576927318067>\n> **API Endpoints:** <#1291117672443936871>\n", color=nextcord.Color.purple())
            embed.set_footer(text=f"ID: {member.id}")
            await channel.send(content=f"Welcome {member.mention} To Quartz AI", embed=embed)

def setup(bot):
    bot.add_cog(on_member_join(bot))