from flask import Blueprint, render_template
from webapp.user.forms import LoginForm, RegistrationForm
from flask_login import current_user, login_user, logout_user, LoginManager

from .extensions import mongo 

main = Blueprint('main', __name__)

@main.route('/')
def index():
    title = 'Главная страница'    
    login_form = LoginForm()
    signup_form = RegistrationForm()

    #user_collection = mongo.db.users
    #user_collection.insert({'name' : 'Cristina'})
    #user_collection.insert({'name' : 'Derek'})
    return render_template("index.html", page_title=title, login_form=login_form, signup_form=signup_form)

    