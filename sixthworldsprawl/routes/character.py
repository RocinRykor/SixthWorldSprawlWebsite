from flask import render_template, Blueprint, request
from flask_login import login_required, current_user

from sixthworldsprawl.app import db, Character
from sixthworldsprawl.forms import CharacterForm
from sixthworldsprawl.routes.api.characters import character_api_routes
from sixthworldsprawl.routes.api.portraits import portraits_api
from sixthworldsprawl.routes.api.users import users_api

character = Blueprint("character", __name__, url_prefix="/character")


@character.route("/")
def characters():
    players = users_api.get_all()
    return render_template("public/characters/characters.html",
                           title="Meet The Runners", players=players)


@character.route("/<int:character_id>")
def character_modal(character_id):
    players = users_api.get_all()
    character = character_api_routes.get_character(character_id)
    return render_template("public/characters/partials/character_modal.html", title="Modal Test", players=players,
                           character=character)


@login_required
@character.route("/edit", methods=["GET"])
def get_edit_character():
    form = CharacterForm(request.form)
    portraits = portraits_api.get_all()
    return render_template("public/characters/create_character.html", form=form, portraits=portraits)


@login_required
@character.route("/edit", methods=["POST"])
def finish_character_add():
    form = CharacterForm(request.form)

    name = form.name.data
    bio = form.bio.data
    race = form.race.data
    gender = form.gender.data
    status = form.status.data
    portrait_id = form.portrait_id.data
    portrait_filename = form.portrait_filename.data

    character = Character(name=name, player_id=current_user.id, bio=bio, race=race, gender=gender, status=status,
                          portrait_id=portrait_id, portrait_filename=portrait_filename)

    db.session.add(character)
    db.session.commit()

    return render_template("public/characters/characters.html", title="Meet The Runners")
