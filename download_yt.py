import sys
import yt_dlp
from pytube import Playlist


def download_audio(link, dir="."):
    ydl_opts_song = {
        "extract_audio": True,
        "format": "bestaudio",
        "outtmpl": dir + "/%(title)s.mp3",
    }
    with yt_dlp.YoutubeDL(ydl_opts_song) as video:
        video.download(link)


def download_playlist(link, dir="."):
    playlist = Playlist(link)
    urls = playlist.video_urls
    len_playlist = len(urls)
    for index, url in enumerate(urls):
        try:
            print(f"Downloading item {index + 1} of {len_playlist}")
            download_audio(url, f"{dir}/{playlist.title}")
            print(f"Item {index + 1} of {len_playlist}: Successfully Downloaded")
        except Exception as e:
            if isinstance(e, KeyboardInterrupt):
                print("\nInterrupção detectada.")
                sys.exit(0)
            print(f"Item {index + 1} of {len_playlist}: Download failed")
