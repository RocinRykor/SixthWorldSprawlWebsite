from flask import render_template, Blueprint, redirect, request
from flask_login import login_required, current_user
from sixthworldsprawl.app import db, User, Character
from sixthworldsprawl.forms import CharacterForm
from sixthworldsprawl.routes.api.characters import characters_api
from sixthworldsprawl.routes.api.users import users_api
from sixthworldsprawl.utils import character_utils
character = Blueprint("character", __name__, url_prefix="/character")

@character.route("/")
def characters():
    players = users_api.get_all()
    return render_template("public/characters/characters.html", 
                            title="Meet The Runners", players=players)

@login_required
@character.route("/edit", methods=["GET"])
def get_edit_character():
    form = CharacterForm(request.form)
    return render_template("public/characters/create_character.html", form=form)

@login_required
@character.route("/edit", methods=["POST"])
def finish_character_add():
    form = CharacterForm(request.form)

    name = form.name.data
    bio = form.bio.data
    race = form.race.data
    gender = form.gender.data
    status = form.status.data

    character = Character(name=name, player_id=current_user.id, bio=bio, race=race, gender=gender, status=status)
    
    db.session.add(character)
    db.session.commit()

    return render_template("public/characters/characters.html", title="Meet The Runners")
