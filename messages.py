from querys import *


@app.route('/user_messages', methods=['GET', 'POST'])
def user_messages():
    current_user_object = connect_current_user_to_database(current_user)
    title = 'Messages'
    return render_template('user_messages.html', title=title,
                           current_session_user=current_user_object)


@socketio.on('server message')
def server_message(json, methods=['GET', 'POST']):
    socketio.emit('client message', json)
