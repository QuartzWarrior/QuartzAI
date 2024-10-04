import nextcord
from nextcord.ext import commands
from nextcord import SlashOption
from g4f.client import Client
import json

class Ask_ai(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(name="ask-ai", description="Ask AI A Question")
    async def ask_ai(
        self,
        ctx: nextcord.Interaction,
        prompt: str,
        model: str = SlashOption(
            name="model",
            description="Select The Model To Use",
            choices={"GPT-4o": "gpt-4o"}),
    ):
        e1 = nextcord.Embed(
                               title="AI - Ask AI",
                               description="Please Wait...",
                               color=nextcord.Color.purple())

        msg  = await ctx.send(embed=e1)


        client = Client()
        response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": f"{prompt}"}],
    )
        e2 = nextcord.Embed(
                               title="AI - Ask AI",
                               description=f"> **Model:** {model}\n> **Prompt:**  {prompt}\n> **Response:** {response.choices[0].message.content}",
                               color=nextcord.Color.purple()
                               )
        await msg.edit(embed=e2)

        

def setup(bot):
    bot.add_cog(Ask_ai(bot))