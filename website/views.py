from flask import Blueprint, render_template
from .extensions import mongo
from flask_login import login_required, current_user

views = Blueprint("views", __name__)


@views.route("/")
@views.route("/home")
@login_required
def home():
    return render_template("home.html", user=current_user)


@views.route("/insert")
def index():
    user_collection = mongo.db.users
    user_collection.insert_one({'name': 'Tharushika'})

    return render_template("home.html")
