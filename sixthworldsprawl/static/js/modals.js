function openModal(title, pageURL) {
    console.log(title);
    console.log(pageURL);

    setContent(pageURL);
    $('#genericModalTitle').html(title);
    $('#genericModal').modal('show');
}

function setContent(pageURL) {
    //First Clear out the exisitng content
    $('#genericModalBody').empty();
    $('#genericModalBody').load(pageURL);
}
