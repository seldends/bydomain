from flask import Blueprint, redirect, url_for, render_template, flash


from webapp.user.forms import LoginForm, RegistrationForm
from webapp.site.forms import SearchForm
from webapp.extensions import mongo

blueprint = Blueprint('site', __name__, url_prefix='/site')




@blueprint.route('/sort_test')
def sort_test():
    #site_url_collection = mongo.db.site_url
    site_collection = mongo.db.site_data
    search_form = SearchForm()       
    login_form = LoginForm()
    signup_form = RegistrationForm()
    site_list = site_collection.find({})

    return render_template('test.html', login_form=login_form, signup_form=signup_form, site_list=site_list, search_form=search_form)

