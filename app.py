from config import *
from querys import *
from login import *
from messages import *

"""
The current_user_object is the current_user thats logged in using flask-login
connected with their own user object in the database. This is in most views
so the website can dynamically display information based on whether a user is
logged in or not
"""

@app.route('/')
def index():
    current_user_object = connect_current_user_to_database(current_user)
    return render_template('index.html', current_session_user=current_user_object, title="Home")

"""
The mentors view finds all mentors and renders the mentors search page with them.
If the search bars are used it checks to see if the form was filled. If it was
not then it will just render all the mentors. If it is filled then it will
query the users collection for the name and expertise of the mentor. The title
parameter is used to find users who are mentors.
"""

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

"""
The pair_programmers view does the same thing as the mentors view except that
it renders all the users who want to pair program. The title "Pair Programmers"
is sent to the query so it knows to look for pair programmers
"""

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

"""
The expertise_search view takes a specific expertise and searches for users
who have that expertise. It knows whether to search for mentors or pair
programmers by passing dev_type to the user search query. It then renders the
search template with the relevant users
"""

@app.route('/<dev_type>/search/<expertise_tag>', methods=["GET","POST"])
@login_required
def expertise_search(dev_type, expertise_tag):
    current_user_object = connect_current_user_to_database(current_user)
    name = ['']
    expertise_tag = [expertise_tag]
    users = user_search_query(name, expertise_tag, dev_type)
    return render_template('search.html', users=users, current_session_user=current_user_object, title=dev_type, expertise_tag=expertise_tag)

"""
The edit_profile view renders a form that is automatically filled based on the 
current logged in user. This form contains all the information in the users
own document on the database. They can update or delete their profile from here
"""

@app.route('/edit_profile')
@login_required
def edit_profile():
    current_user_object = connect_current_user_to_database(current_user)
    return render_template('edit_profile.html', current_session_user=current_user_object, title="Edit Profile")

"""
The user_profile view calls a query that finds a user by their user_id which is
given as a parameter to the query. It then renders a user profile which is
populated from the users collection in the database
"""

@app.route('/user/<user_id>')
@login_required
def user_profile(user_id):
    current_user_object = connect_current_user_to_database(current_user)
    user = user_profile_query(user_id)
    title = user["first_name"].capitalize() + ' ' + user["last_name"].capitalize()
    return render_template('user_profile.html', user=user, current_session_user=current_user_object, title=title)

"""
The update_profile view calls a query to update the users document with the
form information from edit_profile
"""

@app.route('/update_profile', methods=["POST"])
@login_required
def update_profile():
    current_user_object = connect_current_user_to_database(current_user)
    update_profile_query(current_user_object)
    return redirect(url_for('edit_profile'))

"""
The delete_profile view renders a form that the user has to enter their email
and password to continue to deletion. If the details of the form are correct on 
submission it calls a query to delete the document of the current user. Then
it redirects to the login view
"""

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
    
# socketio.run() replaces app.run() to run the flask-socketio library properly

if __name__ == '__main__':
    socketio.run(app,
                host=os.environ.get('IP'),
                port=os.environ.get('PORT'),
                debug=True)