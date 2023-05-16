from yt_dlp import YoutubeDL
from moviepy.editor import *
import mimetypes


def youtube(URLS):
    """ydl_opts = {
        "ignoreerrors": True
    }

    with YoutubeDL(ydl_opts) as ydl:
        res = ydl.extract_info(url, download=False)"""


    ydl_audio_opts = {
        'ignoreerrors': True,
        'format': 'mp3/bestaudio/best',
        'postprocessors': [{  
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',}]
    }

    with YoutubeDL(ydl_audio_opts) as ydl:
        ydl.download(URLS)


    """videoclip = VideoFileClip("video.mp4")
    audioclip = AudioFileClip("audio.mp3")
    output_video = videoclip.set_audio(audioclip)
    output_video.write_videofile(res['id'] + ".mp4")"""


if __name__ == "__main__":
    url = input("URL: ")
    video_name = []
    youtube(url)