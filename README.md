# SimpleMusicBot
 
pycordを用いた非常にシンプルな音楽botです。<br>
プログラミングを習うにあたり、プログラミングに慣れるために作成しました。<br>
URLからの音楽再生(音楽ファイルへの直リンクまたはYouTubeリンク)または、検索機能を利用したYouTubeからの検索が利用できます。<br>

# 手動インストール(Windows)
1. <a href="https://www.python.org/downloads/">python3</a>、<a href="https://ffmpeg.org/download.html">ffmpeg</a>をインストールしてください。
2. `pip install`を用いて`discord.py`、`yt-dlp`、`configparser`をインストールしてください。
4. <a href="https://github.com/ni-302/SimpleDiscordMusicBot/releases">リリース</a>から`main.py`及び`config.ini`を入手し、任意のディレクトリに、(**2つのファイルは同じディレクトリである必要があります**)置いてください。
5. `config.ini`内の`YOUR_TOKEN_HERE`を、<a href="https://discord.com/developers/applications">Discord Developer Portal</a>にて入手したbotのトークンに置き換えてください。
6. コマンドプロンプトで`py main.py`を実行してください。
7. 終了する際はCtrl+Cキーをご利用ください。

# 手動インストール(Linux)
1. `sudo apt install`を用いて`python3`、`python3-nacl`、`python3-pip`、`ffmpeg`をインストールしてください。
2. `sudo pip install`を用いて`discord.py`、`yt-dlp`、`configparser`をインストールしてください。
3. <a href="https://github.com/ni-302/SimpleDiscordMusicBot/releases">リリース</a>から`main.py`及び`config.ini`を入手し、任意のディレクトリに、(**2つのファイルは同じディレクトリである必要があります**)置いてください。
4. `config.ini`内の`YOUR_TOKEN_HERE`を、<a href="https://discord.com/developers/applications">Discord Developer Portal</a>にて入手したbotのトークンに置き換えてください。
5. bashなどで`python3 main.py`を実行してください。
6. 終了する際はCtrl+Cキーをご利用ください。

# コマンド
- `&play [URL]`   ・・・・・URL内の音楽を再生します。
- `&search [キーワード]`   ・・・・・YouTubeでキーワード検索を行い、ヒットした一番上の曲を再生します。
- `&connect`   ・・・・・Botをボイスチャンネルに入室させます。&playや&searchを実行した際に自動的に同等の処理が行われるため、特別な際を除いて使用する必要はありません。
- `&stop`   ・・・・・再生を停止し、Botをボイスチャンネルから退室させます。
- `&vol`   ・・・・・音量を調節します。初期値は100%です。
- `&skip`   ・・・・・今再生している曲をスキップします。
