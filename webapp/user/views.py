from flask import Blueprint, redirect, url_for, render_template, flash, request
from webapp.user.forms import LoginForm, RegistrationForm
from webapp.user.models import User
from flask_login import current_user, login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from webapp.database import users, site_data

blueprint = Blueprint('user', __name__, url_prefix='/users')

@blueprint.route('/signup', methods=['GET','POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    signup_form = RegistrationForm()
    if signup_form.validate_on_submit():
        existing_username = users.find_one({ "username" : signup_form.username.data })
        existing_email = users.find_one({ "email" : signup_form.email.data })
        if existing_username is not None:
            flash('Пользователь с таким именем уже зарегистрирован')
            return redirect(url_for('main.index'))
        if existing_email is not None:
            flash('Пользователь с такой почтой уже зарегистрирован')
            return redirect(url_for('main.index'))
        password = set_password(signup_form.password.data)
        mydict = {"username": signup_form.username.data, "email": signup_form.email.data, "password": password, "role": "user"}
        users.insert(mydict)
        flash('Вы успешно зарегистрировались')
        return redirect(url_for('main.index'))
    else:
        for field, errors in signup_form.errors.items():
            for error in errors:
                flash('Ошибка в поле "{}": - {}'.format(getattr(signup_form, field).label.text, error))
        return redirect(url_for('main.index'))


@blueprint.route('/login', methods=['POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    login_form = LoginForm()
    if login_form.validate_on_submit():
        password = login_form.password.data  
        user = users.find_one({ "username" : login_form.username.data })
        if user is None:
            flash('Пользователь не найден')
            return redirect(url_for('main.index'))
        if not check_password(user['password'], password):
            flash('Неверный пароль')
            return redirect(url_for('main.index'))
        if user and check_password(user['password'], password):
            user_obj = User(username=user['username'])
            login_user(user_obj)
            flash('Вы вошли на сайт')
            return redirect(url_for('main.index')) 
    else:     
        flash('Неправильное имя пользователя или пароль')
        return redirect(url_for('main.index'))


@blueprint.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

def set_password(password):
    return generate_password_hash(password)

def check_password(password_hash, password2):
    return check_password_hash(password_hash, password2)