from os import getenv
from dotenv import load_dotenv

load_dotenv()

get_queue = {}


API_ID = int(getenv("API_ID", "8479389"))
API_HASH = getenv("API_HASH", "f75e6f068c8bb9b8c884484ea2c6177b")

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

STRING_SESSION = getenv("STRING_SESSION", "BQEHOHgAC3BczuFprsxcdxuMM44c4KG2Ee7z8xmlrgD3iHF2w_xC2bF5E3QWybar8kYPi23X5pG3GiYDWXFOvqrlVa95lKgqOD-xFL1FB3cq3hvqol6U1rd0y3fqSvkZ5-Til1fcG4KbQynqUzBSXF_Nn0umZc0JdTjIu3YZ_6vHjrbi_u0eVfhtROPXqwNRA5ON0HGqTIRw8K1hxgNeIIWPCkuKFyrxS4LgJpn7XBTbz_cH_EesID55puZv7Zbty8S1_xLuFkBVG-1IFXd2SZpOKZ3KuAJzsKnMeK4EXZxQ_sooWuggJmQjtlLzYzHel7Nunuxfrpk5f5NYGDuBzPInF4YQUwAAAABPogyPAA")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "961659670").split()))
