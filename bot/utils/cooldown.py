import time
import asyncio
from functools import wraps
import nextcord

cooldowns = {}

def cooldown_prefix(seconds):
    def decorator(func):
        @wraps(func)
        async def wrapper(self, ctx, *args, **kwargs):
            user_id = ctx.author.id
            current_time = time.time()
            if user_id in cooldowns:
                last_used = cooldowns[user_id]
                time_since_last_used = current_time - last_used

                if time_since_last_used < seconds:
                    remaining_time = seconds - time_since_last_used
                    future_timestamp = int(current_time + remaining_time)
                    embed = nextcord.Embed(
                        title="Cooldown",
                        description=f"Command is on cooldown. Try again <t:{future_timestamp}:R>.",
                        color=nextcord.Color.red()
                    )
                    cooldown_message = await ctx.reply(embed=embed)
                    await asyncio.sleep(remaining_time)
                    await cooldown_message.delete()
                    return

            cooldowns[user_id] = current_time
            return await func(self, ctx, *args, **kwargs)

        return wrapper
    return decorator
    
def cooldown_slash(seconds):
    def decorator(func):
        @wraps(func)
        async def wrapper(self, ctx, *args, **kwargs):
            user_id = ctx.user.id
            current_time = time.time()
            if user_id in cooldowns:
                last_used = cooldowns[user_id]
                time_since_last_used = current_time - last_used

                if time_since_last_used < seconds:
                    remaining_time = seconds - time_since_last_used
                    future_timestamp = int(current_time + remaining_time)
                    embed = nextcord.Embed(
                        title="Cooldown",
                        description=f"Command is on cooldown. Try again <t:{future_timestamp}:R>.",
                        color=nextcord.Color.red()
                    )
                    cooldown_message = await ctx.send(embed=embed)
                    await asyncio.sleep(remaining_time)
                    await cooldown_message.delete()
                    return

            cooldowns[user_id] = current_time
            return await func(self, ctx, *args, **kwargs)

        return wrapper
    return decorator