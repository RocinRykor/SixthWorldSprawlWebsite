function submitEvent() {
    var dicePool = document.getElementById('dice_pool').value;
    var targetNumber = document.getElementById('target_number').value;

    let countHits = 0;
    let countsMisses = 0;

    let listRolls = [];

    for (let index = 0; index < dicePool; index++) {
        const result = ExplodingSixRoll();
        listRolls.push(result);
        if (result >= targetNumber) {
            countHits++;
        } else if (result == 1) {
            countsMisses++;
        }
    }

    listRolls.sort(function (a, b) {
        return a - b;
    });

    let output = `Rolling ${dicePool} dice against a Target Number of ${targetNumber}:
    Hits: ${countHits}
    Rolls: ${listRolls}`;

    let resultsArea = document.getElementById('results_text_area');

    console.log(output);
    resultsArea.value = output;
}

function ExplodingSixRoll() {
    //Keep rolling if you get a six, add all the rolls together
    let result = 0;
    let explodingSix = true;

    while (explodingSix) {
        const tmp = getRandomRange(1, 6);
        result += tmp;
        if (tmp != 6) {
            explodingSix = false;
        }
    }

    return result;
}

function getRandomRange(min, max) {
    min = Math.ceil(min);
    max = Math.floor(max);
    return Math.floor(Math.random() * (max - min + 1)) + min;
}
