from flask import Blueprint, redirect, url_for, render_template, flash

from webapp.user.forms import LoginForm, RegistrationForm
from webapp.site.forms import SearchForm
from webapp.extensions import mongo
from webapp.site.util import get_data, get_url, get_data_all

blueprint = Blueprint('site', __name__, url_prefix='/site')


@blueprint.route('/sort_test')
def sort_test():
    # site_url_collection = mongo.db.site_url
    site_collection = mongo.db.site_data
    search_form = SearchForm()
    login_form = LoginForm()
    signup_form = RegistrationForm()
    site_list = site_collection.find({})

    context = {
        'login_form': login_form,
        'signup_form': signup_form,
        'site_list': site_list,
        'search_form': search_form
        }
    # get_url()
    # get_data_all()

    return render_template('result.html', **context)


@blueprint.route('/search', methods=['GET', 'POST'])
def search():
    site_collection = mongo.db.site_data
    login_form = LoginForm()
    signup_form = RegistrationForm()
    search_form = SearchForm()
    site_list = []
    context = {
        'login_form': login_form,
        'signup_form': signup_form,
        'site_list': site_list,
        'search_form': search_form
        }

    if search_form.validate_on_submit():
        url_str = search_form.request.data
        result = site_collection.find({"domain": url_str})
        for x in result:
            site_list.append(x)
        if not site_list:
            get_data(url_str)
            flash('Информация о сайте добавлена')
            result = site_collection.find({"domain": url_str})
            for x in result:
                site_list.append(x)
            return render_template('result.html', **context)
        flash('Сайт найден')
        return render_template('result.html', **context)
    else:
        flash('Ошибка')
        return redirect(url_for('main.index'))
