import os
from dotenv import load_dotenv

load_dotenv()


class Setting:
    CONNECTION_MONGO_DB = os.getenv("CONNECTION_MONGO_DB")
    NAME_DB_MONGO = os.getenv("NAME_DB_MONGO")
    OPEN_KEY= os.getenv("OPEN_KEY")

setting = Setting()
print(setting.CONNECTION_MONGO_DB)
