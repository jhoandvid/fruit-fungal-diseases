import pymongo
from src.utils.environment.env import setting

connection_string = setting.CONNECTION_MONGO_DB
conn = pymongo.MongoClient(connection_string)