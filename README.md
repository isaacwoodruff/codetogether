# <a href="http://code-together-platform.herokuapp.com/" target="_blank">Code Together</a>

<a href="http://code-together-platform.herokuapp.com/" target="_blank">Code Together</a> was created as a free platform to connect software developers with mentors, and pair programmers to learn, help, and build together.

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
    - [Local Deployment](#local-deployment)
    - [Heroku Deployment](#heroku-deployment)

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
A user of <a href="http://code-together-platform.herokuapp.com/" target="_blank">Code Together</a> expects to:
- Be able to register, login, and logout
- Have their own profile which they can create, read, update or delete
- Search through the database for all mentors and pair programmers
- Search for mentors/pair programmers with a specific expertise
- Search for mentors/pair programmers with a specific name
- View another users profile
- Contact another user

## Wireframes

These wireframes were created using <a href="https://balsamiq.com/" target="_blank">Balsamiq</a>.

- <a href="https://ibb.co/vh6Zwvh" target="_blank">Home</a>
- <a href="https://ibb.co/5YGzSs5" target="_blank">Login/Register</a>
- <a href="https://ibb.co/2qsSbpB" target="_blank">My Profile</a>
- <a href="https://ibb.co/rFmqZzf" target="_blank">Edit Profile</a>
- <a href="https://ibb.co/fvxbKqL" target="_blank">Mentors</a>
- <a href="https://ibb.co/qdCMVmk" target="_blank">Pair programmers</a>
- <a href="https://ibb.co/YTjCRWr" target="_blank">User Profile</a>
- <a href="https://ibb.co/WF8CBTB" target="_blank">Messages</a>

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

##### Global Chat
- Users can chat with each other in this global chatroom
- The messages aren't saved so they will disapear once you close the window

## Features Left To Implement
##### Messaging
- The ability for users to contact each other within the website through the medium of:
    - Private text messaging
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
    - The project uses **MongoDB Atlas** as the database for this project- 
- [AutoPrefixer](https://autoprefixer.github.io/)
    - The project used **AutoPrefixer** to add prefixes in the CSS for cross-browser support.

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
### Validation Tools

These tools were used to test the validity of the code for this project:
- [W3C HTML Validator]( https://validator.w3.org/) was used to validate HTML.
- [W3C CSS validator](https://jigsaw.w3.org/css-validator/) was used to validate CSS.
- [Pythoniter](https://pythoniter.appspot.com/) was used to format python.

### Testing Matrix

A testing matrix was created using google spreadsheets. It details all of the tests to make sure the site is responsive and works on different screen sizes, devices, and browsers. The testing matrix can be found <a href="https://github.com/isaacwoodruff/codetogether/blob/master/testing-matrix.pdf" target="_blank">here</a>.


# Deployment
## Local Deployment
To run this project locally the following must be installed in your IDE:
- [Git](https://git-scm.com/downloads)
- [Python 3](https://www.python.org/downloads/)
- [PIP](https://pip.pypa.io/en/stable/installing/)
- [MongoDB](https://www.mongodb.com/download-center)

### Instructions

1. Follow <a href="https://github.com/isaacwoodruff/codetogether" target="_blank">this link</a> to the main page of the <a href="https://github.com/isaacwoodruff/codetogether" target="_blank">isaacwoodruff/code-together</a> repository.
2. On the right side of the page click the green **Clone or download** button.
3. In the '**Clone with HTTPS**' section, copy the URL for the repository.
4. Open your **terminal/Git Bash**.
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, and then paste the URL that was copied in Step 3 or copy and paste this command:

    `git clone https://github.com/isaacwoodruff/codetogether.git`
    
7. Press **Enter**.
8. You can either 
    - Create a virtual environment and create environment variables for **IP**, **PORT**, **MONGO_URI**, and **SECRET_KEY**.
    - Or edit the app.py file like the following variables:
        ```
        'IP', '127.0.0.1'
        ```
        ```
        'PORT', '5000'
        ```
        ```
        'SECRET_KEY', '<somethingsecret>'
        ```
        ```
        'MONGO_URI', 'mongodb+srv://<username>:<password>@<cluster_name>-ocous.mongodb.net/<database_name>?retryWrites=true&w=majority'
        ```
9. Install all required modules from requirements.txt with the command:
    ```
    pip3 install -r requirements.txt.
    ```
10. Now you can run the website with the command:
    ```
    python3 app.py
    ```
11. You can now access the website at **http://127.0.0.1:5000**

## Heroku Deployment
1. In your terminal create a **requirements.txt** file using the command:
    ```
    pip freeze > requirements.txt
    ```

2. Then create a **Procfile** with the terminal command:
    ```
    echo web: python3 app.py > Procfile
    ```

3. Commit your changes and push to GitHub with the terminal commands:

    ```Note: set your GitHub remote to origin if not done already```
    
    ```
    git add requirements.txt Procfile
    ```
    
    ```
    git commit -m "Your commit message"
    ```
    
    ```
    git push origin
    ```
    
3. Go to <a href="https://heroku.com/" target="_blank">Heroku</a> and create a new app by clicking the **New** button in your dashboard. Set your app name and set the region to whichever is closest to you.

4. In the heroku dashboard of your application, click on **Deploy** then **Deployment method** and select GitHub.

5. Click confirm in the pop up window to link the heroku app to the GitHub repository.

6. In the heroku dashboard of your application, click on **Settings** then **Reveal Config Vars** and set the following:

| Key | Value |
 --- | ---
IP | 0.0.0.0
PORT | 5000
MONGO_URI | `mongodb+srv://<username>:<password>@<cluster_name>-ocous.mongodb.net/<database_name>?retryWrites=true&w=majority`
SECRET_KEY | `<somethingsecret>`
DEBUG | FALSE

To get your MONGO_URI please reference the <a href="https://docs.atlas.mongodb.com/" target="_blank">MongoDB Atlas documentation</a>.

7. In the heroku dashboard of your app you can either click **Deploy** or enable **Automatic Deploys** in the **Automatic Deployment** section.

8. To pick your branch for manual deployment go to the **Manual Deploy** section and set the branch to **master** then click **Deploy Branch**.

9. Your site is now successfully deployed at:
    ```
    your-heroku-app-name.herokuapp.com
    ```

# Credits
### Content
- All written content was created by the developer

### Media
- Some avatars used were from these sources
    - <a href="https://www.flaticon.com/free-icon/man_180665" target="_blank">Flaticon-hipster</a>
    - <a href="https://www.flaticon.com/free-icon/hacker_843331" target="_blank">Flaticon-hacker</a>
- The favicon for this website is from <a href="https://www.flaticon.com/free-icon/code_25185" target="_blank">Flaticon-code</a>
- The index page uses images from these sources 
    - <a href="https://www.freepik.com/free-vector/connected-concept-illustration_5568958.htm">Freepik-image-1</a>
    - <a href="https://www.freepik.com/premium-vector/online-training-flat-design-man-s-character-is-sitting-desk-studying-online-with-online-course-online-examination-concept_4852682.htm">Freepik-image-2</a>
    - <a href="https://www.freepik.com/free-vector/managers-looking-chart-monitor_4530296.htm" target="_blank">Freepik-image-3</a>
    - <a href="https://www.freepik.com/free-vector/communication-flat-icon_4167276.htm" target="_blank">Freepik-image-4</a>
- The GitHub logo in the footer was sourced from <a href="https://www.flaticon.com/free-icon/github-logo_37318" target="_blank">FlatIcon-GitHub</a>
- All wireframe images were created by the developer and uploaded to <a href="https://imgbb.com" target="_blank">imgBB</a>

### Code
- The nav bar and mobile nav bar were taken from <a href="https://materializecss.com/" target="_blank">Materialize</a> and modified to suit the website
- The tabbed content structure on the user profiles was taken from a <a href="https://codepen.io/cssjockey/pen/jGzuK" target="_blank">CodePen</a> by Mohit Aneja and modified heavily
- The login system was adapted from <a href="https://boh717.github.io/post/flask-login-and-mongodb/" target="_blank">How to use MongoDB (and PyMongo) with Flask-Login</a>
- The messaging functionality was created from parts of this article <a href="https://codeburst.io/building-your-first-chat-application-using-flask-in-7-minutes-f98de4adfa5d" target="_blank">Building your first Chat Application using Flask in 7 minutes</a>

### Acknowledgements
- The <a href="https://imgbb.com" target="_blank">flask-login</a>, and <a href="https://imgbb.com" target="_blank">flask-socketio</a> docs were invaluable during the development process
- <a href="https://materializecss.com/" target="_blank">Materialize</a> sped up the development process considerably
- Thanks to <a href="https://github.com/aaronsnig501" target="_blank">Aaron Sinnott</a> for his suggestions throughout the project