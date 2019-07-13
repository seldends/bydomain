from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["brdomain"]
site_url = db["site_url"]
site_data = db["site_data"]
users = db["users"]