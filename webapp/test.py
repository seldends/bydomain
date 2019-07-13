from flask_pymongo import PyMongo
from pymongo import MongoClient

mongo = PyMongo()

client = MongoClient("mongodb://localhost:27017/")
db = client["brdomain"]
users = db["users"]
site_data = db["site_data"]

username = "test"
myquery = { "username": username}

users_count = users.find(myquery)
site_list = site_data.find_one()
us = users.find_one(myquery)
if us:
    print(us["role"])
print(users_count)
print(site_list)


def validate_username(username):
    users_count = users.find_one({ "username": username })
    if users_count:
        print(users_count["username"])

validate_username(username)
# user = col_site.find(myquery)
# user2 = mongo.db.users.find(myquery)
# print(type(user))
# for x in user:
#     print(x)
# for н in user2:
#     print(н)
  
