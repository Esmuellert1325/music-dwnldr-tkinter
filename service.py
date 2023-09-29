from pytube import Search
from pytube import YouTube
from os import getlogin
import re

# Get video by url
def get_video_by_url(url :str):
    pattern = r"v=([A-Za-z0-9_-]+)"
    viewkey = ""
    try:
        match = re.search(pattern, url)
        viewkey = match.group(1)
    except:
        print("Error occured")
    
    try:
        user_name = getlogin()
        yt = YouTube(f"https://www.youtube.com/watch?v={viewkey}")
        streams = yt.streams.filter(only_audio=True)
        stream = streams.get_by_itag(streams[0].itag)
        stream.download(f"C:/Users/{user_name}/Downloads", f"{yt.title}.mp3")
    except:
        print("Error occured")
