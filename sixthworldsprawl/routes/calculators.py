import json

from flask import render_template, Blueprint
from collections import OrderedDict
from sixthworldsprawl.utils.calculators.cyberdeck_programs_calc import total_size_of_utilities_list, total_size_of_data_list
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

    return render_template('public/calculators/cyberdeck_utilities.html', title="Cyberdeck Utilities Calculator",
                           util_data=sorted_data)


@calcs.route("/example")
def example():
    util_file = os.path.join(JSON_DIR, "example_deck.json")
    with open(util_file) as file:
        raw_data = json.loads(file.read())
        deck_name = list(raw_data.keys())[0]
        deck_data = raw_data[deck_name]

        memory = deck_data['memory']
        active_index = memory['active']['utilities']

        storage = memory['storage']
        print("Storage: ", storage)
        storage_utilities_size = total_size_of_utilities_list(storage['utilities'])
        storage_data_size = total_size_of_data_list(storage['data'])
        storage_size = storage_data_size + storage_utilities_size

        active = [storage['utilities'][i] for i in active_index]
        active_size = total_size_of_utilities_list(active)
    return render_template('public/calculators/example_deck.html', title="Example Cyberdeck",
                           deck_data=deck_data, deck_name=deck_name,
                           memory=memory, storage=storage, active=active,
                           storage_size=storage_size, active_size=active_size)
