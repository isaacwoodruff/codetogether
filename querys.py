from config import *

def connect_current_user_to_database(current_user):
    if current_user.is_authenticated:
        current_user_object = mongo.db.users.find_one({"contact.email": current_user.email})
        return current_user_object
    else:
        current_user_object = None
        return current_user_object

def mentor_search_query(name, expertise):
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
    
def update_profile_query(form, current_user_object):
    password = request.form.get('password')
    update = mongo.db.users.update( {'_id': current_user_object["_id"]},
    {
        '$set': {
            'first_name':request.form.get('first_name'),
            'last_name':request.form.get('last_name'),
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
    if password is not '':
        user_pass = users.update( {'_id': current_user_object["_id"]},
        {'$set':
            {'password': generate_password_hash(password)}
        })
    else:
        user_pass = ''
    return update, user_pass
        
def find_user_by_email(email):
    return mongo.db.users.find_one({"contact.email": email})

def find_user_by_form_email(form):
    return mongo.db.users.find_one({ "contact.email" : form.email.data})

def create_new_user_query(form):
    return mongo.db.users.insert_one({
                "password": generate_password_hash(form.password.data),
                'first_name': "",
                'last_name': "",
                'description': "",
                'avatar': "",
                'about': "",
                'expertise': "",
                'looking_to': "",
                "contact": {
                    "email" : form.email.data,
                    'skype': "",
                    'github': "",
                    'linkedin': "",
                    'discord': ""
                }
            })