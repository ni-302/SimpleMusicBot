# ライブラリをインポート
import discord
from yt_dlp import YoutubeDL
from discord.ext import commands
import configparser
import os

# configparserの設定
config = configparser.ConfigParser()
path = 'config.ini'
is_file = os.path.isfile(path)
if is_file:
    config.read('config.ini')
else:
    print(f'[警告]config.iniが見つかりません!')

# トークンの設定
TOKEN = config.get('config', 'token')

# クライアントの設定と接頭辞の設定
client = commands.Bot(command_prefix='&', intents=discord.Intents.all(), help_command=None)

# キューを保存するところ
queue = []

# yt-dlpのオプションの設定
options = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192'
            }]
        }

# 関数の設定
def next(vc):
    if queue:
        with YoutubeDL(options) as opt:
            info = opt.extract_info(queue.pop(0), download=False)
            vc.play(discord.FFmpegPCMAudio(info['url']), after=lambda e: next(vc))
            vc.source = discord.PCMVolumeTransformer(vc.source)
            vc.source.volume = 0.15
    else:
        vc.stop()

# コマンドの設定
@client.command()
async def play(ctx, url: str):
    voice_channel = ctx.author.voice.channel
    vc = ctx.voice_client
    if vc is None:
        vc = await voice_channel.connect()
        queue.append(url)
        next(vc)
        await ctx.channel.send(f'{url} を再生します。')
    else:
        queue.append(url)
        await ctx.channel.send(f'キューに {url} を追加しました。')
        if not vc.is_playing():
            next(vc)

@client.command()
async def search(ctx, *, query: str):
    if ctx.voice_client is None:
        voice_channel = ctx.author.voice.channel
        await voice_channel.connect()
    vc = ctx.voice_client
    with YoutubeDL(options) as opt:
        songname = {query}
        query = f'ytsearch1:{query}'
        info = opt.extract_info(query, download=False)
        url = info['entries'][0]['url']
        queue.append(url)
        await ctx.channel.send(f'{songname} をキューに追加しました。')
        if not vc.is_playing():
            next(vc)

@client.command()
async def help(ctx):
    help_message =  "使い方: &コマンド\n\n" \
                    "&play [URL] - URL の音楽を再生する\n" \
                    "&search [キーワード] - キーワードで検索した最初の動画の音楽を再生する\n" \
                    "&stop - 再生を停止してボイスチャンネルから退出する\n" \
                    "&connect - ボイスチャンネルに接続する\n" \
                    "&vol [パーセント] - 音量を変更する\n" \
                    "&jazz - Relaxing Jazz Piano Radio - Slow Jazz Music - 24/7 Live Stream - Music For Work & Studyを再生します。(終了予定のないライブストリーミングを拾うので終了したいときは&stopか&skipをご利用ください。)\n"\
                    "&lofi - lofi hip hop radio - beats to relax/study toを再生します。(終了予定のないライブストリーミングを拾うので終了したいときは&stopか&skipをご利用ください。)\n"
    await ctx.send(help_message)

@client.command()
async def stop(ctx):
    vc = ctx.voice_client
    if vc is not None:
        vc.stop()
        await vc.disconnect()
        await ctx.channel.send(f'再生を停止しました。')

@client.command()
async def connect(ctx):
    if ctx.voice_client is not None:
        return
    voice_channel = ctx.author.voice.channel
    await voice_channel.connect()
    await ctx.send(f'{voice_channel.name} に接続しました。')

@client.command()
async def vol(ctx, volume: float):
    vc = ctx.voice_client
    if vc is not None:
        vc.source.volume = volume / 100 * 0.15
        await ctx.channel.send(f'音量を {volume} %に設定します。')

@client.command()
async def skip(ctx):
    vc = ctx.voice_client
    if vc is not None:
        vc.stop()
        await ctx.channel.send(f'スキップしました。')

@client.command()
async def jazz(ctx):
    if ctx.voice_client is None:
        voice_channel = ctx.author.voice.channel
        await voice_channel.connect()
    vc = ctx.voice_client
    query = "Relaxing Jazz Piano Radio - Slow Jazz Music - 24/7 Live Stream - Music For Work & Study"
    with YoutubeDL(options) as opt:
        query = f'ytsearch1:{query}'
        info = opt.extract_info(query, download=False)
        url = info['entries'][0]['url']
        queue.append(url)
        await ctx.channel.send(f'Relaxing Jazz Piano Radio - Slow Jazz Music - 24/7 Live Stream - Music For Work & Studyをキューに追加しました。')
        if not vc.is_playing():
            next(vc)

@client.command()
async def lofi(ctx):
    if ctx.voice_client is None:
        voice_channel = ctx.author.voice.channel
        await voice_channel.connect()
    vc = ctx.voice_client
    query = "lofi hip hop radio - beats to relax/study to"
    with YoutubeDL(options) as opt:
        query = f'ytsearch1:{query}'
        info = opt.extract_info(query, download=False)
        url = info['entries'][0]['url']
        queue.append(url)
        await ctx.channel.send(f'lofi hip hop radio - beats to relax/study toをキューに追加しました。')
        if not vc.is_playing():
            next(vc)

# BOTを実行
client.run(TOKEN)