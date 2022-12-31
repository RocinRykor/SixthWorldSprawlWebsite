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

    console.log(
        `Host Level-Host Rating/Access/Control/Index/Files/Slave
        Green-${securityValue}/${subsystemAccess}/${subsystemControl}/${subsystemIndex}/${subsystemFiles}/${subsystemSlave}`
    );

    outputToTable();
}

function outputToTable() {
    var myTable = '<tr><th>Security Code</th>';
    myTable += '<th>Host Rating</th>';
    myTable += '<th>Access</th>';
    myTable += '<th>Control</th>';
    myTable += '<th>Index</th>';
    myTable += '<th>Files</th>';
    myTable += '<th>Slave</th>';

    myTable += '<tr class="table-option"><th> COLOR </th>';
    myTable += '<td>' + securityValue + '</td>';
    myTable += '<td>' + subsystemAccess + '</td>';
    myTable += '<td>' + subsystemControl + '</td>';
    myTable += '<td>' + subsystemIndex + '</td>';
    myTable += '<td>' + subsystemFiles + '</td>';
    myTable += '<td>' + subsystemSlave + '</td>';

    document.getElementById('resultsTable').innerHTML = myTable;
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
