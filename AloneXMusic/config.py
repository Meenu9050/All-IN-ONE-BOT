#ALONE CODER
from os import getenv
from dotenv import load_dotenv

load_dotenv()

class Config:
    def __init__(self):
        self.API_ID = int(getenv("API_ID", "17596251"))
        self.API_HASH = getenv("API_HASH", "e58343b4c0193e293e391daf97603fcd")

        self.BOT_TOKEN = getenv("BOT_TOKEN") or getenv("TOKEN", "Apna Bot Token")
        self.MONGO_URL = getenv("MONGO_URL") or getenv("DB_URL", "Apna Mongo Db Dalo")

        self.LOGGER_ID = int(getenv("LOGGER_ID") or getenv("LOG_GROUP_ID", "0"))
        self.OWNER_ID = int(getenv("OWNER_ID") or getenv("ALONE_OWNER_ID", "0"))
        
        self.SESSION1 = getenv("SESSION") or getenv("USER_STRING", "Apna String Dalo")
        self.SESSION2 = getenv("SESSION2", None)
        self.SESSION3 = getenv("SESSION3", None)

        self.SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/AloneUpdates")
        self.SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/AloneBotSupport")

        self.AUTO_END: bool = str(getenv("AUTO_END", "False")).lower() == "true"
        self.AUTO_LEAVE: bool = str(getenv("AUTO_LEAVE", "False")).lower() == "true"
        self.VIDEO_PLAY: bool = str(getenv("VIDEO_PLAY", "True")).lower() == "true"

        self.QUEUE_LIMIT = int(getenv("QUEUE_LIMIT", "50"))
        self.DURATION_LIMIT = int(getenv("DURATION_LIMIT", "5400"))
        self.PLAYLIST_LIMIT = int(getenv("PLAYLIST_LIMIT", "20"))
        self.YOUTUBE_API_KEY = getenv("YOUTUBE_API_KEY", "INFLEX68575028D")
        self.COOKIES_URL = [
            url for url in getenv("COOKIES_URL", "").split(" ")
            if url and "batbin.me" in url
        ]
        self.DEFAULT_THUMB = getenv("DEFAULT_THUMB", "https://te.legra.ph/file/3e40a408286d4eda24191.jpg")
        self.PING_IMG = getenv("PING_IMG", "https://files.catbox.moe/haagg2.png")
        self.START_IMG = getenv("START_IMG", "https://files.catbox.moe/zvziwk.jpg")

    def check(self):
        invalid_values = {"", "0", "Apna Bot Token", "Apna Mongo Db Dalo", "Apna String Dalo"}
        missing = [
            var
            for var in ["API_ID", "API_HASH", "BOT_TOKEN", "MONGO_URL", "LOGGER_ID", "OWNER_ID", "SESSION1"]
            if str(getattr(self, var, "")).strip() in invalid_values
        ]
        if missing:
            raise SystemExit(f"Missing required environment variables: {', '.join(missing)}")
