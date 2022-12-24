class APIRequest {
    constructor(api_request) {
        this.endpoint_url = `${window.location.protocol}//${window.location.hostname}:${window.location.port}/api/`;
        this.headers = {
            'Content-Type': 'application/json',
        };
        this.response = {};
        this.api_request = this.endpoint_url + api_request;
    }
    async get_request() {
        this.response = await fetch(this.api_request, {
            method: 'GET',
            mode: 'cors',
            cache: 'no-cache',
            credentials: 'same-origin',
            headers: this.headers,
            redirect: 'follow',
        });
        return this.response.json();
    }
}

// Frontend admin API endpoint implementation
async function character_search(character_id) {
    /*
     * Searches for character on the server.
     * keywords should be a json list of keywords to search for
     *
     * Returns a JSON dict containing the character
     */
    var api_request = `character/${character_id}`;
    var request = new APIRequest(api_request);
    return await request.get_request();
}

function showModal(character_id) {
    character_search(character_id).then((character) => {
        console.log(character);

        $('.modal-title').html(character.name);

        img_url = '/static/img/portraits/' + character.portrait_filename;

        console.log(img_url);

        $('.character-portrait').attr('src', img_url);
        $('#details-metatype').text('Metatype: ' + character.race);
        $('#details-gender').text('Gender: ' + character.gender);
        $('#details-bio').text('Bio: ' + character.bio);
        $('#details-status').text('Current Status: ' + character.status);

        $('#characterModal').modal('show');
    });
}

$(document).ready(() => {
    console.log('Character Window is loaded');
});
