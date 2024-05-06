import json


def calc_utility_size(program_rating=1, multiplier_value=1) -> int:
    """
    Calculates the size of a Cyberdeck Utility Program.

    Formula is Rating² x Multiplier

    :param program_rating: (int) The rating of the utility program. Default is 1.
    :param multiplier_value: (int) The value to multiply by the square of the rating, which determines how much space it takes up in memory. Default is 1.
    :return: (int) The utility size
    :doc-author: Trelent
    """

    return (program_rating * program_rating) * multiplier_value


def calc_utility_cost(program_rating=1, program_size=1) -> int:
    """
    Calculates the cost of a utility program based on its rating and size.

    :param program_rating: (int) The rating of the utility program.
    :param program_size: (int) The size of the utility program in MP. Must be greater than 0.
    :return:  The cost of a utility program
    :doc-author: Trelent
    """

    if 1 <= program_rating <= 3:
        cost = program_size * 100
    elif 4 <= program_rating <= 6:
        cost = program_size * 200
    elif 7 <= program_rating <= 9:
        cost = program_size * 500
    else:
        cost = program_size * 1000
    return cost


def total_size_of_utilities_list(util_list):
    print(util_list)
    total_size = 0
    for util in util_list:
        # print(util['name'], ": ", util["rating"], " x ", util['multiplier'])
        total_size += calc_utility_size(util["rating"], util["multiplier"])
        print(total_size)

    return total_size


def total_size_of_data_list(data_list):
    print(data_list)
    total_size = 0
    for data in data_list:
        total_size += data['size']
        print(total_size)
    return total_size
