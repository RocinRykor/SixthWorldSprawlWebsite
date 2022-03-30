from flask import Blueprint, redirect, render_template, request, flash
from flask_login import current_user, login_required
from forms import LoginForm
from utils import flash_form_errors
from sixthworldsprawl import models
from werkzeug.security import check_password_hash
from flask_login import login_user, logout_user


User = models.User


auth = Blueprint("auth", __name__)


@auth.route("/logout/")
@login_required
def logout():
    current_user.authenticated = False
    logout_user()
    return redirect("/login/")


@auth.route("/login/", methods=["GET"])
def login():
    wtform = LoginForm()
    return render_template("/login.html", form=wtform)


@auth.route("/login/", methods=["POST"])
def process_login():
    wtform = LoginForm(request.form)

    # Check if the form is valid. If not, return to the login screen.
    if not wtform.validate():
        flash_form_errors(wtform, "error")
        return render_template("/login.html", form=wtform)

    # Check if the user exists
    form_name = wtform.name.data
    user = User.query.filter_by(name=form_name).first()

    if not user:
        flash("Invalid username or password", "error")
        return render_template("/login.html", form=wtform)

    password = wtform.password.data
    if not check_password_hash(user.password, password):
        flash("Invalid username or password", "error")
        return render_template("/login.html", form=wtform)

    login_user(user)
    flash(f"Welcome {user.name}", "info")
    user.authenticated = True
    return redirect("/")
