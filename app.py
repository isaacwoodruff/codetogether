import os
from flask import Flask, render_template
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'main_db'
app.config["MONGO_URI"] = os.getenv('MONGO_URI')

mongo = PyMongo(app)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/edit-profile')
def edit_profile():
    return render_template('edit-profile.html')
    
@app.route('/user/<username>')
def user_profile(username):
    user = mongo.db.users.find_one({u"_id": ObjectId(username)})
    return render_template('user_profile.html', user=user)
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=8080,
            debug=True)