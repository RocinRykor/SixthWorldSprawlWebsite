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
