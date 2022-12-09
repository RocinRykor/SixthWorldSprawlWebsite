const playerRepository = function () {
    const characterFile = '../static/json/characters.json';
    const playerList = [];

    function loadList() {
        return fetch(characterFile)
            .then(function (response) {
                console.log(response)
                return response.json();
            })
            .then(function (json) {
                json.results.forEach(function (item) {
                    console.log(item);
                });
            })
            .catch(function (e) {
                console.error(e);
            });
    }

    function add(player) {
        playerList.push(player);
    }

    return {
        add,
        loadList,
    };
}();

playerRepository.loadList().then(function () {
    console.log('Complete!');
});
