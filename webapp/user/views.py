from flask import Blueprint, redirect, url_for, render_template, flash
from webapp import mongo
from webapp.user.forms import LoginForm, RegistrationForm
from flask_login import current_user, login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash

blueprint = Blueprint('user', __name__, url_prefix='/users')

@blueprint.route('/signup', methods=['POST'])
def signup():
    login_form = LoginForm()
    signup_form = RegistrationForm()
    site_list = mongo.db.site_data.find_one()
    if signup_form.validate_on_submit():
        password = set_password(signup_form.password.data)
            
        mydict = {"username": signup_form.username.data, "email": signup_form.email.data, "password": password, "role": "user"}
        mongo.db.users.insert(mydict)
        flash('Вы успешно зарегистрировались')
        return render_template('index.html', login_form=login_form, signup_form=signup_form, site_list=site_list)
    else:
        for field, errors in signup_form.errors.items():
            for error in errors:
                flash('Ошибка в поле "{}": - {}'.format(getattr(signup_form, field).label.text, error))
        return render_template('index.html', login_form=login_form, signup_form=signup_form, site_list=site_list)


@blueprint.route('/login', methods=['POST'])
def login():
    login_form = LoginForm()
    signup_form = RegistrationForm()
    site_list = mongo.db.site_data.find_one()
    if login_form.validate_on_submit():
        myquery = { "username" : login_form.username.data }
        user = mongo.db.site_data.find(myquery)
        if user and check_password(login_form.password.data):
            login_user(user)
            flash('Вы вошли на сайт')
            return redirect(url_for('user.base'))
        flash('Пароль не прошел проверку')
    flash('Неправильное имя пользователя или пароль')
    return render_template('index.html', login_form=login_form, signup_form=signup_form, site_list=site_list)


@blueprint.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

def set_password(password):
    return generate_password_hash(password)

def check_password(password1, password2):
    return check_password_hash(password1, password2)