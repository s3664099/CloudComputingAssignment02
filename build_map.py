import database_utils as database
import trans_utils as translate

#Establish a class to hold variables pulled from the static HTML page
class search ():
    locale_type = "All"
    locale_place = "Sunbury"

class language():
    language = 'en'

class show_locations():
	selection = "everything"

class place():
    lng = 0
    lat = 0

def get_values():

	template_values = {}

	"""
    client = bigquery.Client()
    tablecode = datetime.now().strftime('%Y%m%d')
    dailyLogins = 0

    try:
        query = """
        #SELECT count(*) FROM `map-cc-assignment.LoginData.appengine_googleapis_com_request_log_""" + tablecode + """` 
        #where DATE(timestamp) = CURRENT_DATE LIMIT 1000;
	"""
        query_job = client.query(query)
        results = query_job.result()

        dailyLogins = 0

        for row in results:
            dailyLogins = row.f0_

    except:
        pass
    """

	if search.locale_type != "":
		template_values = perform_search(language.language)

	"""    
    userKey = self.session.get('user')

    if (userKey != None):
        user_key = ndb.Key("User", userKey)
        user = user_key.get()
        template_values['user'] = user.firstName

    template_values['loginCount'] = dailyLogins
	"""

	return template_values

#This function is where all of the database searches are performed
def perform_search(language):

    #Set up the values to be used in this function
    locations = []
    visit_places = []
    location_details = {}
    template_values = {}
    template_values['visited_places'] = None
    visited = False
    results = None

    db = database.database_utils()

    if show_locations.selection == "visited":
        results = db.get_all_open_locations(language)
        visited_results = db.get_all_visited()
        visited = True
    elif show_locations.selection == "beer":
        results = db.get_all_open_type("place.localtype = 'Pub/Bar'", language)
    elif show_locations.selection == "coffee":
        results = db.get_all_open_type("place.localtype = 'Cafe'", language)
    elif show_locations.selection == "beercoffee":
        results = db.get_all_open_type("place.localtype = 'Cafe' OR place.localtype = 'Pub/Bar'", language)
    else:
        results = db.get_all_open_locations(language)

    #Now that we have performed the queries, the results are processed and stored
    #in the dictionary which is then passed back to the main function
    for x_coord, y_coord, likes, localeName, description_fr, icon in results:

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
            "icon": icon,
            "name": localeName,
            "description": description_fr
            }
        locations.append(location_details) 

    if visited == True:   
        for x_coord, y_coord in visited_results:
            visited_places = {
                "x_coord": x_coord,
                "y_coord": y_coord
            }
            visit_places.append(visited_places)
        template_values['visited_places'] = visit_places

    main_page = translate.main_page(language)

    #The results are stored in the template values for use on the webpage
    template_values['location_details'] = locations
    template_values['visit_selected'] = visited
    template_values['main_page'] = main_page
    template_values['selection'] = show_locations.selection
           
    return template_values

#Method to change the what is visible on the map.
def change_locations(option):

	if option == "beer":
		show_locations.selection = "beer"
	elif option == "coffee":
		show_locations.selection = "coffee"
	elif option == "beercoffee":
		show_locations.selection = "beercoffee"
	elif option == "visited":
		show_locations.selection = "visited"
	else:
		show_locations.selection = "everything"