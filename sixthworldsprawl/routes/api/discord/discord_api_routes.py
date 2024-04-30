from flask import request, Blueprint

from sixthworldsprawl.utils.calculators import assensing_calc

bot_api = Blueprint("bot_api", __name__, url_prefix="/api/bot")


@bot_api.route("/assensing_test", methods=["GET", "POST"])
def assensing_test():
    """
    Method: GET or POST

    Performs an asscencing test including the supplementary aura reading test
    Returns the results of the roll and the gleamed information according to the assensing table

    Keys/Params:
    dice_pool = The amount of dice used in the assensing test, must be greater than 0
    target_number = base target number to be used in both tests, defaults to 4
    aura_reading = amount of dice to be used for a supplementary aura reading test, defaults to 0 to indicate not being used

    GET: Uses Query Params
    POST: Uses JSON format

    -> JSON Dict
    """

    if request.method == "GET":
        dice_pool = request.args.get('dice_pool', 1, type=int)
        target_number = request.args.get('target_number', 4, type=int)
        aura_reading = request.args.get('aura_reading', 0, type=int)
    elif request.method == "POST":
        data = request.get_json()
        dice_pool = data.get('dice_pool') or 1
        target_number = data.get('target_number') or 4
        aura_reading = data.get('aura_reading') or 0
    else:
        return "Invalid request method"

    response = assensing_calc.assensing_test(dice_pool, target_number, aura_reading)

    return response, 200
