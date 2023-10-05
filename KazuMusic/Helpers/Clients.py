import config

from pyrogram import Client


app = Client(
    "KazuMusic",
    config.API_ID,
    config.API_HASH,
    bot_token=config.BOT_TOKEN,
)
Ass = Client("Anjay", session_string=str(config.STRING_SESSION), api_id=config.API_ID, api_hash=config.API_HASH)
