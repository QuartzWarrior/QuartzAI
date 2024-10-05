import nextcord
from nextcord.ext import commands
import yt_dlp
import os
import asyncio

# WARNING | Might Be Unstable, Use At Your Own Risk

class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.voice_clients = {}
        self.music_queue = {}
        self.download_folder = "yt_dlp"

        if not os.path.exists(self.download_folder):
            os.makedirs(self.download_folder)

    @commands.command(name="play", help="Plays a song from a given URL or searches YouTube.")
    async def play(self, ctx, *, query: str):
        if not ctx.author.voice:
            embed = nextcord.Embed(
                title="Error",
                description="> **You Must  Be Connected To A Voice Channel To Play Music.**",
                color=nextcord.Color.red()
            )
            await ctx.send(embed=embed)
            return

        voice_channel = ctx.author.voice.channel

        if ctx.voice_client:
            if ctx.voice_client.channel != voice_channel:
                embed = nextcord.Embed(
                    title="Error",
                    description="> **I'm Already Connected To A Voice Channel**",
                    color=nextcord.Color.red()
                )
                await ctx.send(embed=embed)
                return
        else:
            await voice_channel.connect()

        vc = ctx.voice_client

        if not self.music_queue.get(ctx.guild.id):
            self.music_queue[ctx.guild.id] = []

        def is_url(string):
            return string.startswith("http://") or string.startswith("https://")

        if is_url(query):
            url = query
        else:
            url = await self.search_youtube(query)

        if not url:
            embed = nextcord.Embed(
                title="Error",
                description="> **No Results Found**",
                color=nextcord.Color.red()
            )
            await ctx.send(embed=embed)
            return

        file_path = await self.download_song(url)
        if not file_path:
            embed = nextcord.Embed(
                title="Error",
                description="> **Failed To Download Song**",
                color=nextcord.Color.red()
            )
            await ctx.send(embed=embed)
            return

        self.music_queue[ctx.guild.id].append(file_path)

        if not vc.is_playing():
            e2 = nextcord.Embed(
                title="🔍 | Searching",
                description=f"> **Your Song ({query}) Is Being Searched, Please Wait...**",
                color=nextcord.Color.purple()
            )
            await ctx.reply(embed=e2)
            await self.play_next(ctx)

    async def play_next(self, ctx):
        if self.music_queue[ctx.guild.id]:
            vc = ctx.voice_client
            file_path = self.music_queue[ctx.guild.id].pop(0)
            audio_source = nextcord.FFmpegPCMAudio(file_path)
            song_name = os.path.splitext(os.path.basename(file_path))[0]
            vc.play(nextcord.PCMVolumeTransformer(audio_source), after=lambda e: self.bot.loop.create_task(self.check_queue(ctx)))
            embed = nextcord.Embed(
                title="🎵 | Now Playing",
                description=f"> **{song_name}**",
                color=nextcord.Color.purple()
            )
            embed.set_footer(text=f"Requested By: {ctx.author.name}", icon_url=ctx.author.avatar.url)
            await ctx.send(embed=embed)

    async def check_queue(self, ctx):
        if self.music_queue[ctx.guild.id]:
            await self.play_next(ctx)
        else:
            embed = nextcord.Embed(
                title="👋 | Queue Empty",
                description="> **No Songs In Queue, Leaving VC.**",
                color=nextcord.Color.purple()
            )
            await ctx.send(embed=embed)

    async def search_youtube(self, query):
        ydl_opts = {
            'format': 'bestaudio',
            'quiet': True,
            'default_search': 'ytsearch1',
            'noplaylist': True,
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(query, download=False)
            if 'entries' in info:
                return info['entries'][0]['webpage_url']
            else:
                return None

    async def download_song(self, url):
        ydl_opts = {
            'format': 'bestaudio/best',
            'quiet': True,
            'outtmpl': os.path.join(self.download_folder, '%(title)s.%(ext)s'),
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=True)
                filename = ydl.prepare_filename(info)
                base, _ = os.path.splitext(filename)
                return f"{base}.mp3"
        except Exception as e:
            print(f"Error occurred while downloading: {e}")
            return None

def setup(bot):
    bot.add_cog(Music(bot))
