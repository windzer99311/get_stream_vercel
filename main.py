from fastapi import FastAPI
import requests
app = FastAPI()
@app.get("/search")
def get_stream(url: str):
    api = "https://www.clipto.com/api/youtube"
    payload = {
        "url": url
    }
    r = requests.post(api, json=payload)
    for item in r.json()["medias"]:
        if item["itag"] == 139:
            stream = item["url"]
            return {
                "stream": stream
            }
