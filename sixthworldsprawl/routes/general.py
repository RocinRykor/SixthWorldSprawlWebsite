from flask import render_template, Blueprint  # , redirect, session, request

general = Blueprint("general", __name__)


@general.route("/")
def index():
    return render_template("index.html", title="Sixth World Sprawl")


@general.route("/characters/")
def characters():
    return render_template("characters.html")


@general.route("/decrypt/")
def decrypt():
    return render_template("decrypt.html")
