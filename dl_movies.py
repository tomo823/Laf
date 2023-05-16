from yt_dlp import YoutubeDL
from moviepy.editor import *
import mimetypes


def youtube(URLS):

    ydl_movies_opts = {
        'ignoreerrors': True,
        'outtmpl': 'video.mp4',
        'format': 'bestvideo/best'
    }
        
    with YoutubeDL(ydl_movies_opts) as ydl:
        error_code = ydl.download(URLS)


if __name__ == "__main__":
    url = input("URL: ")
    video_name = []
    youtube(url)