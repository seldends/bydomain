from flask import Blueprint
import urllib.request
import requests, json
from re import findall
from pymongo import MongoClient
from bs4 import BeautifulSoup
from webapp.extensions import mongo

#from flask_pymongo import PyMongo 

#mongo = PyMongo()
blueprint = Blueprint('util', __name__)

#site_url_collection = mongo.db.site_url
#site_collection = mongo.db.site_data
#site_favorites = mongo.db.favorites

def get_html(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:65.0) Gecko/20100101 Firefox/65.0'
    }
    try:
        result = requests.get(url, headers=headers)
        result.raise_for_status()
        return result.text
    except(requests.RequestException, ValueError):
        print("Сетевая ошибка")
        return False


def save_url(url):
    url_str = str(url)
    mydict = {"url": url_str}
    site_url_collection = mongo.db.site_url
    site_url_collection.insert_one(mydict)


def get_url():
    html = get_html("https://letsearch.ru/search?text=host%3Aby&s=0")
    if html:
        soup = BeautifulSoup(html, 'html.parser')
        all_url = soup.find('table', class_='search-result__').findAll('td', class_='ico')
        print(all_url)
        for site_url in all_url:
            url = site_url.find('a')['href']
            save_url(url)


def save_data(domain, domain_type, registrar, creation_date, expiration_date):
    site_collection = mongo.db.site_data
    mydict = {"domain": domain, "domain_type": domain_type, "registrar": registrar, "creation_date": creation_date, "expiration_date": expiration_date}
    site_collection.insert_one(mydict)


def get_data(name):
    url_str = "http://api.whois.vu/?q=" + name 

    with urllib.request.urlopen(url_str) as url:
        data = json.loads(url.read().decode())
    text = data["whois"]
    dates = get_dates(text)

    domain = data["domain"]
    domain_type = data["type"]
    registrar = data["registrar"]
    creation_date = dates["creation_date"]
    expiration_date = dates["expiration_date"]
    save_data(domain, domain_type, registrar, creation_date, expiration_date)


def get_dates(text):
    # Creation Date - дата создания домена
    # Expiration Date/free-date - дата окончания действия домена
    # Updated Date/Last updated - последняя дата обновления
    cd_pattern = r"Creation Date: \d{4}-\d\d-\d\d|created:       \d{4}-\d\d-\d\d" 
    ed_pattern = r"Expiration Date: \d{4}-\d\d-\d\d|paid-till:     \d{4}-\d\d-\d\d"
    date_pattern = r"\d{4}-\d\d-\d\d"
    creation_date = findall(date_pattern, findall(cd_pattern, text)[0])
    expiration_date = findall(date_pattern, findall(ed_pattern, text)[0])
    return {"creation_date": creation_date[0], "expiration_date": expiration_date[0]}

# def fav_col(domain, domain_type, registrar, creation_date, expiration_date):
#     mydict = {"domain": domain, "domain_type": domain_type, "registrar": registrar, "creation_date": creation_date, "expiration_date": expiration_date}
#     site_collection.insert_one(mydict)


#def add_site(url):
#get_data()