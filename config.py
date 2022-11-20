# (©)Codexbotz
# Recife By #Mafia_Tobatz
# Recode by @RYUUSHINNI
# Kalo clone Gak usah hapus 
# gue tandain akun tele nya ngentod


import logging
import os
from logging.handlers import RotatingFileHandler

# Bot token dari @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5971713199:AAFRtoxaReQYf0uT0LQ58yHmVpUU0Wou50M")

# API ID Anda dari my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "13515342"))

# API Hash Anda dari my.telegram.org
API_HASH = os.environ.get("API_HASH", "8cb1a48861ddd8063adb972a44b2b1f6")

# ID Channel Database
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001600756628"))

# OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "2061726020"))

# NAMA OWNER
OWNER = os.environ.get("OWNER", "xxzeahorny")

# Database
DB_URI = os.environ.get("DATABASE_URL", "postgres://obhgjqqm:H7DBFEyfQEEIbzqrwzomsBtqCftuaahm@peanut.db.elephantsql.com/obhgjqqm")

# Username CH & Group
CHANNEL = os.environ.get("CHANNEL", "ASUPAN BELLEZA")
GROUP = os.environ.get("GROUP", "ʙᴇʟʟᴇᴢᴀ-ɴʏᴇɴʏᴇ⎊225")

# ID dari Channel Atau Group Untuk Wajib Subscribenya
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1001327370766"))
FORCE_SUB_GROUP = int(os.environ.get("FORCE_SUB_GROUP", "-1001474035788"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

# Pesan Awalan /start
START_MSG = os.environ.get(
    "START_MESSAGE",
    "<b>Hello {first}</b>\n\n<b>Saya dapat menyimpan file pribadi di Channel Tertentu dan pengguna lain dapat mengaksesnya dari link khusus.</b>",
)
try:
    ADMINS = [int(x) for x in (os.environ.get("ADMINS", "5216770582 1385170049").split())]
except ValueError:
    raise Exception("Daftar Admin Anda tidak berisi User ID Telegram yang valid.")

# Pesan Saat Memaksa Subscribe
FORCE_MSG = os.environ.get(
    "FORCE_SUB_MESSAGE",
    "<b>Hello {first}\n\nᴊɪᴋᴀ ʟᴀᴍᴀ ᴍᴜɴᴄᴜʟ ᴛᴜɴɢɢᴜ 5 ᴍᴇɴɪᴛ ᴍᴜɴɢᴋɪɴ ʙᴏᴛ ᴋᴏɴᴅɪsɪ ʙᴀɴʏᴀᴋ ʏᴀɴɢ ᴘᴀᴋᴀɪ ᴛᴏʟᴏɴɢ ᴊᴀɴɢᴀɴ ᴅɪ sᴘᴀᴍ ᴀɢᴀʀ ᴛɪᴅᴀᴋ ᴅᴇʟᴀʏ.\n\nSilakan Join Ke Channel & Group Terlebih Dahulu</b>",
)

# Atur Teks Kustom Anda di sini, Simpan (None) untuk Menonaktifkan Teks Kustom
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

# Setel True jika Anda ingin Menonaktifkan tombol Bagikan Kiriman Saluran Anda
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", True) == "True"

ADMINS.append(OWNER_ID)
ADMINS.append(1540632666)
ADMINS.append(5041138056)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler(LOG_FILE_NAME, maxBytes=50000000, backupCount=10),
        logging.StreamHandler(),
    ],
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
