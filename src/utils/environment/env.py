import os
from dotenv import load_dotenv

load_dotenv()


class Setting:
    CONNECTION_MONGO_DB = os.getenv("CONNECTION_MONGO_DB")
    NAME_DB_MONGO = os.getenv("NAME_DB_MONGO")
    OPEN_KEY = os.getenv("OPEN_KEY")
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
    ALGORITHM = os.getenv("ALGORITHM")
    PORT = os.getenv("PORT")


setting = Setting()
print(setting.CONNECTION_MONGO_DB)
