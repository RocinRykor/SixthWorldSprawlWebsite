var matrixInformationTable = {
    'Security Codes': 'This is a test',
};

function generateEasyHost() {
    generateHost(1, 3, 3, 1, 3, 7);
}

function generateAverageHost() {
    generateHost(1, 3, 6, 2, 3, 9);
}

function generateHardHost() {
    generateHost(2, 3, 6, 1, 6, 12);
}

function generateHost(svPool, svSide, svMod, srPool, srSide, srMod) {
    securityValue = rollWithMod(svPool, svSide, svMod);

    subsystemAccess = rollWithMod(srPool, srSide, srMod);
    subsystemControl = rollWithMod(srPool, srSide, srMod);
    subsystemIndex = rollWithMod(srPool, srSide, srMod);
    subsystemFiles = rollWithMod(srPool, srSide, srMod);
    subsystemSlave = rollWithMod(srPool, srSide, srMod);

    outputToTable();
}

function outputToTable() {
    document.getElementById('securityValue').innerHTML = securityValue;
    document.getElementById('subsystemAccess').innerHTML = subsystemAccess;
    document.getElementById('subsystemControl').innerHTML = subsystemControl;
    document.getElementById('subsystemIndex').innerHTML = subsystemIndex;
    document.getElementById('subsystemFiles').innerHTML = subsystemFiles;
    document.getElementById('subsystemSlave').innerHTML = subsystemSlave;

    //Reveal the Copy Results Button
    $('#copyResults').removeClass('visually-hidden');
}

function rollWithMod(dicePool, diceSide, modifer) {
    let tmpValue = modifer;

    for (let i = 0; i < dicePool; i++) {
        tmpValue += getRandomRange(1, diceSide);
    }

    return tmpValue;
}

function getRandomRange(min, max) {
    min = Math.ceil(min);
    max = Math.floor(max);
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

function copyToClipboard() {
    //Get the currently selected security code (Host Color)
    const securityCode = $(
        "input[type='radio'][name='radioSecrityCode']:checked"
    ).val();

    standardFormat = `${securityCode}-${securityValue}/${subsystemAccess}/${subsystemControl}/${subsystemIndex}/${subsystemFiles}/${subsystemSlave}`;

    if (navigator.clipboard) {
        navigator.clipboard.writeText(standardFormat).then(() => {
            alert('Copied to clipboard');
        });
    } else {
        console.log('Browser Not compatible');
    }
}

function openBasicModal(title) {
    $('#genericModalTitle').html(title);
    $('#genericModal').modal('show');
}
