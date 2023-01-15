# Assensing Test Steps
# Roll and Assencing (4) Success Test
# (Optional) Roll an Aura Reading (4) Complementary Test
#   * Half the successes from Complementary Test are added to initial Success Test
# Compare Results to Assencing Table

from sixthworldsprawl.utils.rollers import dice_roller
import math

def assencing_test(assencing_dice_pool, target_number=4, aura_reading_dice_pool=0):
    assencing_rolls = dice_roller.sr3_roll(assencing_dice_pool)
    assencing_results = dice_roller.success_test(assencing_rolls, target_number)

    aura_reading_rolls = dice_roller.sr3_roll(aura_reading_dice_pool)
    # Aura Reading is a supplentary roll so the results are divided by two and rounded down
    aura_reading_initial_results = dice_roller.success_test(aura_reading_rolls, target_number)
    aura_reading_results = math.trunc(aura_reading_initial_results/2)

    if assencing_results:
        total_hits = assencing_results + aura_reading_results
    else :
        total_hits = 0

    output = {
        "Assencing Test" : {
            "Rolls" : assencing_rolls,
            "Results" : assencing_results,
        },
        "Aura Reading" : {
            "Rolls" : aura_reading_rolls,
            "Raw Results" : aura_reading_initial_results,
            "Results" : aura_reading_results,
        },
        "Total Hits" : total_hits
    }

    return output
