from flask import render_template, Blueprint

rules = Blueprint("rules", __name__, url_prefix="/gamerules")


@rules.route("/assensing")
def assensing():
    return render_template('public/game_rules/assensing.html', title="Magic - Assensing")
