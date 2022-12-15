function openModal(title, pageURL) {
    console.log(title);
    console.log(pageURL);

    setContent(pageURL);
    $('.modal-title').html(title);
    $('#genericModal').modal('show');
}

function setContent(pageURL) {
    //First Clear out the exisitng content
    $('.modal-body').empty();

    $('.modal-body').load(pageURL);

    fetch(pageURL)
        .then((response) => response.text())
        .then((text) => ($('.modal-body').inngerHTML = text));
}
