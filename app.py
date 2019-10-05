from config import *
from querys import *

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

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

class User():

    def __init__(self, email):
        self.email = email

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.email
        
    @staticmethod
    def validate_login(password_hash, password):
        return check_password_hash(password_hash, password)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    current_user_object = connect_current_user_to_database(current_user)
    if request.method == 'POST' and form.validate_on_submit():
        user = find_user_by_form_email(form)
        if user and User.validate_login(user['password'], form.password.data):
            user_obj = User(user["contact"]["email"])
            login_user(user_obj)
            flash("is logged in successfully", category='success')
            return redirect(request.args.get("next") or url_for("login"))
        flash("Wrong email or password", category='error')
    return render_template('login.html', title='Login', form=form, current_session_user=current_user_object)
    
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))
    
@lm.user_loader
def load_user(email):
    user = find_user_by_email(email)
    if not user:
        return None
    return User(user['contact']['email'])
    
@app.route('/register', methods=['GET', 'POST'])
def register():
    current_user_object = connect_current_user_to_database(current_user)
    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        if find_user_by_form_email(form) is None:
            create_new_user_query(form)
            user = find_user_by_form_email(form)
            login_user(User(user["contact"]["email"]))
            flash("is logged in successfully", category='success')
            return redirect(request.args.get("next") or url_for("edit_profile"))
        else:
            flash("Email already registered", category='success')
    return render_template('login.html', title='Register', form=form, current_session_user=current_user_object)

@app.route('/user_messages', methods=['GET', 'POST'])
def user_messages():
    current_user_object = connect_current_user_to_database(current_user)
    return render_template('user_messages.html', current_session_user=current_user_object)

@socketio.on('server message')
def server_message(json, methods=['GET', 'POST']):
    socketio.emit('client message', json)

if __name__ == '__main__':
    socketio.run(app,
                host=os.environ.get('IP'),
                port=os.environ.get('PORT'),
                debug=False)