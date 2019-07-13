from flask_pymongo import PyMongo
from pymongo import MongoClient

mongo = PyMongo(uri="mongodb://localhost:27017/brdomain")

client = MongoClient("mongodb://localhost:27017/")
db = client["brdomain"]
col_site = db["users"]
myquery = { "username": "test"}
user = col_site.find(myquery)
user2 = mongo.db.site_data.find(myquery)
print(type(user))
for x in user:
    print(x)
#for н in user2:
 #   print(н)
  
