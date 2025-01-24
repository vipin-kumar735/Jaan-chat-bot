from os import getenv

from dotenv import load_dotenv

load_dotenv()

API_ID = 6435225
# -------------------------------------------------------------
API_HASH = "4e984ea35f854762dcde906dce426c2d"
# --------------------------------------------------------------
BOT_TOKEN = getenv("BOT_TOKEN", "7833972330:AAErp7yd_GYU9UyvE84tyfvFlb0KctRe9do")
STRING1 = getenv("STRING_SESSION", None)
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://theriyamusic94:f67KlgTyzr3TTutn@cluster0.lym5x.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
OWNER_ID = int(getenv("OWNER_ID", 7668520999))
SUPPORT_GRP = "https://t.me/SaregamaSupport"
UPDATE_CHNL = "https://t.me/SaregamaUpdate"
OWNER_USERNAME = "https://t.me/Rocky_dtm"
