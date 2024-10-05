from nextcord.ext import commands
import nextcord
import asyncio
from utils.perms import perms_prefix, perms_slash


class Lock(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(name="lock", description="Locks A Channel")
    @perms_slash(name="manage_roles")
    @perms_slash(name="manage_channels")
    async def lock(self, ctx, channel: nextcord.TextChannel = None):
        if channel is None:
            channel = ctx.channel
        await channel.set_permissions(ctx.guild.default_role, send_messages=False)
        embed = nextcord.Embed(
            title="🔒 | Channel Locked", 
            description=f"> **Channel:  {channel.mention}**\n> **Locked By:** {ctx.user.mention}",
            color=nextcord.Color.purple()
                )
        embed.set_footer(text="⚠️ | This Message Will Be Deleted In 4 Seconds")
        msg = await ctx.send(embed=embed)
        await asyncio.sleep(4)
        await msg.delete()
    






def setup(bot):
    bot.add_cog(Lock(bot))