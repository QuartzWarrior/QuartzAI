import nextcord
from nextcord.ext import commands
from utils.perms import perms_prefix

class Announcement(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="announce")
    @perms_prefix(name="administrator")
    async def announce(self, ctx: commands.Context, channel: nextcord.TextChannel,  *, message: str):
        embed = nextcord.Embed(
            title="Announcement",
            description=message,
            color=nextcord.Color.purple()
        )
        embed.set_thumbnail(ctx.guild.icon.url)
        e2 = nextcord.Embed(
            title="Announcement Sent",
            description=f"> **Channel:**  **{channel.mention}**\n> **Admin:** {ctx.author.mention}\n> **Message:**\n```{message}```",
            color=nextcord.Color.purple()
        )
        await channel.send(content="||@everyone||", embed=embed)
        await ctx.reply(embed=e2)



def setup(bot):
    bot.add_cog(Announcement(bot))