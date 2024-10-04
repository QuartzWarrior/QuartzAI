import nextcord
from nextcord.ext import commands
import colorama
from colorama import Fore, Style, init
from datetime import datetime



class on_ready(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_ready(self):
        time = datetime.now().strftime("[%H:%M:%S]")
        print(f"{Fore.RESET}{time}{Fore.BLUE} [DEBUG] {Fore.BLUE}[CLIENT]{Fore.MAGENTA} Client Is Online{Fore.RESET}")
   
        
        
def setup(bot):
    bot.add_cog(on_ready(bot))