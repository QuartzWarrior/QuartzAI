import nextcord
from nextcord.ext import commands
import asyncio
from utils.perms import perms_prefix
from utils.cooldown import cooldown_prefix
class Purge(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='purge')
    @perms_prefix(name="manage_messages")
    @cooldown_prefix(seconds=5)
    async def purge(self, ctx, amount: int):
        if amount < 1:
            await ctx.send("You must delete at least one message.")
            return

        deleted_messages = await ctx.channel.purge(limit=amount + 1)
        user_counts = {}
        for message in deleted_messages:
            if message.author not in user_counts:
                user_counts[message.author] = 1
            else:
                user_counts[message.author] += 1
        response_embed = nextcord.Embed(
            title='Purge Complete',
            description=f"> **Deleted {len(deleted_messages)} Messages**\n",
            color=nextcord.Color.purple()
        )
        for user, count in user_counts.items():
            response_embed.add_field(name=user.name, value=f"{count} message(s)", inline=False)
        response_message = await ctx.send(embed=response_embed)
        await asyncio.sleep(3)
        await response_message.delete()


def setup(bot):
    bot.add_cog(Purge(bot))