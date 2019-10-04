# Code Together

Code Together was created as a free platform to connect software developers with mentors, and pair programmers to learn, help, and build together.

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
    - [Local Deployment](#how-to-deploy-this-project-locally)

7. [Credits](#credits)

# UX
## Goals
The goal of this project is to create a web application to connect software developers with mentors, and pair programmers. It's aim was to be built in Python in conjunction with the Flask framework, and MongoDB to enable users to create, read, update and delete (CRUD).

### User Goals
The target audience for this project is:
- Developers looking to find a mentor
- Developers looking to find a pair programming partner
- Developers looking to start mentoring other developers

The user goals are to have:
- A platform that easily connects developers with mentors, and pair programmers
- A simple, user friendly search functionality to find who they're looking for
- Their own profile with relevant information that they can edit themselves
- The ability to contact another developer

## User Stories
A user of Code Together expects to:
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
- You can search by:
    - First name and/or last name
    - Job Title/Description
    - Expertise

##### Pair Programmers Page
- This page shows all of the people looking to pair program with other developers. It also has search functionality.
- You can search by:
    - First name and/or last name
    - Job Title/Description
    - Expertise

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
