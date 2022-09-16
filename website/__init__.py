from flask import Flask
from os import path
from flask_login import LoginManager


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "chefkey"

    return app
