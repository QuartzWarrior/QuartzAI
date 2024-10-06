import time
import logging
import os
from pymongo import MongoClient
from dotenv import load_dotenv
load_dotenv()

logging.basicConfig(level=logging.INFO)

URI = str(os.getenv("URI"))
DB = str(os.getenv("COLLECTION"))
Collection = str(os.getenv("DB"))

client = MongoClient(URI)
db = client[DB]
collection = db[Collection]

def check_api_key(api_key): 
    user = collection.find_one({"api_key": api_key})
    if user:
        return {
            "status": "success",
            "user_id": user["user_id"],
            "usage": user["usage"]
        }
    else:
        return {
            "status": "error",
            "message": "Invalid API key"
        }
