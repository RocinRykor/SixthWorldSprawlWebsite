from flask import render_template, Blueprint  # , redirect, session, request
from sixthworldsprawl.app import db, User, Character

general = Blueprint("general", __name__)


@general.app_errorhandler(404)
def custom_error_page(e):
    return render_template("error.html", title="404 - Page Not Found!")

@general.route("/")
@general.route("/index")
@general.route("/home")
def index():
    return render_template("index.html", title="Sixth World Sprawl")

@general.route("/characters")
def characters():
    return render_template("characters.html", title="Meet The Runners")

@general.route("/roller")
def roller():
    return render_template("diceroller.html", title="Dice Roller")