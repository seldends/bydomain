from flask import Blueprint, render_template
from webapp.user.forms import LoginForm, RegistrationForm, ChangePasswordForm
from webapp.site.forms import SearchForm
from flask_login import current_user, login_user, logout_user, LoginManager

from webapp.extensions import mongo 

blueprint = Blueprint('main', __name__)


@blueprint.route('/')
def index():
    title = 'Главная страница'    
    login_form = LoginForm()
    signup_form = RegistrationForm()
    search_form = SearchForm()

    return render_template("index.html", page_title=title, login_form=login_form, signup_form=signup_form, search_form=search_form)

@blueprint.route('/settings')
def settings(): 
    title = 'Настройки'    
    login_form = LoginForm()
    signup_form = RegistrationForm()
    search_form = SearchForm()
    change_password_form = ChangePasswordForm()
      
    return render_template("settings.html", page_title=title, login_form=login_form, signup_form=signup_form, search_form=search_form, change_password_form=change_password_form)


    