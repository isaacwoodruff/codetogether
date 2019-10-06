from querys import *

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

"""
The User class is what is used to create a user which can be used to register
and login. The validate_login function checks if the password is correct. The
is_authenticated function can be used to allow users to access certain pages
"""

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

"""
The load_user view calls a query to find a user in the database with a specific
email. It returns None if the user doesn't exist. If the user does exist it
returns an instance of the User class with its id as the email from the user in
the database. This will give access to pages with @login_required
"""

@lm.user_loader
def load_user(email):
    user = find_user_by_email(email)
    if not user:
        return None
    return User(user['contact']['email'])

"""
The login view renders a form. If its validated on submission it querys the
database for a user with the form email. If the user exists, and the database
password and form password are the same it creates an instance of the User
class. Then the User is logged in and it renders the next page that was trying
to be accessed or the login template
"""

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

"""
The register view renders a form. If validated on submission it check to see if
the user email is already in use if not it inserts a new user document to the
users collection with the form data. It then querys the database for the new
user and creates an instance of the User class which gets logged in. Then it
redirects to edit_profile
"""

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
            return redirect(url_for("edit_profile"))
        else:
            flash("Email already registered", category='success')
    return render_template('login.html', title='Register', form=form, current_session_user=current_user_object)