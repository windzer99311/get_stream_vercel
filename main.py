from fastapi import FastAPI
import requests
app = FastAPI()
@app.get("/search")
def get_video():
    url = "https://www.clipto.com/api/youtube"
    payload = {
        "url": "https://youtu.be/jQdDpRTVe9k?si=tbXO9xj1xakNgQhn"
    }

    r = requests.post(url, json=payload)
    print(r.status_code)
    return r.text
