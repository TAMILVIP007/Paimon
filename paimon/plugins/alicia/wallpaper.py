import requests
from pyrogram.types import Message

from paimon import Message, paimon


@paimon.on_cmd(
    "wallpaper",
    about={
        "header": "Search Wallpaper",
        "description": "Search and Download Wallpapers from Nekos-life and upload to Telegram",
        "usage": "{tr}wall [Query]",
        "examples": "{tr}wall paimon",
    },
)
async def wall_(message: Message):
    r = requests.get("https://nekos.life/api/v2/img/wallpaper")
    g = r.json().get("url")
    await paimon.send_document(
        message.chat.id,
        g,
    )