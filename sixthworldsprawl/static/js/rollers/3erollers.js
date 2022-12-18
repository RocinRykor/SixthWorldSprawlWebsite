function submitEvent() {
    var dicePool = document.getElementById('dice_pool').value;
    var target_number = document.getElementById('target_number').value;

    let output = `Rolling ${dicePool} dice against a Target Number of ${target_number}: `;

    let resultsArea = document.getElementById('results_text_area');

    console.log(output);
    resultsArea.value = output;
}

function displayModifier(int) {
    if (int < 0) {
        return `- ${Math.abs(int)}`;
    } else {
        return `+ ${int}`;
    }
}
