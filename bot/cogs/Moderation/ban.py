import nextcord
from nextcord.ext import commands
from utils.perms import perms_prefix

class Ban(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @perms_prefix(name="ban_members")
    async def ban(self, ctx, member: nextcord.Member, *, reason=None):
        if ctx.author == member:
            await ctx.send(embed=nextcord.Embed(
                title="Ban Error",
                description="> **You Cannot Ban Yourself!**",
                color=nextcord.Color.red()
            ))
            return
        if member.top_role >= ctx.author.top_role:
            await ctx.send(embed=nextcord.Embed(
                title="Ban Error",
                description="> **You Cannot Ban A Member With A Higher Or Equal Role To Yourself.**",
                color=nextcord.Color.red()
            ))
            return
        if member.top_role >= ctx.guild.me.top_role:
            await ctx.send(embed=nextcord.Embed(
                title="Ban Error",
                description="> **I Cannot Ban A Member With A Higher Or Equal Role Than Mine.**",
                color=nextcord.Color.red()
            ))
            return
        try:
            await member.ban(reason=reason)
            await ctx.send(embed=nextcord.Embed(
                title="Member Banned",
                description=f"> **{member.mention} Has Been Banned By {ctx.author.mention} For: {reason or 'No Reason Provided.'}**",
                color=nextcord.Color.green()
            ))
        except nextcord.Forbidden:
            await ctx.send(embed=nextcord.Embed(
                title="Ban Error",
                description="> **An Error Occured While Trying To Ban This Member.**",
                color=nextcord.Color.red()
            ))
        except Exception as e:
            await ctx.send(embed=nextcord.Embed(
                title="Ban Error",
                description=f"> **An Error Occurred While Trying To Ban This Member.**",
                color=nextcord.Color.red()
            ))

def setup(bot):
    bot.add_cog(Ban(bot))