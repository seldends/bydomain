from flask_pymongo import PyMongo
from pymongo import MongoClient
from werkzeug.security import generate_password_hash, check_password_hash

mongo = PyMongo()

client = MongoClient("mongodb://localhost:27017/")
db = client["brdomain"]
users = db["users"]
site_data = db["site_data"]

def check_password(password1, password2):
    print(check_password_hash(password1, password2)) 


def validate_username(username):
    users_count = users.find_one({ "username": username })
    if users_count:
        print(users_count["username"])


# username = "test"
# myquery = { "username": username}

# users_count = users.find(myquery)
# site_list = site_data.find_one()
# us = users.find_one(myquery)
# if us:
#     print(us["role"])
# print(users_count)
# print(site_list)

# password2 = "150000$TJeCQvvV$15c04a338635b4d11f559b9d8d55f92bb91e17f82ec34283809b25b082ecb550"
# myquery = { "domain" : "tut.by" }  
# site = site_data.find(myquery)
# print(site)
# test = []
# for x in site:
#         test.append(x)
#         print(x)
ttt = "dfsdf"
test = "dgfsgf" + ttt
print(test)


# validate_username(username)
# user = col_site.find(myquery)
# user2 = mongo.db.users.find(myquery)
# print(type(user))
# for x in user:
#     print(x)
# for н in user2:
#     print(н)
  
