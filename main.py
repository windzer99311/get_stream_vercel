from fastapi import FastAPI
from pytubefix import YouTube
app = FastAPI()
@app.get("/search")
def get_stream(url: str):
    yt = YouTube(url)
    link = yt.streams.first().url
    return link
