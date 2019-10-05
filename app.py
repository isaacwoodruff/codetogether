from config import *
from querys import *
from login import *
from messages import *

@app.route('/')
def index():
    current_user_object = connect_current_user_to_database(current_user)
    return render_template('index.html', current_session_user=current_user_object)
    
@app.route('/mentors/search', methods=["GET","POST"])
@login_required
def mentors_search():
    current_user_object = connect_current_user_to_database(current_user)
    if request.method == 'POST':
        name = request.form.get('name').split(' ', 2)
        expertise = request.form.get('expertise').strip().split(",")
        mentor_search_query(name, expertise)
        return render_template('search.html', users=users, current_session_user=current_user_object, title="Mentors")
    return render_template('search.html', current_session_user=current_user_object, title="Mentors")
    
@app.route('/mentors')
@login_required
def mentors():
    current_user_object = connect_current_user_to_database(current_user)
    title = "Mentors"
    users = all_mentors_query()
    return render_template('search.html', users=users, current_session_user=current_user_object, title=title)
    
@app.route('/pair_programmers/search', methods=["GET","POST"])
@login_required
def pair_programmers_search():
    current_user_object = connect_current_user_to_database(current_user)
    if request.method == 'POST':
        name = request.form.get('name').split(' ', 2)
        expertise = request.form.get('expertise').strip().split(",")
        pair_programmers_search_query(name, expertise)
        return render_template('search.html', users=users, current_session_user=current_user_object, title="Pair Programmers")
    return render_template('search.html', current_session_user=current_user_object, title="Pair Programmers")
    
@app.route('/pair_programmers')
@login_required
def pair_programmers():
    current_user_object = connect_current_user_to_database(current_user)
    title = "Pair Programmers"
    users = all_pair_programmers_query()
    return render_template('search.html', users=users, current_session_user=current_user_object, title=title)

@app.route('/edit_profile')
@login_required
def edit_profile():
    current_user_object = connect_current_user_to_database(current_user)
    return render_template('edit_profile.html', current_session_user=current_user_object)
    
@app.route('/user/<user_id>')
@login_required
def user_profile(user_id):
    current_user_object = connect_current_user_to_database(current_user)
    user = user_profile_query(user_id)
    return render_template('user_profile.html', user=user, current_session_user=current_user_object)
    
@app.route('/update_profile', methods=["POST"])
@login_required
def update_profile(form, current_user_object):
    current_user_object = connect_current_user_to_database(current_user)
    update_profile_query()
    return redirect(url_for('edit_profile'))

if __name__ == '__main__':
    socketio.run(app,
                host=os.environ.get('IP'),
                port=os.environ.get('PORT'),
                debug=False)