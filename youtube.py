
from pytube import YouTube, Playlist    

p = Playlist("https://youtube.com/playlist?list=PLGBKsNyGY-afmc5ff3n1HOYGTmZO1xJGw&si=CoTtAqqVUn6upBJ4")

for video in p.videos:
    print(f"Downloading: {video.title}")
    video.streams.get_highest_resolution().download()