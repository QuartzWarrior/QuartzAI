from nextcord.ext import commands
import nextcord
import asyncio
from utils.perms import perms_prefix, perms_slash


class Unlock(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(name="unlock", description="Unlocks A Channel")
    @perms_slash(name="manage_roles")
    @perms_slash(name="manage_channels")
    async def unlock(self, ctx, channel: nextcord.TextChannel = None):
        if channel is None:
            channel = ctx.channel
        await channel.set_permissions(ctx.guild.default_role, send_messages=True)
        embed = nextcord.Embed(
            title="🔒 | Channel Locked", 
            description=f"> **Channel:  {channel.mention}**\n> **Unlocked By:** {ctx.user.mention}",
            color=nextcord.Color.purple()
                )
        embed.set_footer(text="⚠️ | This Message Will Be Deleted In 4 Seconds")
        msg = await ctx.send(embed=embed)
        await asyncio.sleep(4)
        await msg.delete()
    






def setup(bot):
    bot.add_cog(Unlock(bot))