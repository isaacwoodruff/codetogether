import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'main_db'
app.config["MONGO_URI"] = os.getenv('MONGO_URI')

mongo = PyMongo(app)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/edit_profile')
def edit_profile():
    user = mongo.db.users.find_one({"_id": ObjectId('5d90d9dd1c9d440000f6a0b6')})
    return render_template('edit_profile.html', user=user)
    
@app.route('/user/<user_id>')
def user_profile(user_id):
    user = mongo.db.users.find_one({"_id": ObjectId(user_id)})
    return render_template('user_profile.html', user=user)
    
@app.route('/update_profile', methods=["POST"])
def update_profile():
    user = mongo.db.users
    user.update( {'_id': ObjectId("5d90d9dd1c9d440000f6a0b6")},
    {
        '$set': {
            'first_name':request.form.get('first_name'),
            'last_name':request.form.get('last_name'),
            'password': request.form.get('password'),
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
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=8080,
            debug=True)