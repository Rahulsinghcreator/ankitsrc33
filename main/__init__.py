import logging
import sys
from decouple import config
from pyrogram import Client
from telethon import TelegramClient
from telethon.sessions import StringSession

# Configure logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("telethon").setLevel(logging.WARNING)

# Environment variables
API_ID = config("API_ID", default=None, cast=int)
API_HASH = config("API_HASH", default=None)
BOT_TOKEN = config("BOT_TOKEN", default=None)
SESSION = config("SESSION", default=None)
FORCESUB = config("FORCESUB", default=None)
AUTH = config("AUTH", default=None)
SUDO_USERS = set(map(int, AUTH.split())) if AUTH else set()

# Initialize Telethon Bot
bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN)

# Initialize Pyrogram Userbot
userbot = Client(session_name=SESSION, api_hash=API_HASH, api_id=API_ID)

try:
    userbot.start()
except Exception as e:
    logging.error("Userbot Error! Have you added SESSION while deploying?", exc_info=True)
    sys.exit(1)

# Initialize Pyrogram Bot
Bot = Client("SaveRestricted", bot_token=BOT_TOKEN, api_id=API_ID, api_hash=API_HASH)

try:
    Bot.start()
except Exception as e:
    logging.error("Failed to start the Bot", exc_info=True)
    sys.exit(1)
