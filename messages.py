from querys import *

@app.route('/user_messages', methods=['GET', 'POST'])
def user_messages():
    current_user_object = connect_current_user_to_database(current_user)
    return render_template('user_messages.html', current_session_user=current_user_object)

@socketio.on('server message')
def server_message(json, methods=['GET', 'POST']):
    socketio.emit('client message', json)