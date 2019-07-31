from flask import Blueprint, redirect, url_for, flash

from flask_login import current_user, login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash

from webapp.user.forms import LoginForm, RegistrationForm, ChangePasswordForm
from webapp.user.models import User
from webapp.extensions import mongo

blueprint = Blueprint('user', __name__, url_prefix='/users')


@blueprint.route('/signup', methods=['GET', 'POST'])
def signup():
    user_collection = mongo.db.users
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    signup_form = RegistrationForm()
    if signup_form.validate_on_submit():
        query_username = {"username": signup_form.username.data}
        query_email = {"email": signup_form.email.data}
        existing_username = user_collection.find_one(query_username)
        existing_email = user_collection.find_one(query_email)
        if existing_username is not None:
            flash('Пользователь с таким именем уже зарегистрирован')
            return redirect(url_for('main.index'))
        if existing_email is not None:
            flash('Пользователь с такой почтой уже зарегистрирован')
            return redirect(url_for('main.index'))
        password = set_password(signup_form.password.data)
        mydict = {
            "username": signup_form.username.data,
            "email": signup_form.email.data,
            "password": password,
            "role": "user"
            }
        user_collection.insert(mydict)
        flash('Вы успешно зарегистрировались')
        return redirect(url_for('main.index'))
    else:
        for field, errors in signup_form.errors.items():
            for error in errors:
                flash('Ошибка в поле "{}": - {}'.format(getattr(signup_form, field).label.text, error))
        return redirect(url_for('main.index'))


@blueprint.route('/login', methods=['POST'])
def login():
    user_collection = mongo.db.users
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    login_form = LoginForm()
    if login_form.validate_on_submit():
        password = login_form.password.data
        user = user_collection.find_one({"username": login_form.username.data})
        if user is None:
            flash('Пользователь не найден')
            return redirect(url_for('main.index'))
        if not check_password(user['password'], password):
            flash('Неверный пароль')
            return redirect(url_for('main.index'))
        if user and check_password(user['password'], password):
            username = user['username']
            hash_password = user['password']
            user_obj = User(username, hash_password)
            login_user(user_obj)
            flash('Вы вошли на сайт')
            return redirect(url_for('main.index'))
        return redirect(url_for('main.index'))
    else:
        flash('Ошибка')
        return redirect(url_for('main.index'))


@blueprint.route('/change_password', methods=['POST'])
def change_password():
    change_password_form = ChangePasswordForm()
    user_collection = mongo.db.users

    if change_password_form.validate_on_submit():

        password_old = change_password_form.password_old.data
        password_new1 = change_password_form.password_new1.data
        password_new2 = change_password_form.password_new2.data

        username = current_user.get_id()
        myquery = {"username": username}
        user = user_collection.find_one(myquery)

        if not check_password(user['password'], password_old):
            flash('Неверный пароль')
            return redirect(url_for('main.settings'))
        if password_new1 != password_new2:
            flash('пароли не совпадают')
            return redirect(url_for('main.settings'))
        if password_old == password_new1:
            flash('Старый и новый пароли совпадают')
            return redirect(url_for('main.settings'))

        password = set_password(change_password_form.password_new1.data)
        newvalues = {"$set": {"password": password}}
        user_collection.update_one(myquery, newvalues)
        flash('Пароль обновлён')
        return redirect(url_for('main.index'))
    else:
        flash('Ошибка')
        return redirect(url_for('main.index'))


@blueprint.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))


def set_password(password):
    return generate_password_hash(password)


def check_password(password_hash, password2):
    return check_password_hash(password_hash, password2)
