from config import *

def connect_current_user_to_database(current_user):
    if current_user.is_authenticated:
        current_user_object = mongo.db.users.find_one({"contact.email": current_user.email})
        return current_user_object
    else:
        current_user_object = None
        return current_user_object

def mentor_search_query(name, expertise):
    name = name.islower()
    expertise = expertise.lower()
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
        return users
    else:
        users = mongo.db.users.find(
            {"$and" :
                [{"$or":
                    [{'first_name':name[0]},
                    {'expertise': { "$all": expertise }}
                ]},
                {'looking_to': {"$in":["become a mentor"]}}],
            })
        return users

def all_mentors_query():
    return mongo.db.users.find({'looking_to': {"$in":["become a mentor"]}})
    
def pair_programmers_search_query(name, expertise):
    name = name.lower()
    expertise = expertise.lower()
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
        return users
    else:
        users = mongo.db.users.find(
            {"$and" :
                [{"$or":
                    [{'first_name':name[0]},
                    {'expertise': { "$all": expertise }}
                ]},
                {'looking_to': {"$in":["pair program"]}}],
            })
        return users
                
def all_pair_programmers_query():
    return mongo.db.users.find({'looking_to': {"$in":["pair program"]}})
    
def user_profile_query(user_id):
    return mongo.db.users.find_one({"_id": ObjectId(user_id)})
    
def update_profile_query(current_user_object):
    password = request.form.get('password')
    first_name = request.form.get('first_name').lower()
    last_name = request.form.get('last_name').lower()
    description = request.form.get('description').lower()
    avatar = request.form.get('avatar')
    about = request.form.get('about')
    expertise = request.form.get('expertise').strip().split(",")
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
        users.update( {'_id': current_user_object["_id"]},
        {'$set':
            {'password': generate_password_hash(password)}
        })
    else:
        user_pass = ''
        
def find_user_by_email(email):
    return mongo.db.users.find_one({"contact.email": email})

def find_user_by_form_email(form):
    email = form.email.data.lower()
    return mongo.db.users.find_one({ "contact.email" : email})

def create_new_user_query(form):
    email = form.email.data.lower()
    mongo.db.users.insert_one({
        "password": generate_password_hash(form.password.data),
        'first_name': "",
        'last_name': "",
        'description': "",
        'avatar': "",
        'about': "",
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