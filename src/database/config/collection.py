from src.utils.environment.env import setting
from src.database.config.database import conn

name_database = setting.NAME_DB_MONGO


def get_collection(collection: str):
    collection_db = conn["demo"]
    return collection_db[collection]
