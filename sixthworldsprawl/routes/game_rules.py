from flask import render_template, Blueprint, redirect

rules = Blueprint("rules", __name__, url_prefix="/gamerules")


@rules.route("/assencing")
def assencing():
    return render_template('public/game_rules/assencing.html', title="Magic - Assencing")
