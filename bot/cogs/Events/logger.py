import nextcord
from nextcord.ext import commands


LOG_ID = 1292285058652307516

class Logger(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.get_logging_channel(member.guild)
        if channel:
            embed = nextcord.Embed(
                title='👤 | Member Joined',
                description=f'> **Name:** {member.name}\n> **ID:** `{member.id}`\n> **Account Created:** {member.created_at.strftime("%Y-%m-%d %H:%M:%S")}',
                color=nextcord.Color.green()
            )
            embed.set_thumbnail(url=member.avatar.url if member.avatar else member.default_avatar.url)
            await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = self.get_logging_channel(member.guild)
        if channel:
            embed = nextcord.Embed(
                title='👤 | Member Left',
                description=f'> **Name:** {member.name}\n> **ID:** `{member.id}`\n> **Joined At:** {member.joined_at.strftime("%Y-%m-%d %H:%M:%S") if member.joined_at else "N/A"}',
                color=nextcord.Color.red()
            )
            embed.set_thumbnail(url=member.avatar.url if member.avatar else member.default_avatar.url)
            await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        if before.author.bot:
            return
        channel = self.get_logging_channel(before.guild)
        if channel:
            embed = nextcord.Embed(
                title='✏️ | Message Edited',
                description=f'> **Author:** {before.author.mention}\n> **Channel:** {before.channel.mention}\n> **Before:** {before.content}\n> **After:** {after.content}\n> **Message ID:** `{before.id}`',
                color=nextcord.Color.orange()
            )
            await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        if message.author.bot:
            return
        channel = self.get_logging_channel(message.guild)
        if channel:
            embed = nextcord.Embed(
                title='🗑️ | Message Deleted',
                description=f'> **Author:** {message.author.mention}\n> **Channel:** {message.channel.mention}\n> **Content:** {message.content}\n> **Message ID:** `{message.id}`',
                color=nextcord.Color.dark_red()
            )
            await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_guild_role_create(self, role):
        channel = self.get_logging_channel(role.guild)
        if channel:
            embed = nextcord.Embed(
                title='✨ | Role Created',
                description=f'> **Name:** `{role.name}`\n> **ID:** `{role.id}`',
                color=nextcord.Color.green()
            )
            await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_guild_role_delete(self, role):
        channel = self.get_logging_channel(role.guild)
        if channel:
            embed = nextcord.Embed(
                title='🚫 | Role Deleted',
                description=f'> **Name:** `{role.name}`\n> **ID:** `{role.id}`',
                color=nextcord.Color.red()
            )
            await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_guild_role_update(self, before, after):
        channel = self.get_logging_channel(before.guild)
        if channel:
            embed = nextcord.Embed(
                title='🔄 | Role Updated',
                description=f'> **Before:** `{before.name}`\n> **After:** `{after.name}`\n> **ID:** `{before.id}`',
                color=nextcord.Color.blue()
            )
            await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_guild_channel_create(self, channel):
        log_channel = self.get_logging_channel(channel.guild)
        if log_channel:
            embed = nextcord.Embed(
                title='📂 | Channel Created',
                description=f'> **Name:** `{channel.name}`\n> **Type:** `{channel.type}`\n> **Mention:** {channel.mention}\n> **ID:** `{channel.id}`',
                color=nextcord.Color.green()
            )
            await log_channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_guild_channel_delete(self, channel):
        log_channel = self.get_logging_channel(channel.guild)
        if log_channel:
            embed = nextcord.Embed(
                title='🗑️ | Channel Deleted',
                description=f'> **Name:** `{channel.name}`\n> **Type:** `{channel.type}`\n> **ID:** `{channel.id}`',
                color=nextcord.Color.red()
            )
            await log_channel.send(embed=embed)

    def get_logging_channel(self, guild):
        return guild.get_channel(LOG_ID)

def setup(bot):
    bot.add_cog(Logger(bot))

