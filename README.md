# SimpleDiscordMusicBot
 
pycordを用いた非常にシンプルな音楽botです。<br>
プログラミングを習うにあたり、プログラミングに慣れるために作成しました。<br>
URLからの音楽再生(音楽ファイルへの直リンクまたはYouTubeリンク)または、検索機能を利用したYouTubeからの検索が利用できます。<br>

# 手動インストール
1. <a href="https://www.python.org/downloads/">python3</a>、<a href="https://ffmpeg.org/download.html">ffmpeg</a>をインストールしてください。
2. pip等を用いて<a href="https://docs.pycord.dev/en/stable/">pycord</a>、<a href="https://github.com/yt-dlp/yt-dlp">yt-dlp</a>、configparserを入手してください。
 - <u>discord.pyでは正常に動作しないのでご注意ください。</u>
4. <a href="https://github.com/ni-302/SimpleDiscordMusicBot/releases">リリース</a>からmain.py及びconfig.iniを入手し、任意のディレクトリに、(**2つのファイルは同じディレクトリである必要があります**)置いてください。
5. config.ini内のYOUR_TOKEN_HEREを、<a href="https://discord.com/developers/applications">Discord Developer Portal</a>にて入手したbotのトークンに置き換えてください。
6. コマンドプロンプトやbashなどでmain.pyを実行してください。
   - Windowsの方はmain.pyのディレクトリでコマンドプロンプトなどを開き、`py main.py`を実行してください。
   - Linuxの方はmain.pyのディレクトリでbashなどを開き、`python3 main.py`を実行してください。
7. 終了する際はCtrl+Cキーをご利用ください。

# コマンド
- `&play [URL]`   ・・・・・URL内の音楽を再生します。
- `&search [キーワード]`   ・・・・・YouTubeでキーワード検索を行い、ヒットした一番上の曲を再生します。
- `&connect`   ・・・・・Botをボイスチャンネルに入室させます。&playや&searchを実行した際に自動的に同等の処理が行われるため、特別な際を除いて使用する必要はありません。
- `&stop`   ・・・・・再生を停止し、Botをボイスチャンネルから退室させます。
- `&vol`   ・・・・・音量を調節します。初期値は100%です。
- `&skip`   ・・・・・今再生している曲をスキップします。
