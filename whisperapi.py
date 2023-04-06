import openai
from yt_dlp import YoutubeDL
import os
import mimetypes
import whisper


openai.api_key = "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"

def youtube(URLS):
    
    ydl_opts = {
        'format': 'mp3/bestaudio/best',
        'ignoreerrors': True,

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

    with open(f"{video}.txt", "w", encoding="UTF-8") as file:
        file.write(transcript["text"])
        file.close()
    os.remove(f"{video}.mp3")


if __name__ == "__main__":
    url = input("URL: ")
    video_name = []
    youtube(url)
    for video in video_name:
        text(video)
