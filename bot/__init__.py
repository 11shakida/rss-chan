import os
import logging
from dotenv import load_dotenv
from telegram.ext import Updater, MessageFilter

# Prevent unauthorised access to the bot
class OwnerFilter(MessageFilter):
    def filter(self, message):
        return bool(message.from_user.id == OWNER_ID)
owner_filter = OwnerFilter()

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
LOGGER = logging.getLogger(__name__)

load_dotenv('config.env', override=True)
# Environment Variables
def getConfig(name: str):
    return os.environ[name]
try:
    BOT_TOKEN = getConfig('BOT_TOKEN')
    OWNER_ID = int(getConfig('OWNER_ID'))
    CHAT_ID = getConfig('CHAT_ID')
    DELAY = int(getConfig('DELAY'))
    DATABASE_URL = getConfig('DATABASE_URL')
    if len(DATABASE_URL) == 0:
        raise KeyError
except KeyError as e:
    LOGGER.error("One or more env variables are missing! Exiting now.")
    exit(1)
try:
    CUSTOM_MESSAGES = getConfig('CUSTOM_MESSAGES')
except:
    CUSTOM_MESSAGES = ""

updater = Updater(token=BOT_TOKEN, request_kwargs={'read_timeout': 20, 'connect_timeout': 15})
