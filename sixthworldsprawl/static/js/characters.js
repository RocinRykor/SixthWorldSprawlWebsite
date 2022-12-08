let playerRepository = function () {
    const characterFile = '../staic/json/SR3E_active_skills.json';
    let playerList = [];

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
        add: add,
        loadList: loadList,
    };
}();

playerRepository.loadList().then(function () {
    console.log('Complete!');
});
