from config import *
from querys import *
from login import *
from messages import *

@app.route('/')
def index():
    current_user_object = connect_current_user_to_database(current_user)
    return render_template('index.html', current_session_user=current_user_object, title="Home")

@app.route('/<dev_type>/search/<expertise_tag>', methods=["GET","POST"])
@login_required
def expertise_search(dev_type, expertise_tag):
    current_user_object = connect_current_user_to_database(current_user)
    name = ['']
    expertise_tag = [expertise_tag]
    if dev_type == "Mentors":
        users = user_search_query(name, expertise_tag, dev_type)
    if dev_type == "Pair Programmers":
        users = user_search_query(name, expertise_tag, dev_type)
    return render_template('search.html', users=users, current_session_user=current_user_object, title=dev_type, expertise_tag=expertise_tag)
    
@app.route('/mentors', methods=["GET","POST"])
@login_required
def mentors():
    current_user_object = connect_current_user_to_database(current_user)
    users = all_mentors_query()
    title = "Mentors"
    if request.method == 'POST':
        name = request.form.get('name').lower().split(' ', 2)
        expertise = request.form.get('expertise').lower().strip().split(",")
        if name == [""] and expertise == [""]:
            users = all_mentors_query()
            return render_template('search.html', users=users, current_session_user=current_user_object, title=title)
        else:
            users = user_search_query(name, expertise, title)
            return render_template('search.html', users=users, current_session_user=current_user_object, title=title)
    return render_template('search.html', users=users, current_session_user=current_user_object, title=title)

@app.route('/pair_programmers', methods=["GET","POST"])
@login_required
def pair_programmers():
    current_user_object = connect_current_user_to_database(current_user)
    users = all_pair_programmers_query()
    title = "Pair Programmers"
    if request.method == 'POST':
        name = request.form.get('name').lower().split(' ', 2)
        expertise = request.form.get('expertise').lower().strip().split(",")
        if name == [""] and expertise == [""]:
            users = all_pair_programmers_query()
            return render_template('search.html', users=users, current_session_user=current_user_object, title=title)
        else:
            users = user_search_query(name, expertise, title)
            return render_template('search.html', users=users, current_session_user=current_user_object, title=title)
    return render_template('search.html', users=users, current_session_user=current_user_object, title=title)

@app.route('/edit_profile')
@login_required
def edit_profile():
    current_user_object = connect_current_user_to_database(current_user)
    return render_template('edit_profile.html', current_session_user=current_user_object, title="Edit Profile")
    
@app.route('/user/<user_id>')
@login_required
def user_profile(user_id):
    current_user_object = connect_current_user_to_database(current_user)
    user = user_profile_query(user_id)
    title = user["first_name"].capitalize() + ' ' + user["last_name"].capitalize()
    return render_template('user_profile.html', user=user, current_session_user=current_user_object, title=title)

@app.route('/update_profile', methods=["POST"])
@login_required
def update_profile():
    current_user_object = connect_current_user_to_database(current_user)
    update_profile_query(current_user_object)
    return redirect(url_for('edit_profile'))

@app.route('/delete_profile', methods=["GET","POST"])
@login_required
def delete_profile():
    current_user_object = connect_current_user_to_database(current_user)    
    form = LoginForm()
    user_email = form.email.data
    if request.method == 'POST' and form.validate_on_submit():
        if user_email and current_user_object['contact']['email']:
            delete_user_query(current_user_object)
            return redirect(url_for('index'))

    return render_template('login.html', title='Are you sure?', form=form, current_session_user=current_user_object)
    

if __name__ == '__main__':
    socketio.run(app,
                host=os.environ.get('IP'),
                port=os.environ.get('PORT'),
                debug=True)