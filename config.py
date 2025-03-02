from os import getenv

from dotenv import load_dotenv

load_dotenv()

API_ID = "21553328"
# -------------------------------------------------------------
API_HASH = "3bcc137f124bc8518c30d461986e247b"
# --------------------------------------------------------------
BOT_TOKEN = getenv("BOT_TOKEN", "7940019678:AAFnZD4f0dM_PPZm9vbmuv_HGPxw6EjGswo")
STRING1 = getenv("STRING_SESSION", None)
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://oliva:oliva123@cluster0.6cohqfv.mongodb.net/?retryWrites=true&w=majority")
OWNER_ID = int(getenv("OWNER_ID", "7380417336"))
SUPPORT_GRP = "EsproSupport"
UPDATE_CHNL = "EsproUpdate"
OWNER_USERNAME = "UFC_INOCENT"
