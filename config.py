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
from flask_socketio import SocketIO, send, emit


app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'main_db'
app.config["MONGO_URI"] = os.getenv('MONGO_URI')
app.secret_key = os.environ.get('SECRET_KEY')


mongo = PyMongo(app)


lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'


socketio = SocketIO(app, cors_allowed_origins='*')
