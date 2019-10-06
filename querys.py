from config import *

"""
The connect_current_user_to_database() function check if the current_user is
authenticated. If they are then it querys the users collection for the user and
assigns the document to the variable current_user_object. This connects the 
flask-login current_user with the user in the database
"""

def connect_current_user_to_database(current_user):
    if current_user.is_authenticated:
        current_user_object = mongo.db.users.find_one({"contact.email": current_user.email})
        return current_user_object
    else:
        current_user_object = None
        return current_user_object

"""
The user_search_query takes 3 parameters, name, expertise, and search_type. The
search_type will decide whether to look for mentors or pair programmers.
"""

def user_search_query(name, expertise, search_type):
    if search_type == "Mentors":
        search_type = "become a mentor"
    else:
        search_type = "pair program"

    """
    If the name and expertise have values in them, it checks to see if name has 2 words.
    If it has 2 then it querys the users collection for 4 key/values which all have
    to be present in one user document. It doesn't find the user if its missing one
    field. If name has got less than 2 words the query is the same except it querys the
    first_name OR last_name
    """

    if name != [""] and expertise != [""]:
        if len(name) == 2:
            users = mongo.db.users.find(
                {"$and" :
                    [{'first_name':name[0]},
                    {'last_name':name[1]},
                    {'expertise': { "$all": expertise }},
                    {'looking_to': {"$in":[search_type]}}]
                })
            return users
        else:
            users = mongo.db.users.find(
                {"$and" :
                    [{"$or":
                        [{'first_name':name[0]},
                        {'last_name':name[0]}
                    ]},
                    {'expertise': { "$all": expertise }},
                    {'looking_to': {"$in":[search_type]}}]
                })
            return users
    
    """
    If their is not a value in either name or expertise, the query is the same as the 
    one above except that it lets the user search by name OR expertise. So one
    field can be empty
    """
    
    else:
        if len(name) == 2:
            users = mongo.db.users.find(
                {"$and" :
                    [{"$or":
                        [{"$and" :
                            [{'first_name':name[0]},
                            {'last_name':name[1]}
                        ]},
                        {'expertise': { "$all": expertise }}]
                    },
                    {'looking_to': {"$in":[search_type]}}]
                })
            return users
        else:
            users = mongo.db.users.find(
                {"$and" :
                    [{"$or":
                        [{'first_name':name[0]},
                        {'last_name':name[0]},
                        {'expertise': { "$all": expertise }}
                    ]},
                    {'looking_to': {"$in":[search_type]}}]
                })
            return users
            
def all_mentors_query():
    return mongo.db.users.find({'looking_to': {"$in":["become a mentor"]}})
  
def all_pair_programmers_query():
    return mongo.db.users.find({'looking_to': {"$in":["pair program"]}})
    
def user_profile_query(user_id):
    return mongo.db.users.find_one({"_id": ObjectId(user_id)})

"""
The update_profile_query takes all the fields from the form on edit_profile and
updates the relevant user document in the users collection. If password field is
not empty then it will hash the password before updating it in the user document
"""

def update_profile_query(current_user_object):
    password = request.form.get('password')
    first_name = request.form.get('first_name').lower()
    last_name = request.form.get('last_name').lower()
    description = request.form.get('description').lower()
    avatar = request.form.get('avatar')
    about = request.form.get('about')
    expertise = request.form.get('expertise').lower().strip().split(",")
    looking_to = request.form.getlist('looking_to')
    email = request.form.get('email').lower()
    skype = request.form.get('skype').lower()
    github = request.form.get('github').lower()
    linkedin = request.form.get('linkedin').lower()
    discord = request.form.get('discord').lower()
    mongo.db.users.update( {'_id': current_user_object["_id"]},
    {
        '$set': {
            'first_name': first_name,
            'last_name': last_name,
            'description': description,
            'avatar': avatar,
            'about': about,
            'expertise': expertise,
            'looking_to': looking_to,
            'contact.email': email,
            'contact.skype': skype,
            'contact.github': github,
            'contact.linkedin': linkedin,
            'contact.discord': discord
        }
    })
    if password is not '':
        mongo.db.users.update( {'_id': current_user_object["_id"]},
        {'$set':
            {'password': generate_password_hash(password)}
        })
        
def find_user_by_email(email):
    return mongo.db.users.find_one({"contact.email": email})

def find_user_by_form_email(form):
    email = form.email.data.lower()
    return mongo.db.users.find_one({ "contact.email" : email})

"""
The create_new_user_query takes the form data from the register view and inserts
a new document to the users collection. It hashes the password before insertion
and inserts a placeholder for avatar and about
"""

def create_new_user_query(form):
    email = form.email.data.lower()
    mongo.db.users.insert_one({
        "password": generate_password_hash(form.password.data),
        'first_name': "",
        'last_name': "",
        'description': "",
        'avatar': "https://image.flaticon.com/icons/svg/843/843331.svg",
        'about': "Write a bit about yourself here",
        'expertise': "",
        'looking_to': "",
        "contact": {
            "email" : email,
            'skype': "",
            'github': "",
            'linkedin': "",
            'discord': ""
        }
    })
    
def delete_user_query(current_user_object):
    mongo.db.users.delete_one({"_id" : current_user_object['_id']})