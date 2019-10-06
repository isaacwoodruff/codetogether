# [Code Together](http://code-together-platform.herokuapp.com/)

[Code Together](http://code-together-platform.herokuapp.com/) was created as a free platform to connect software developers with mentors, and pair programmers to learn, help, and build together.

## Table of Contents

1. [UX](#ux)
    - [Goals](#goals)
    - [User Stories](#user-stories)
    - [Wireframes](#wireframes)

2. [Features](#features)
    - [Existing Features](#existing-features)
    - [Features Left to Implement](#features-left-to-implement)

3. [Information Architecture](#information-architecture)

4. [Technologies Used](#technologies-used)

5. [Testing](#testing)

6. [Deployment](#deployment)
    - [Heroku Deployment](#heroku-deployment)
    - [Local Deployment](#local-deployment)

7. [Credits](#credits)

# UX
## Goals
The goal of this project is to create a web application to connect software developers with mentors, and pair programmers. It's aim was to be built in Python in conjunction with the Flask framework, and MongoDB to enable users to create, read, update and delete (CRUD).

### User Goals
The target audience for this project are:
- Developers looking to find a mentor
- Developers looking to find a pair programming partner
- Developers looking to start mentoring other developers

The user goals are to have:
- A platform that easily connects developers with mentors, and pair programmers
- A simple, user friendly search functionality to find who they're looking for
- Their own profile with relevant information that they can edit themselves
- The ability to contact another developer

## User Stories
A user of [Code Together](http://code-together-platform.herokuapp.com/) expects to:
- Be able to register, login, and logout
- Have their own profile which they can create, read, update or delete
- Search through the database for all mentors and pair programmers
- Search for mentors/pair programmers with a specific expertise
- Search for mentors/pair programmers with a specific name
- View another users profile
- Contact another user

## Wireframes

These wireframes were created using [Balsamiq](https://balsamiq.com/).

- [Home](https://ibb.co/vh6Zwvh)
- [Login/Register](https://ibb.co/5YGzSs5)
- [My Profile](https://ibb.co/2qsSbpB)
- [Edit Profile](https://ibb.co/rFmqZzf)
- [Mentors](https://ibb.co/fvxbKqL)
- [Pair programmers](https://ibb.co/qdCMVmk)
- [User Profile](https://ibb.co/YTjCRWr)
- [Messages](https://ibb.co/WF8CBTB)

# Features
## Existing Features
##### Navbar
- For users who are not logged in, only the following links are visible:
    1. Mentors
    2. Pair Programmers
    3. Login/Register
    
- For users who are logged in, the following links are visible: 
    1. Mentors
    2. Pair Programmers
    3. A circular user icon (when clicked it displays a dropdown menu)
        - Profile
        - Messages
        - Log out

##### Home Page
- This is used as the landing page. It gives some information about what the website is and gives users the option to register or login.

##### Login Page
- This page displays the form that users can use to login so that they can gain access to all the features of the website. It also gives an option that will bring you to the register page.

##### Register Page
- This page displays the form that users can use to register an account.

##### Edit Profile Page
- This page displays the form that users can use to edit their profile.

##### My Profile Page
- This is the logged in users own profile page that's automatically generated with the information they provided to the database.

##### User Profile Page
- This is the profile page of another user that isn't the one logged in. It is also automatically generated with the information they provided to the database.

##### Mentors Page
- This page shows all of the people looking to mentor other developers. It also has search functionality.
- A user can search by:
    - First name and/or last name
    - Expertise
- A user can click on an expertise tag and it will automatically search for everyone with that expertise e.g Python

##### Pair Programmers Page
- This page shows all of the people looking to pair program with other developers. It also has search functionality.
- A user can search by:
    - First name and/or last name
    - Expertise
- A user can click on an expertise tag and it will automatically search for everyone with that expertise e.g Python

## Features Left To Implement
##### Messaging
- The ability for users to contact each other within the website through the medium of:
    - Text messaging
    - Screen share
    - Multiplayer live code share

##### Forgot Password Option
- Have the option to get the users password sent to their email if a user forgets it

# Information Architecture
A MongoDB NoSQL database was used in the creation of this website.

#### Users Collection
This is the JSON structure of the users collection:

```
{
    _id : ObjectId(),
    first_name : String,
    last_name : String,
    password : Encrypted String,
    description : String,
    avatar : String,
    about : String,
    expertise : Array,
    looking_to : Array,
    contact : {
        email : String,
        skype : String,
        github : String,
        linkedin : String,
        discord : String,
    }
}

```

# Technologies Used

### Tools
- [Cloud9](https://aws.amazon.com/cloud9/) 
    - The IDE **Cloud9** was used throughout the project for development.
- [Git](https://git-scm.com)
    - The project uses **Git** for version control during the development process. 
- [GitHub](https://github.com/)
    - The project uses **GitHub** for a remote repository.
- [Balsamiq](https://balsamiq.com/)
    - The project used **Balsamiq** to build wireframes in the planning stage of development.
- [Google Chrome - Dev Tools](https://www.google.com/chrome/)
    - The project used **Google Chrome - Dev Tools** to test responsiveness, to debug code by utilising breakpoints and the console, and to speed up the design process.
- [PIP](https://pip.pypa.io/en/stable/installing/)
    - The project used **PIP** to install the tools needed in this project.
- [MongoDB Atlas](https://www.mongodb.com/cloud/atlas)
    - The project uses **MongoDB Atlas** as the database for this project

### Libraries
- [JQuery](https://jquery.com)
    - The project uses **JQuery** to simplify DOM manipulation.
- [Materialize](https://materializecss.com/)
    - The project uses the **Materialize** framework to help create a responsive design.
- [Material Icons](https://material.io/resources/icons/)
    - The project uses **Material Icons** to create icons.
- [PyMongo](https://api.mongodb.com/python/current/)
    - The project uses **PyMongo** to facilitate communication between Python and MongoDB.
- [Flask](https://flask.palletsprojects.com/en/1.0.x/)
    - The project uses **Flask** to dynamically render pages.
- [Jinja](http://jinja.pocoo.org/docs/2.10/)
    - The project uses **Jinja** to efficiently provide data from the backend to the templates.
- [Flask-Login](https://flask-login.readthedocs.io/en/latest/)
    - The project uses **Flask-Login** to handle user sessions for login functionality.
- [Flask-WTF](https://flask-wtf.readthedocs.io/en/stable/)
    - The project uses **Flask-WTF** to effectively handle form data.
- [Flask-SocketIO](https://flask-socketio.readthedocs.io/en/latest/)
    - The project uses **Flask-SocketIO** to handle messaging functionality between users.

### Programming Languages
- This project uses **HTML**, **CSS**, **JavaScript** and **Python**.

# Testing

# Deployment
## Heroku Deployment

## Local Deployment

# Credits