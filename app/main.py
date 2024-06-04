import os
from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv

import requests

app = FastAPI()
load_dotenv(dotenv_path=os.path.join("conf", ".env"))
token = os.getenv("LINE_NOTIFY_TOKEN", "")


class Message(BaseModel):
    message: str


@app.post("/messages/")
async def post_message(data: Message):
    url = "https://notify-api.line.me/api/notify"
    headers = {"Authorization": "Bearer " + token}
    payload = {"message": data.message}
    requests.post(url, headers=headers, params=payload)

    return {"message": "Message sent successfully"}
