import nextcord
from nextcord.ext import commands

class Logger(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.get_logging_channel(member.guild)
        if channel:
            await channel.send(f':inbox_tray: {member} joined the server.')

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = self.get_logging_channel(member.guild)
        if channel:
            await channel.send(f':outbox_tray: {member} left the server.')

    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        if before.author.bot:
            return
        channel = self.get_logging_channel(before.guild)
        if channel:
            await channel.send(
                f'✏️ Message edited in {before.channel.mention}:\n**Before:** {before.content}\n**After:** {after.content}'
            )

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        if message.author.bot:
            return
        channel = self.get_logging_channel(message.guild)
        if channel:
            await channel.send(
                f'🗑️ Message deleted in {message.channel.mention}:\n**Author:** {message.author}\n**Content:** {message.content}'
            )

    @commands.Cog.listener()
    async def on_guild_role_create(self, role):
        channel = self.get_logging_channel(role.guild)
        if channel:
            await channel.send(f'✨ Role created: {role.name}')

    @commands.Cog.listener()
    async def on_guild_role_delete(self, role):
        channel = self.get_logging_channel(role.guild)
        if channel:
            await channel.send(f'🚫 Role deleted: {role.name}')

    @commands.Cog.listener()
    async def on_guild_role_update(self, before, after):
        channel = self.get_logging_channel(before.guild)
        if channel:
            await channel.send(f'🔄 Role updated: {before.name} -> {after.name}')

    @commands.Cog.listener()
    async def on_guild_channel_create(self, channel):
        log_channel = self.get_logging_channel(channel.guild)
        if log_channel:
            await log_channel.send(f'📂 Channel created: {channel.name} ({channel.type})')

    @commands.Cog.listener()
    async def on_guild_channel_delete(self, channel):
        log_channel = self.get_logging_channel(channel.guild)
        if log_channel:
            embed =  nextcord.Embed(
                title='🗑️ | Channel deleted', 
                description=f'> **Name:** ``{channel.name}``\n> **Type:** ``{channel.type}``\n> **Mention:** {channel.mention}\n> **ID:** ``{channel.id}``',
                color=nextcord.Color.purple()
                )

            await log_channel.send(f'🗑️ Channel deleted: {channel.name} ({channel.type})')

    def get_logging_channel(self, guild):
        return nextcord.utils.get(guild.text_channels, id='1292285058652307516')

def setup(bot):
    bot.add_cog(Logger(bot))
