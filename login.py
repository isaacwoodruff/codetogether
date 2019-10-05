from querys import *

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
        
@lm.user_loader
def load_user(email):
    user = find_user_by_email(email)
    if not user:
        return None
    return User(user['contact']['email'])
    
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
    
@app.route('/register', methods=['GET', 'POST'])
def register():
    current_user_object = connect_current_user_to_database(current_user)
    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        if find_user_by_form_email(form) is None:
            create_new_user_query(form)
            user = find_user_by_form_email(form)
            print(user)
            login_user(User(user["contact"]["email"]))
            flash("is logged in successfully", category='success')
            return redirect(request.args.get("next") or url_for("edit_profile"))
        else:
            flash("Email already registered", category='success')
    return render_template('login.html', title='Register', form=form, current_session_user=current_user_object)