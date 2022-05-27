# (©)Codexbotz
# Recife By #Mafia_Tobatz
# Recode by @RYUUSHINNI
# Kalo clone Gak usah hapus 
# gue tandain akun tele nya ngentod


import logging
import os
from logging.handlers import RotatingFileHandler

# Bot token dari @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5074637924:AAGInVwDx9EAsnDO4w03ThsnvgDUGuXS3X4")

# API ID Anda dari my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "6244159"))

# API Hash Anda dari my.telegram.org
API_HASH = os.environ.get("API_HASH", "3f15b21827506cb63890f756743be15f")

# ID Channel Database
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001616005275"))

# OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "1494610306"))

# NAMA OWNER
OWNER = os.environ.get("OWNER", "@SKANDALID")

# Database
DB_URI = os.environ.get("DATABASE_URL", "postgres://uctragkj:nxREk2PW1JxCSjvPluLV5JN1a-Qlb47X@fanny.db.elephantsql.com/uctragkj")

# Username CH & Group
CHANNEL = os.environ.get("CHANNEL", "DoujindesuKomik")
GROUP = os.environ.get("GROUP", "BacaDoujinIndonesia")

# ID dari Channel Atau Group Untuk Wajib Subscribenya
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1001758755421"))
FORCE_SUB_GROUP = int(os.environ.get("FORCE_SUB_GROUP", "-1001639668526"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

# Pesan Awalan /start
START_MSG = os.environ.get(
    "START_MESSAGE",
    "<b>Hello {first}</b>\n\n<b>Saya dapat menyimpan file pribadi di Channel Tertentu dan pengguna lain dapat mengaksesnya dari link khusus.</b>",
)
try:
    ADMINS = [int(x) for x in (os.environ.get("ADMINS", "1494610306 2113034787 5241534420 5137157066 5116548438 5261846925 5133855965").split())]
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
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == "True"

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
