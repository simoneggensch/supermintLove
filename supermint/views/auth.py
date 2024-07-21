from flask import Blueprint, render_template, url_for, redirect, request, flash
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from sqLite.utils import get_db_connection, dict_factory
from sqLite import db
from sqLite.models.admin import WebsiteUser

auth = Blueprint("auth", __name__)

@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        admin = WebsiteUser.query.filter_by(username=username).first()
        if admin:
            if check_password_hash(admin.password, password):
                flash(f"{username} Logged in!")
                login_user(admin, remember=True)
                return redirect(url_for("home.homePage"))
            else:
                flash("Wrong password. Login failed")
        else:
            flash("Username does not exist. Sign up first")

    return render_template("login.html")

@auth.route("/signup", methods=["GET"])
def signupForm():
    return render_template("signup.html",username='')

@auth.route("/signup", methods=["POST"])
def signupUser():
    username = request.form.get("username")
    password1 = request.form.get("password1")
    password2 = request.form.get("password2")

    if password1 != password2:
        flash("passwords are not the same")
        return render_template("signup.html", username=username)
    else:
        newAdmin = WebsiteUser(username=username, password=generate_password_hash(password1,method='pbkdf2:sha256'))
        db.session.add(newAdmin)
        db.session.commit()
        login_user(newAdmin, remember=True)
        flash(f"{username} signed in correctly")
        return returnHome()



@auth.route("/logout")
@login_required
def logout():
    logout_user()
    flash(f"Successfully logged out")
    return returnHome()


def returnHome():
    return redirect(url_for("home.homePage"))
 