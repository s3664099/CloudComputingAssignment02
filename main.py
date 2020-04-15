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

"""
Sample App Engine application demonstrating how to connect to Google Cloud SQL
using App Engine's native unix socket or using TCP when running locally.

For more information, see the README.md.
"""

# [START gae_python_mysql_app]

#Imports
import os
import MySQLdb
import webapp2
import jinja2

#This function sets up the jinj enviroment
JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

# These environment variables are configured in app.yaml.
CLOUDSQL_CONNECTION_NAME = os.environ.get('CLOUDSQL_CONNECTION_NAME')
CLOUDSQL_USER = os.environ.get('CLOUDSQL_USER')
CLOUDSQL_PASSWORD = os.environ.get('CLOUDSQL_PASSWORD')
CLOUDSQL_DB = os.environ.get('CLOUDSQL_DB')

#Establish a class to hold variables pulled from the static HTML page
class search ():
    locale_type = "All"
    locale_place = "Sunbury"


#Function to connect to the SQL database in google cloud
def connect_to_cloudsql():
    # When deployed to App Engine, the `SERVER_SOFTWARE` environment variable
    # will be set to 'Google App Engine/version'.
    if os.getenv('SERVER_SOFTWARE', '').startswith('Google App Engine/'):
        # Connect using the unix socket located at
        # /cloudsql/cloudsql-connection-name.
        cloudsql_unix_socket = os.path.join(
            '/cloudsql', CLOUDSQL_CONNECTION_NAME)

        #This function here is what you use to connect to the SQL database
        db = MySQLdb.connect(
            unix_socket=cloudsql_unix_socket,
            user=CLOUDSQL_USER,
            passwd=CLOUDSQL_PASSWORD,
            db=CLOUDSQL_DB,
            charset='utf8')

    # If the unix socket is unavailable, then try to connect using TCP. This
    # will work if you're running a local MySQL server or using the Cloud SQL
    # proxy, for example:
    #
    #   $ cloud_sql_proxy -instances=your-connection-name=tcp:3306
    #
    else:
        db = MySQLdb.connect(
            host='127.0.0.1', user=CLOUDSQL_USER, passwd=CLOUDSQL_PASSWORD, db=CLOUDSQL_DB, charset='utf8')

    return db

#This class is the main page handler. The code in this class processes what gets placed
#Onto the HTML file.
class MainPage(webapp2.RequestHandler):

    #The get function, while it sounds odd, the get is actually being called
    #from the HTML file as opposed to this file.
    def get(self):
        """Simple request handler that shows all of the MySQL variables."""

        #Sets an empty dictionary to handle the template values
        #These are the values that wull be used by the HTML file
        template_values = {}

        if search.locale_type != "":
            template_values = MainPage.perform_search(self)

        #This code sends the template values to the HTML file.
        #The first line sets up the template values, the second line renders the webpage.
        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render(template_values))

#    def database_manip(self, db):

    #This function is where all of the database searches are performed
    def perform_search(self):

        #Set up the values to be used in this function
        locale_type = search.locale_type
        locale_place = search.locale_place
        locations = []
        location_details = {}
        template_values = {}
        towns = []

        number = 0
        db = connect_to_cloudsql()
        #MainPage.database_manip(self, db)

        #Sets up the function that performs the searches and stores the results
        #The queries are below.
        cursor = db.cursor()
        if locale_type == 'All':
            cursor.execute("SELECT localename, address, telephone, localtype FROM place WHERE town = '"+locale_place+"' and state = 'Vic' LIMIT 20")
        else:
            cursor.execute("SELECT localename, address, telephone, localtype FROM place WHERE localtype ='"+locale_type+"' and town = '"+locale_place+"' and state = 'Vic' LIMIT 20")

        #Now that we have performed the queries, the results are processed and stored
        #in the dictionary which is then passed back to the main function
        for locale, address, telephone, localtype in cursor.fetchall():
            number +=1

            if number == 1:
                location_details = {
                    "locale": locale,
                    "address": address,
                    "telephone": telephone,
                    "localtype": localtype,
                    "locale1": " ",
                    "address1": " ",
                    "state1": " ",
                    "localtype1": " "
                }
            else:
                location_details.update({"locale1" : locale})
                location_details.update({"address1": address})
                location_details.update({"telephone1": telephone})
                location_details.update({"localtype1": localtype})
                locations.append(location_details) 
                number = 0

        for location in locations:
            cursor.execute("SELECT icon, localtype FROM localtype WHERE localtype = '"+str(location.get("localtype"))+"'")
            for icon, localtype in cursor.fetchall():
                location.update({"localtype": icon})
            cursor.execute("SELECT icon, localtype FROM localtype WHERE localtype = '"+str(location.get("localtype1"))+"'")
            for icon, localtype in cursor.fetchall():
                location.update({"localtype1": icon})

        cursor.execute("SELECT town, state FROM location WHERE state = 'Vic'")

        for town, state in cursor.fetchall():
            town_details = {
                "town": town,
            }
            towns.append(town_details)

        #The results are stored in the template values for use on the webpage
        template_values = {
           'location_details': locations,
           'towns': towns
        }           
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


#This function defines where data is to go. 
app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/search', Search)
], debug=True)

# [END gae_python_mysql_app]
