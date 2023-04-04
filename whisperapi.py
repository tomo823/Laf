import openai
from yt_dlp import YoutubeDL
import os
import mimetypes
import whisper
import json


openai.api_key = "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"

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
            file_name = files.split(".mp3")
            video_name.append(file_name[0])

def text(video):
    f = open(f"{video}.mp3", "rb")
    transcript = openai.Audio.transcribe("whisper-1", f)

    with open(f"{video}", "w", encoding="UTF-8") as file:
        file.write(transcript["text"])
        file.close()
    os.remove(f"{video}.mp3")


if __name__ == "__main__":
    url = input("URL: ")
    video_name = []
    youtube(url)
    for video in video_name:
        text(video)
