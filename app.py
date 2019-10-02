import os
from flask import Flask, render_template, redirect, request, url_for, flash, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from bson.json_util import dumps
from werkzeug.urls import url_parse
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import current_user, login_user, logout_user, login_required, LoginManager
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'main_db'
app.config["MONGO_URI"] = os.getenv('MONGO_URI')
app.secret_key = os.environ.get('SECRET_KEY')

mongo = PyMongo(app)
lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'

def connect_current_user_to_database():
    if current_user.is_authenticated:
        current_user_object = mongo.db.users.find_one({"contact.email": current_user.email})
        return current_user_object
    else:
        current_user_object = None
        return current_user_object

@app.route('/')
def index():
    current_user_object = connect_current_user_to_database()
    return render_template('index.html', current_session_user=current_user_object)
    
@app.route('/mentors/search', methods=["GET","POST"])
def mentors_search():
    current_user_object = connect_current_user_to_database()
    if request.method == 'POST':
        name = request.form.get('name').split(' ', 2)
        expertise = request.form.get('expertise').strip().split(",")
        if len(name) == 2:
            users = mongo.db.users.find(
                {"$and" :
                    [{"$or":
                        [{"$and" :
                            [{'first_name':name[0]},
                            {'last_name':name[1]}]
                        },
                        {'expertise': { "$all": expertise }}]
                    },
                    {'looking_to': {"$in":["become a mentor"]}}],
                })
        else:
            users = mongo.db.users.find(
                {"$and" :
                    [{"$or":
                        [{'first_name':name[0]},
                        {'expertise': { "$all": expertise }}
                    ]},
                    {'looking_to': {"$in":["become a mentor"]}}],
                })
        return render_template('search.html', users=users, current_session_user=current_user_object, title="Mentors")
    return render_template('search.html', current_session_user=current_user_object, title="Mentors")
    
@app.route('/mentors')
@login_required
def mentors():
    current_user_object = connect_current_user_to_database()
    title = "Mentors"
    users = mongo.db.users.find({'looking_to': {"$in":["become a mentor"]}})
    return render_template('search.html', users=users, current_session_user=current_user_object, title=title)
    
@app.route('/pair_programmers/search', methods=["GET","POST"])
def pair_programmers_search():
    current_user_object = connect_current_user_to_database()
    if request.method == 'POST':
        name = request.form.get('name').split(' ', 2)
        expertise = request.form.get('expertise').strip().split(",")
        if len(name) == 2:
            users = mongo.db.users.find(
                {"$and" :
                    [{"$or":
                        [{"$and" :
                            [{'first_name':name[0]},
                            {'last_name':name[1]}]
                        },
                        {'expertise': { "$all": expertise }}]
                    },
                    {'looking_to': {"$in":["pair program"]}}],
                })
        else:
            users = mongo.db.users.find(
                {"$and" :
                    [{"$or":
                        [{'first_name':name[0]},
                        {'expertise': { "$all": expertise }}
                    ]},
                    {'looking_to': {"$in":["pair program"]}}],
                })
        return render_template('search.html', users=users, current_session_user=current_user_object, title="Pair Programmers")
    return render_template('search.html', current_session_user=current_user_object, title="Pair Programmers")
    
@app.route('/pair_programmers')
def pair_programmers():
    current_user_object = connect_current_user_to_database()
    title = "Pair Programmers"
    users = mongo.db.users.find({'looking_to': {"$in":["pair program"]}})
    return render_template('search.html', users=users, current_session_user=current_user_object, title=title)

@app.route('/edit_profile')
@login_required
def edit_profile():
    current_user_object = connect_current_user_to_database()
    return render_template('edit_profile.html', current_session_user=current_user_object)
    
@app.route('/user/<user_id>')
@login_required
def user_profile(user_id):
    current_user_object = connect_current_user_to_database()
    user = mongo.db.users.find_one({"_id": ObjectId(user_id)})
    return render_template('user_profile.html', user=user, current_session_user=current_user_object)
    
@app.route('/update_profile', methods=["POST"])
@login_required
def update_profile():
    current_user_object = connect_current_user_to_database()
    users = mongo.db.users
    users.update( {'_id': current_user_object["_id"]},
    {
        '$set': {
            'first_name':request.form.get('first_name'),
            'last_name':request.form.get('last_name'),
            'password': generate_password_hash(request.form.get('password')),
            'description': request.form.get('description'),
            'avatar': request.form.get('avatar'),
            'about': request.form.get('about'),
            'expertise': request.form.get('expertise').strip().split(","),
            'looking_to': request.form.getlist('looking_to'),
            'contact.email':request.form.get('email'),
            'contact.skype':request.form.get('skype'),
            'contact.github':request.form.get('github'),
            'contact.linkedin':request.form.get('linkedin'),
            'contact.discord':request.form.get('discord')
        }
    })
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
    current_user_object = connect_current_user_to_database()
    if request.method == 'POST' and form.validate_on_submit():
        user = mongo.db.users.find_one({"contact.email": form.email.data})
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
    user = mongo.db.users.find_one({"contact.email": email})
    if not user:
        return None
    return User(user['contact']['email'])

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=8080,
            debug=True)