from flask import request, Blueprint
from flask_login import login_required
from sixthworldsprawl.routes.api.character import characters_api

characters_api = Blueprint("characters_api", "__name__", url_prefix="/api/character")

@characters_api.app_errorhandler(404)
    def not_found_error(e):
        return {"error" : "Endpoint Not Found",
        "status" : 404,
        "message" : "The requested endpoint does not exist"}, 404

@login_required
@characters_api.route("/create/", methods=["POST"])
def create_character():
    """
    Method: POST

    Creates a character from the POSTed data

    Data must be in JSON format

    KEYS REQUIRED:
    ==============
    name
    bio
    race
    gender
    status

    -> JSON Dict
    """

    character = characters_api.create_character(request.json)
    return character.jsonify(), 200

@login_required
@characters_api.route("/delete/<int:character_id>", methods=["POST"])
def delete_character(characer_id):
    """
    Method: POST

    While the method would be more clear if it was delete, sending a delete
    request from a web browser is nigh impossible in straight HTML forms.
    Using POST for simplicity.
    """

    character = characters_api.delete_character(characer_id)
    if not character:
        return None

    return {"message" : "Character Deleted"}, 200

@characters_api.route("/edit/<int:character_id>", methods=["POST"])
def edit_character(quote_id):
    """
    Method: POST

    Edits the character with the title and character specified in the request json
    """

    character = characters_api.edit_character(character_id, request.json)
    return character.jsonify(), 200

@character_api.route("/get/<int:character_id>", methods=["GET"])
def get_character(character_id):
    character = characters_api.get_qutoe(character_id)
    
    if not character:
        return {"message": "character not found", "error": 404}, 200
    return character.jsonify()

@character_api.route("/", methods=["GET"])
@character_api.route("/random/", methods=["GET"])
def random_character():
    return characters_api.random_character().jsonify(), 200