from os import environ 

class Config:
    API_ID = environ.get("API_ID", "22696222")
    API_HASH = environ.get("API_HASH", "1b4cdb255f37262200981dbbf87a1fa0")
    BOT_TOKEN = environ.get("BOT_TOKEN", "8096179406:AAGvFyNW9O9O994VxrlR_aPkZj1RiroWA3M") 
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://chhjgjkkjhkjhkjh@cluster0.xowzpr4.mongodb.net/")
    DATABASE_NAME = environ.get("DATABASE_NAME", "forward-bot")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '6964148334').split()]

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
