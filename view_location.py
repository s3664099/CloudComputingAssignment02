import database_utils as database
from user import user
import trans_utils as translate
import get_details as details

def view_location(longitude, latitude):

    db = database.database_utils()

    location_data = db.get_Place_Info(latitude, longitude)
    location = {}
    template_values = {}
    reviews = []
    _localtype = None

    for localeName, address, email, telephone, website, description, picture, localtype in location_data:
        location = {
            "name": localeName,
            "address": address,
            "email": email,
            "telephone": telephone,
            "website": website,
            "description": description,
            "picture" : picture,
            "localtype": localtype
        }
        _localtype = localtype

    reviews_t = db.get_Reviews(latitude, longitude)

    for username, review in reviews_t:
        review_details = {
            "username": username,
            "review": review
        }
        reviews.append(review_details)

        """
        userKey = self.session.get('user')

        if (userKey != None):
            user_key = ndb.Key("User", userKey)
            user = user_key.get()
            template_values['user'] = user.firstName
        """
    if user.logged_in == True:
        template_values[user] = user.name


    if _localtype == "Pub/Bar":
        results = db.get_pub_info(latitude, longitude)
        template_values['pub_info'] = details.get_pub_details(results)
            

    if _localtype == "Cafe":
        results = db.get_cafe_info(latitude, longitude)
        template_values['cafe_info'] = details.get_cafe_details(results)

    template_values['localtype'] = _localtype
    template_values['view_place'] = translate.view_page(user.language)
    template_values['location'] = location
    template_values['longitude'] = longitude
    template_values['latitude'] = latitude
    template_values['reviews'] = reviews

    return template_values	