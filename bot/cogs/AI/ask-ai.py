import nextcord
from nextcord.ext import commands
from nextcord import SlashOption, Interaction, Embed
from nextcord.ui import View, Button
from g4f.client import Client

class Ask_ai(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(
        name="ask-ai",
        description="Ask AI A Question"
    )
    async def ask_ai(
        self,
        ctx: Interaction,
        prompt: str,
        model: str = SlashOption(
            name="model",
            description="Select The Model To Use",
            choices={"GPT 4o": "gpt-4o", "GPT 4o Mini": "gpt-4o-mini", "GPT 4": "gpt-4", "GPT 4 Turbo": "gpt-4-turbo", "Gemini Pro": "gemini-pro", "Claude 3 Haiku": "claude-3-haiku", "Claude 3 Sonnet": "claude-3-sonnet"}
        ),
    ):
        e1 = Embed(
            title="AI - Ask AI",
            description="Please Wait...",
            color=nextcord.Color.purple()
        )
        msg = await ctx.send(embed=e1)

        client = Client()
        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": f"{prompt}"}],
        )
        content = response.choices[0].message.content

        page_length = 1800
        pages = [content[i:i + page_length] for i in range(0, len(content), page_length)]
        total_pages = len(pages)

        e2 = Embed(
            title="AI - Ask AI",
            description=f"> **Model:** {model}\n> **Prompt:**  {prompt}\n\n> **Response:**\n{pages[0]}",
            color=nextcord.Color.purple()
        )
        e2.set_footer(text=f"Page: 1 | Total Pages: {total_pages}")

        if total_pages == 1:
            await msg.edit(embed=e2)
            return

        class Paginator(View):
            def __init__(self):
                super().__init__()
                self.current_page = 0
                self.previous_button = Button(label="Previous", style=nextcord.ButtonStyle.secondary, disabled=True)
                self.previous_button.callback = self.go_previous
                self.next_button = Button(label="Next", style=nextcord.ButtonStyle.secondary, disabled=(total_pages == 1))
                self.next_button.callback = self.go_next
                self.add_item(self.previous_button)
                self.add_item(self.next_button)

            async def go_previous(self, interaction: Interaction):
                if self.current_page > 0:
                    self.current_page -= 1
                    e2.description = f"> **Model:** {model}\n> **Prompt:**  {prompt}\n\n> **Response:**\n{pages[self.current_page]}"
                    e2.set_footer(text=f"Page: {self.current_page + 1} | Total Pages: {total_pages}")
                    self.update_buttons()
                    await interaction.response.edit_message(embed=e2, view=self)

            async def go_next(self, interaction: Interaction):
                if self.current_page < total_pages - 1:
                    self.current_page += 1
                    e2.description = f"> **Model:** {model}\n> **Prompt:**  {prompt}\n\n> **Response:**\n{pages[self.current_page]}"
                    e2.set_footer(text=f"Page: {self.current_page + 1} | Total Pages: {total_pages}")
                    self.update_buttons()
                    await interaction.response.edit_message(embed=e2, view=self)

            def update_buttons(self):
                self.previous_button.disabled = (self.current_page == 0)
                self.next_button.disabled = (self.current_page == total_pages - 1)

        view = Paginator()
        await msg.edit(embed=e2, view=view)

def setup(bot):
    bot.add_cog(Ask_ai(bot))
