import os
import glob
import asyncio
import colorama
from colorama import Fore, Style, init
from datetime import datetime



def load_cogs(bot):
    cogs_path = 'cogs'
    for filename in glob.glob(os.path.join(cogs_path, '**/*.py'), recursive=True):
        if os.path.dirname(filename) == cogs_path:
            continue
        cog_name = os.path.splitext(os.path.relpath(filename, cogs_path))[0].replace(os.sep, '.')
        cog_module = f"{cogs_path}.{cog_name}"
        try:
            bot.load_extension(cog_module)
            time = datetime.now().strftime("[%H:%M:%S]")
            print(f'{Style.BRIGHT}{time}{Fore.LIGHTBLUE_EX} [DEBUG] {Fore.BLUE}[COGS] {Fore.MAGENTA}{cog_module}{Fore.RESET}')
        except Exception as e:
            print(f'Failed: {cog_module} {e}')