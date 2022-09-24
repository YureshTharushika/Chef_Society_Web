
from flask import Blueprint, render_template, redirect, url_for, request, flash
from .models import User
from datetime import datetime
from .extensions import mongo
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint("auth", __name__)


@auth.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get("email")
        password = request.form.get("password")

        user = mongo.db.users.find_one({"email": email})
        if user:
            if check_password_hash(user["password"], password):
                flash("Logged in!", category='success')
                loginuser = User(user)
                login_user(loginuser, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Password is incorrect.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("login.html", user=current_user)


@auth.route("/signup", methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get("email")
        username = request.form.get("username")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        user = mongo.db.users.find_one({"email": email})
        if user:
            flash('Email Already Exists.', category='error')
        else:

            # new_user = User(username=username, email=email,
            #                 password=generate_password_hash(password1, method='sha256'))

            new_user = {
                "username": username,
                "email": email,
                "password": generate_password_hash(password1, method='sha256')

            }
            mongo.db.users.insert_one(new_user)
            login_user(user, remember=True)
            flash('Account Created!.', category='success')
            return redirect(url_for("views.home"))
    return render_template("signup.html", user=current_user)


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))
