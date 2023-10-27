import os

from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.database import Database

MONGO_URI: str = os.environ["MONGO_URI"]
DB_NAME: str = os.environ["MONGO_DB"]

if "MONGO_TEST_DB" in os.environ:
    DB_NAME = os.environ["MONGO_TEST_DB"]

client = MongoClient(MONGO_URI)
db: Database = client[DB_NAME]
measurements: Collection = db.measurements
models: Collection = db.models
