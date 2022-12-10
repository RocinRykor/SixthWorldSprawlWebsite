from flask_login import login_user, current_user
from flask import render_template, redirect, Blueprint, request, session, flash
from werkzeug.security import check_password_hash
from sixthworldsprawl.forms import LoginForm, UserForm
from sixthworldsprawl.utils import flash_form_errors
from sixthworldsprawl.app import db
from sixthworldsprawl import models
from werkzeug.security import check_password_hash
from flask_login import login_user, logout_user


User = models.User


auth = Blueprint("auth", __name__)


@auth.route("/login/", methods=["POST"])
def login():
    # Make sure the form validates
    form = LoginForm(request.form)
    if not form.validate():
        # flash("Invalid form data", "error")
        flash_form_errors(form, "error")
        return render_template("login.html", title="SixthWorldSprawl Login",
                               form=form)

    # Get the form data
    username = form.username.data
    password = form.password.data

    # Try select a user
    user = User.query.filter_by(username=username).first()
    if not user:
        flash("Invalid user or password.", "error")
        return render_template("login.html", title="SixthWorldSprawl Login",
                               form=form)

    # Check the password.
    if check_password_hash(user.password, password):
        login_user(user, remember=True)
        user.authenticated = True
        return render_template("welcome.html", title="Congrats")

    flash("Invalid user or password.", "error")
    return render_template("login.html", title="Invalid Login",
                           form=form)


@auth.route("/login/", methods=["GET"])
def display_login():
    form = LoginForm()
    return render_template("login.html", title="SixthWorldSprawl Login", 
                            form=form)


@auth.route("/logout/")
def logout():
    try:
        current_user.authenticated = False
    except KeyError:
        return redirect("/login/")
    return redirect("/")


@auth.route("/signup/")
def signup():
    user = User.query.filter_by(id=1).first()
    if user:
        return redirect("auth.display_login")
    
    form = UserForm()
    return render_template("signup.html", form=form)


@auth.route("/signup/", methods=['POST'])
def finish_signup():
    form = UserForm(request.form)
    username = form.name.data
    password = form.password.data
    confirmation = form.confirmation.data

    if not (password == confirmation):
        flash("Password does not match confirmation", "error")
        return render_template("setup.html", form=form)
    
    user = User(username=username, is_admin=True)
    user.set_password(password)

    db.session.add(user)
    db.session.commit()
    return redirect("/login/")