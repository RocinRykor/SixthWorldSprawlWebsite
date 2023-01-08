from flask import request, Blueprint
from flask_login import login_required
from sixthworldsprawl.routes.api.portraits import portraits_api

portrait_api = Blueprint("portraits_api", __name__, url_prefix="/api/portrait")

@login_required
@portrait_api.route("/create/", methods=["POST"])
def create_portrait():
    """
    Method: POST

    Creates a portrait from the POSTed data

    Data must be in JSON format

    KEYS REQUIRED:
    ==============
    filename

    -> JSON Dict
    """

    portrait = portraits_api.create_portrait(request.json)
    return portrait.jsonify(), 200

@portrait_api.route("/<int:portrait_id>", methods=["GET"])
def get_portrait(portrait_id):
    portrait = portraits_api.get_portrait(portrait_id)
    
    if not portrait:
        return {"message": "portrait not found", "error": 404}, 200
    return portrait.jsonify()


@portrait_api.route("/all", methods=["GET"])
def get_all_portraits():
    portraits = portraits_api.get_all()
    portraits = [portrait.jsonify() for portrait in portraits]
    return portraits