from flask import request, Blueprint
from sixthworldsprawl.routes.api.discord import discord_api

bot_api = Blueprint("bot_api", __name__, url_prefix="/api/bot")

@bot_api.route("/test", methods=["POST"])
def simple_test():
    """
    Method: POST

    Simple testing function, return response based on incoming json data

    Data must be in JSON format

    KEYS REQUIRED:
    ==============
    key

    -> JSON Dict
    """

    response = discord_api.test(request.json)
    return response, 200