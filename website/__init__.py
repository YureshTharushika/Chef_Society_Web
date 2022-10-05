import os
from flask import Flask
from flask_wtf.csrf import CSRFProtect
from flask_pymongo import PyMongo
from os import path
from bson import ObjectId
from .models import User
from .extensions import mongo
from flask_login import LoginManager
import pyrebase
from dotenv import load_dotenv, find_dotenv


def create_app(config_object='website.settings'):
    app = Flask(__name__)
    csrf = CSRFProtect()
    app.config['SECRET_KEY'] = "chefkey"
    app.config.from_object(config_object)
    # app.config['MONGO_URI'] = 'mongodb+srv://chefsociety:Myapp2022@chefsocietydb.e4h6kbb.mongodb.net/chefsociety?retryWrites=true&w=majority'
    # mongodb_client = PyMongo(app)
    # db = mongodb_client.db

    csrf.init_app(app)
    mongo.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        users = mongo.db.users
        user_json = users.find_one({'_id': ObjectId(user_id)})
        if not user_json:
            return None
        return User(user_json)

    from .views import views
    from .auth import auth
    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    return app
