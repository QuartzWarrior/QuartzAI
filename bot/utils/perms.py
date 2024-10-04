import nextcord
from nextcord.ext import commands

async def send_permission_error(ctx: commands.Context, embed: nextcord.Embed):
    await ctx.send(embed=embed)

def perms_slash(name: str):
    def predicate(ctx: commands.Context):
        if not ctx.guild:
            return False
        user_perms = getattr(ctx.author.guild_permissions, name, False)
        bot_perms = getattr(ctx.guild.me.guild_permissions, name, False)

        if not user_perms:
            user_embed = nextcord.Embed(
                title="Permissions Required",
                description=f"> **You Need The `{name.replace('_', ' ').title()}` Permission To Use This Command.**",
                color=nextcord.Color.red()
            )
            user_embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar.url)
            ctx.bot.loop.create_task(send_permission_error(ctx, user_embed))  
            return False

        if not bot_perms:
            bot_embed = nextcord.Embed(
                title="Bot Permission Error",
                description=f"> **I Need The `{name.replace('_', ' ').title()}` Permission To Execute This Command.**",
                color=nextcord.Color.red()
            )
            bot_embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar.url)
            ctx.bot.loop.create_task(send_permission_error(ctx, bot_embed))
            return False

        return True

    return commands.check(predicate)

def perms_prefix(name: str):
    def predicate(ctx: commands.Context):
        if not ctx.guild:
            return False
        user_perms = getattr(ctx.author.guild_permissions, name, False)
        bot_perms = getattr(ctx.guild.me.guild_permissions, name, False)

        if not user_perms:
            user_embed = nextcord.Embed(
                title="Permissions Required",
                description=f"> **You Need The `{name.replace('_', ' ').title()}` Permission To Use This Command.**",
                color=nextcord.Color.red()
            )
            user_embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar.url)
            ctx.bot.loop.create_task(send_permission_error(ctx, user_embed))  
            return False

        if not bot_perms:
            bot_embed = nextcord.Embed(
                title="Bot Permission Error",
                description=f"> **I Need The `{name.replace('_', ' ').title()}` Permission To Execute This Command.**",
                color=nextcord.Color.red()
            )
            bot_embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar.url)
            ctx.bot.loop.create_task(send_permission_error(ctx, bot_embed))
            return False

        return True

    return commands.check(predicate)