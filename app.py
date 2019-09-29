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
    user = mongo.db.users.find_one({u"_id": ObjectId('5d84afe31c9d440000f48258')})
    return render_template('edit-profile.html', user=user)
    
@app.route('/user/<user_id>')
def user_profile(user_id):
    user = mongo.db.users.find_one({u"_id": ObjectId(user_id)})
    return render_template('user_profile.html', user=user)
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=8080,
            debug=True)