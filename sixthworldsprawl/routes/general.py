from flask import render_template, Blueprint, redirect
from sixthworldsprawl.app import db, User, Character

general = Blueprint("general", __name__)

@general.app_errorhandler(404)
def custom_error_page(e):
    return render_template("public/error.html", title="404 - Page Not Found!")

@general.route("/")
@general.route("/index")
@general.route("/home")
def index():
    return render_template("public/index.html", title="Sixth World Sprawl")

@general.route("/roller")
def roller():
    return render_template("public/rollers/diceroller.html", title="Dice Roller")

@general.route("/matrixhost")
def matrixhost():
    return render_template("public/generators/matrixhost.html", title="Matrix Host Generator")

@general.route("/matrixsecurity")
def matrixsecurity():
    return render_template("public/generators/matrixsecurity.html", title="Matrix Security Sheaf Generator")