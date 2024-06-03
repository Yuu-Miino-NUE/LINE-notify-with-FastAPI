import os
from fastapi import FastAPI
from dotenv import load_dotenv

import requests

app = FastAPI()
load_dotenv(dotenv_path=os.path.join("conf", ".env"))
token = os.getenv("LINE_NOTIFY_TOKEN", "")


@app.post("/messages/{message}")
async def post_message(message: str):
    url = "https://notify-api.line.me/api/notify"
    headers = {"Authorization": "Bearer " + token}
    payload = {"message": message}
    requests.post(url, headers=headers, params=payload)

    return {"message": "Message sent successfully"}
