var socket = io.connect('https://' + document.domain + ':' + location.port);

socket.on('connect', function() {
    socket.emit('server message', {
        data: 'User Connected'
    })
    $('form').on('submit', function(e) {
        e.preventDefault()
        socket.emit('server message', {
            user_name: $('input.hide').val(),
            message: $('input.message').val()
        })
        $('input.message').val('').focus()
    })
})

socket.on('client message', function(msg) {
    console.log(msg)
    if (typeof msg.user_name !== 'undefined') {
        $('h3').remove()
        $('div.message_holder').append('<div><h6>' + msg.user_name + ": " + msg.message + '</h6></div>')
    }
})