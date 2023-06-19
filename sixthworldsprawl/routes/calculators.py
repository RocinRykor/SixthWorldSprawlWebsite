import json

from flask import render_template, Blueprint
from collections import OrderedDict
import os

calcs = Blueprint("calcs", __name__, url_prefix="/calculators")

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
JSON_DIR = os.path.join(PROJECT_ROOT, 'static', 'json')


@calcs.route("/cyberdeck")
def cyberdeck():
    util_file = os.path.join(JSON_DIR, "Cyberdeck_Utilities.json")
    with open(util_file) as file:
        util_data = json.load(file)

    # Sort the entries by key (in alphabetical order) and convert back to a dictionary
    sorted_data = OrderedDict(sorted(util_data.items(), key=lambda item: item[0]))

    return render_template('public/calculators/cyberdeck_utilities.html', title="Cyberdeck Utilities Calculator", util_data=sorted_data)
