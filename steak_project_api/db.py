import os

from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.database import Database

MONGO_USERNAME: str = os.environ["MONGO_USERNAME"]
MONGO_PASSWORD: str = os.environ["MONGO_PASSWORD"]
MONGO_URI: str = f"mongodb+srv://{MONGO_USERNAME}:{MONGO_PASSWORD}@thesteakproject.jmceetb.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(MONGO_URI)
db: Database = client.steak_project
measurements: Collection = db.measurements
