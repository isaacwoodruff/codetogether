$(document).ready(function() {
    var messageBox = document.getElementById("messages-wrapper");
    
    var socket = io.connect('https://' + document.domain + ':' + location.port);

    socket.on('connect', function() {
        socket.emit('server message', {
            data: 'User Connected'
        })
        $('#messages-form').on('submit', function(e) {
            e.preventDefault()
            socket.emit('server message', {
                user_name: $('input.hide').val(),
                message: $('input.message').val()
            })
            $('input.message').val('').focus()
        })
    })

    socket.on('client message', function(msg) {
        if (typeof msg.user_name !== 'undefined') {
            $('#messages-wrapper h3').remove()
            $('div.message_holder').append('<div><h6>' + msg.user_name + ": " + msg.message + '</h6></div>')
            // Scroll to the bottom when a new message is received or sent, if there is a scroll bar
            if (messageBox != null){
                messageBox.scrollTop = messageBox.scrollHeight;
            }
        }
    })
})