# Assensing Test Steps
# Roll and Assensing (4) Success Test
# (Optional) Roll an Aura Reading (4) Complementary Test
#   * Half the successes from Complementary Test are added to initial Success Test
# Compare Results to Assensing Table

import math
from typing import Any

from sixthworldsprawl.utils.constants.magic_constants import ASSCENING_TEST_RESULTS
from sixthworldsprawl.utils.rollers import dice_roller


def assensing_test(assensing_dice_pool, target_number=4, aura_reading_dice_pool=0):
    assensing_rolls = dice_roller.sr3_roll(assensing_dice_pool)
    assensing_results = dice_roller.success_test(assensing_rolls, target_number)

    aura_reading_rolls = dice_roller.sr3_roll(aura_reading_dice_pool)
    # Aura Reading is a supplementary roll so the results are divided by two and rounded down
    aura_reading_initial_results = dice_roller.success_test(aura_reading_rolls, target_number)
    aura_reading_results = math.trunc(aura_reading_initial_results / 2)

    if assensing_results:
        total_hits = assensing_results + aura_reading_results
    else:
        total_hits = 0

    information = get_information_from_table(total_hits)

    output = {
        "Assensing Test": {
            "Rolls": assensing_rolls,
            "Results": assensing_results,
        },
        "Aura Reading": {
            "Rolls": aura_reading_rolls,
            "Raw Results": aura_reading_initial_results,
            "Results": aura_reading_results,
        },
        "Total Hits": total_hits,
        "Information": information
    }

    return output


def get_information_from_table(total_hits: int) -> str | dict[Any, Any]:
    level = ""
    if total_hits == 0:
        return "No Hits, Test Failure"
    elif total_hits < 3:
        level = "LOW"
    elif total_hits < 5:
        level = "MID"
    else:
        level = "HIGH"
    results = {}
    for category, levels in ASSCENING_TEST_RESULTS.items():
        results[category] = levels[level]
    return results
