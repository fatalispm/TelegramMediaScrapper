
import os 
import time
import logging

from telethon import TelegramClient, events, sync
from telethon.tl.types import InputMessagesFilterPhotos
from telethon.errors.rpcerrorlist import FloodWaitError
from dotenv import load_dotenv


load_dotenv()

# These example values won't work. You must get your own api_id and
# api_hash from https://my.telegram.org, under API Development.
api_id = os.getenv('api_id')
api_hash = os.getenv('api_hash')

client = TelegramClient('session_name', api_id, api_hash)
client.start()

group_id = -1001124433333

for message in client.iter_messages(group_id, filter=InputMessagesFilterPhotos):
    try:
        message.download_media(file='photos/')
    except Exception:
        logging.exception("Unknown error occured. Trying to sleep")
        time.sleep(30)
        try:
            message.download_media(file='photos/')
        except Exception as e:
            exit(0)
