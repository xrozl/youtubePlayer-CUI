import os
import platform
import youtube_dl
from playsound import playsound
from typing import Any

def playMusic(music: str) -> None:
    ss: str = getOS()
    if ss == "Windows":
       playsound(music)
    elif ss == "Linux":
        os.system("mpg123 " + music)
    elif ss == "Darwin":
        os.system("afplay " + music)

def getOS() -> str:
    return platform.system()

def main() -> None:
    while True:
        url: str = input("Enter the url of the youtube video: ")
        if url == "exit":
            break
        else:
            ydl: Any = youtube_dl.YoutubeDL({'outtmpl': '%(id)s%(ext)s',
                                        'postprocessors': [{
                                        'key': 'FFmpegExtractAudio',
                                        'preferredcodec': 'mp3',
                                        'preferredquality': '192',
                                        }]})
            with ydl:
                result: Any = ydl.extract_info(url, download=True)
            playMusic(result['id'] + ".mp3")

if __name__ == "__main__":
    main()
