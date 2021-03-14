fetch(URL, {
    headers: {
        'Accept': 'application/json',
        'X-Requested-With': 'XMLHttpRequest', //Necessary to work with request.is_ajax()
    },
})
    .then(response => {
        return response.json() //Convert response to JSON
    })
    .then(data => {

    })
}
