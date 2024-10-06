import nextcord
from nextcord.ext import commands
from nextcord import SlashOption
from g4f.client import Client

class Imagine(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(name="imagine", description="Create Images Using AI")
    async def imagine(self, 
                      ctx: nextcord.Interaction, 
                      prompt: str = SlashOption(
                          description="Prompt For The Image "), 
                      model: str = SlashOption(
                          description="Select A Model To Use",
                          choices={"Dall E":"dalle", "Dall E 2":"dalle-2", "Dall E 3":"dalle-3", "Gemini":"gemini",}),
                    ):
        try:

         await ctx.response.defer()
         client = Client()
         response = await client.images.async_generate(
            prompt=prompt, 
            model=model
            )
         image_url = response.data[0].url
         embed = nextcord.Embed(
            title="Generated Image",
            description=f"> **Prompt:** {prompt}\n> **Model:** {model}",
            color=nextcord.Color.purple()
         )
         embed.set_image(url=image_url)
         await ctx.followup.send(embed=embed)
        except Exception as e:
           embed = nextcord.Embed(
              title="Error",
              description=f"> **An Unknown Error Has Occurred Whilst Trying To Generate Your Image**",
              color=nextcord.Color.red()
           )
           await ctx.followup.send(embed=embed)
   








def setup(bot):
    bot.add_cog(Imagine(bot))