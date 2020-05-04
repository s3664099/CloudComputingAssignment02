# Copyright 2013 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START gae_python_mysql_app]
from google.appengine.ext import ndb

#Imports
import os
import hashlib
import binascii
import webapp2
import jinja2
import database_utils as database

from webapp2_extras import sessions

#This function sets up the jinj enviroment
JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

#Establish a class to hold variables pulled from the static HTML page
class search ():
    locale_type = "All"
    locale_place = "Sunbury"

class User(ndb.Model):
    """Models a user."""
    firstName = ndb.StringProperty()
    surname = ndb.StringProperty()
    email = ndb.StringProperty()
    password = ndb.StringProperty()
    salt = ndb.StringProperty()

# https://stackoverflow.com/a/12737074
# Maintains session data.

class BaseHandler(webapp2.RequestHandler):
    def dispatch(self):
        # Get a session store for this request.
        self.session_store = sessions.get_store(request=self.request)

        try:
            # Dispatch the request.
            webapp2.RequestHandler.dispatch(self)
        finally:
            # Save all sessions.
            self.session_store.save_sessions(self.response)

    @webapp2.cached_property
    def session(self):
        # Returns a session using the default cookie key.
        return self.session_store.get_session()

#This class is the main page handler. The code in this class processes what gets placed
#Onto the HTML file.
class MainPage(BaseHandler):

    #The get function, while it sounds odd, the get is actually being called
    #from the HTML file as opposed to this file.
    def get(self):
        """Simple request handler that shows all of the MySQL variables."""

        #Sets an empty dictionary to handle the template values
        #These are the values that wull be used by the HTML file
        template_values = {}

        if search.locale_type != "":
            template_values = MainPage.perform_search(self)

        userKey = self.session.get('user')
        template_values['user'] = userKey


        #This code sends the template values to the HTML file.
        #The first line sets up the template values, the second line renders the webpage.
        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render(template_values))

#    def database_manip(self, db):

    #This function is where all of the database searches are performed
    def perform_search(self):

        #Set up the values to be used in this function
        locations = []
        location_details = {}
        template_values = {}

        db = database.database_utils()

        results = db.get_all_locations()

        #Now that we have performed the queries, the results are processed and stored
        #in the dictionary which is then passed back to the main function
        for x_coord, y_coord, likes, icon in results:

            rating = 0

            if (likes == 0):
                rating = 1
            elif (likes == 20):
                rating = 2
            elif (likes == 50):
                rating =3
            elif (likes == 80):
                rating = 4
            else:
                rating = 5

            location_details = {
                "x_coord": x_coord,
                "y_coord": y_coord,
                "rating": rating,
                "icon": icon
                }
            locations.append(location_details) 

        #The results are stored in the template values for use on the webpage

        template_values['location_details'] = locations
           
        return template_values

#This is the handler for recieving data from the webpage.
class Search(webapp2.RequestHandler):
    def post(self):

        #These functions are where the data is recieved and stored
        #in the class to hold the data. The tags inside the get correspond
        #with the name in the form on the html page
        search.locale_type = self.request.get('type')
        search.locale_place = self.request.get('suburb')

        #The program is then sent to the MainPage to update the page
        self.redirect('/')

class Login(BaseHandler):

    def get(self):

        template = JINJA_ENVIRONMENT.get_template('login.html')
        self.response.write(template.render())

    def post(self):
        enteredEmail = self.request.get('email')
        enteredPassword = self.request.get('password')

        # Hash the email and attempt to get a key.
        hasher = hashlib.sha256()
        hasher.update(enteredEmail)
        hashedEmail = hasher.hexdigest()

        # Constructing key to get user details.
        user_key = ndb.Key("User", hashedEmail)
        user = user_key.get()

        # If no user, refuse sign in.
        if (user is None):
            template = JINJA_ENVIRONMENT.get_template('login.html')
            self.response.write(template.render(message = "There is no account associated with that email address."))
        else:
            # Check password.
            storedPass = user.password
            storedSalt = user.salt

            pwdhash = hashlib.pbkdf2_hmac('sha256', enteredPassword.encode('utf-8'), storedSalt.encode('ascii'), 100000)
            pwdhash = binascii.hexlify(pwdhash).decode('ascii')

            if (pwdhash == storedPass):
                # Redirect to wherever needed.
                self.session['user'] = hashedEmail
                self.redirect('/')
            else:
                template = JINJA_ENVIRONMENT.get_template('login.html')
                self.response.write(template.render(message = "Your password was incorrect."))

class SignUpPage(webapp2.RequestHandler):

    def get(self):

        template = JINJA_ENVIRONMENT.get_template('signup.html')
        self.response.write(template.render())

    def post(self):
        # Check for form errors.
        isError = False

        firstName = self.request.get('firstname')
        firstNameError = ""

        if (firstName == ""):
            firstNameError = "Please enter a valid first name."
            isError = True

        surname = self.request.get('surname')
        surnameError = ""

        if (surname == ""):
            surnameError = "Please enter a valid surname."   
            isError = True     

        email = self.request.get('email')
        emailError = ""
        
        # Will need to add regex check.
        if (email == ""):
            emailError = "Please enter a valid email address."
            isError = True

        password = self.request.get('password')
        confirmPass = self.request.get('confirmpassword')   
        passwordError = ""

        if (password == "" or confirmPass == ""):
            passwordError = "Please enter a password."
            isError = True
        
        if (password != confirmPass):
            passwordError = "Your passwords do not match."
            isError = True

        if (isError):
            # Redirect to Sign Up page with error messages.
            template = JINJA_ENVIRONMENT.get_template('signup.html')
            self.response.write(template.render(firstNameError = firstNameError, surnameError = surnameError, 
            emailError = emailError, passwordError = passwordError))
        else:
            # Hashing email to use as a key.
            hasher = hashlib.sha256()
            hasher.update(email)

            # Check if there is an account.
            user_key = ndb.Key("User", hasher.hexdigest())
            user = user_key.get()

            if (user is None):
                # Generating a crypto-safe random string to use as a salt.
                # https://www.vitoshacademy.com/hashing-passwords-in-python/
                salt = hashlib.sha256(os.urandom(20)).hexdigest().encode('ascii')

                # Hashing password with the salt.
                pHash = hashlib.pbkdf2_hmac('sha256', password.encode("utf-8"), salt, 100000)
                hashedPass = binascii.hexlify(pHash)

                # Creating Datastore entity.
                newUser = User(id = hasher.hexdigest(), firstName = firstName, surname = surname, email = email, password = hashedPass, salt = salt)
                newUser.put()
                template = JINJA_ENVIRONMENT.get_template('login.html')
                self.response.write(template.render(message = "Your account was created! Sign in below."))
            else:
                # Display error if there is already an account.
                emailError = "There is already an account associated with that email address."
                template = JINJA_ENVIRONMENT.get_template('signup.html')
                self.response.write(template.render(firstNameError = firstNameError, surnameError = surnameError, 
                emailError = emailError, passwordError = passwordError))

class SignOut(BaseHandler):
    def get(self):
        self.session['user'] = None
        self.redirect('/')

class Review(webapp2.RequestHandler):

    def get(self):
        template = JINJA_ENVIRONMENT.get_template("review.html")
        self.response.write(template.render())

    def post(self):
        self.response.write(self.request.POST)
    
# Config for Session Storage.
config = {}
config['webapp2_extras.sessions'] = {
    'secret_key': 'test',
}

#This function defines where data is to go. 
app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/search', Search),
    ('/login', Login),
    ('/signup', SignUpPage),
    ('/signout', SignOut),
    ('/review', Review)
], debug=True, config=config)

# [END gae_python_mysql_app]
