from flask_pymongo import PyMongo
from pymongo import MongoClient
from werkzeug.security import generate_password_hash, check_password_hash
import requests
from bs4 import BeautifulSoup
import requests, json


mongo = PyMongo()

client = MongoClient("mongodb://localhost:27017/")
db = client["brdomain"]
users = db["users"]
site_list_url = db["site_url"]


result = site_list_url.find({})
for x in result:
        
        print(x)
print(result)
page_list = [i for i in range(1,2)] 
for page in page_list:
        print(str(page))
# def get_data_all()
#     site_list_url = mongo.db.site_url
#     result = site_list_url.find({ "domain" : url_str })
#         for x in result:
#             site_list.append(x)



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


# def get_html(url):
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:65.0) Gecko/20100101 Firefox/65.0'
#     }
#     try:
#         result = requests.get(url, headers=headers)
#         result.raise_for_status()
#         return result.text
#     except(requests.RequestException, ValueError):
#         print("Сетевая ошибка")
#         return False



# ttt = "dfsdf"
# test = "dgfsgf" + ttt
# print(test)


# r = requests.get('http://tut.by') # first we try http
# print(r.url) # check the actual URL for the site

# name = "tut.by"
# url_str = "http://"+ name
# r = requests.get(url_str) # first we try http
# html = get_html(r.url)
# #print(html)
# if html:
#         soup = BeautifulSoup(html, 'html.parser')
#         title = soup.find('title').text
#         description = soup.find('head').find('meta', {"name":"description"})['content']
#         #description = soup.find('head').find('meta', {"name":"description"})
#         print(title)
#         print(description)
#         print(r.url)
        #return {"title": title, "description": description}
# validate_username(username)
# user = col_site.find(myquery)
# user2 = mongo.db.users.find(myquery)
# print(type(user))
# for x in user:
#     print(x)
# for н in user2:
#     print(н)
  
