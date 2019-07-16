from flask import Flask, render_template
from webapp.user.forms import LoginForm, RegistrationForm
from flask_login import current_user, login_user, logout_user, LoginManager
from webapp.database import site_data

from webapp.user.views import blueprint as user_blueprint

app = Flask(__name__)
app.config.from_pyfile('config.py')
#app.config["MONGO_URI"] = "mongodb://localhost:27017/brdomain"
#mongo = PyMongo(app)

app.register_blueprint(user_blueprint)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'Login'

@app.route("/")
def home_page():
    title = 'Главная страница'
    login_form = LoginForm()
    signup_form = RegistrationForm()

    site_list = site_data.find_one()
    #mydict = {"username": "signup_form.username", "email": "signup_form.email", "password": "signup_form.password", "role": "user"}
    #mongo.db.site_data.insert(mydict)
    #site_list = mongo.db.site_data.find({"_id": "i7.ru"})
    return render_template("index.html", page_title=title, login_form=login_form, signup_form=signup_form, site_list=site_list)


from flask import Flask 
from flask_login import LoginManager

from .extensions import mongo
from .main import main
from webapp.user.views import blueprint as user_blueprint

def create_app(config_object='webapp.settings'):
    
    app = Flask(__name__)
    app.config.from_object(config_object)
    mongo.init_app(app)
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'Login'

    app.register_blueprint(main)
    app.register_blueprint(user_blueprint)

    return app