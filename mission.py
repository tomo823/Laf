
from yt_dlp import YoutubeDL
import os
import mimetypes
import whisper


def youtube(URLS):
    
    ydl_opts = {
        'format': 'mp3/bestaudio/best',

        'postprocessors': [{  
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
        }]
    }

    with YoutubeDL(ydl_opts) as ydl:
        error_code = ydl.download(URLS)
        
    for files in os.listdir("."):
        if mimetypes.guess_type(files)[0] == "audio/mpeg":
            os.rename(files, "test.mp3")


def text():
    model = whisper.load_model("medium",)
    result = model.transcribe("test.mp3", verbose=True, language="ja")

    with open("contents.txt", "w", encoding="UTF-8") as file:
        file.write(result["text"])
        file.close()

    os.remove("test.mp3")


if __name__ == "__main__":
    url = input("URL: ")
    youtube(url)
    text()