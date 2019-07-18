from flask import Flask 
from .extensions import mongo, login_manager
#from webapp.database import users

from .main import main as main_blueprint
from webapp.user.views import blueprint as user_blueprint
from webapp.site.views import blueprint as site_blueprint
from webapp.user.models import User

def create_app(config_object='webapp.settings'):
    
    app = Flask(__name__)
    app.config.from_object(config_object)
    mongo.init_app(app)

    app.register_blueprint(main_blueprint)
    app.register_blueprint(user_blueprint)
    app.register_blueprint(site_blueprint)

    login_manager.init_app(app)
    login_manager.login_view = 'login'
    user_collection = mongo.db.users

    @login_manager.user_loader
    def load_user(username):
        u = user_collection.find_one({"username": username})
        if not u:
            return None
        return User(username=u["username"])

    return app


