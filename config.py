from os import getenv
from dotenv import load_dotenv

load_dotenv()

get_queue = {}


API_ID = int(getenv("API_ID", "26987250"))
API_HASH = getenv("API_HASH", "dd3d9c1d6f3db707a983344fab5a9335")

ASS_HANDLER = list(getenv("ASS_HANDLER", ".").split())
BOT_TOKEN = getenv("BOT_TOKEN", "6417202271:AAGGeOlIvOGzwG4Hi4Qoj5xGoQsmpcWehN4")

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "5000"))
LOGGER_ID = int(getenv("LOGGER_ID", "-1001837838911"))
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://kazumusik:kazumusik@cluster0.4lhw10l.mongodb.net/?retryWrites=true&w=majority")
OWNER_ID = list(map(int, getenv("OWNER_ID", "961659670").split()))

PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/8fee06afc6cfe471ea1c2.jpg")
START_IMG = getenv("START_IMG", "https://telegra.ph/file/8fee06afc6cfe471ea1c2.jpg")

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/KazuSupportGrp")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", " https://t.me/KazuxProjects")

STRING_SESSION = getenv("STRING_SESSION", "BQC1PyoEDZURR0ou8y12fnM0Ui6HVP8RL3gLuxv2SLcY8hRXX8ZX2kWlcLYH8UY_2JnuzRdm351xuGUAGGbedHbGDooszbYiU0Ax5n8FNr8Wzhp1BKX1lv0cjyNxhj1meEX9Up749UeAKQ85BoV1h4M61oxtYfA9H4dmvemXJ2efGIHSaGlB1w3m1dOOM5wtqXMdHMuvwSzjgfI48h7nqQhuMA3_vZrtjGPQW3QHMR5muW8VROrIcehvISBCVQgnHhzObuJmSfg2wYp8Mox0LhADxGPJUh8B-If2E1g85D-FO8w6yKMljM_jzVlbDyWCtr1VgiUA-rv5seYEub2M4OWST6IMjwA")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "961659670").split()))
