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

import MySQLdb
import os
import logging

class database_utils:

	# These environment variables are configured in app.yaml.
	CLOUDSQL_CONNECTION_NAME = os.environ.get('CLOUDSQL_CONNECTION_NAME')
	CLOUDSQL_USER = os.environ.get('CLOUDSQL_USER')
	CLOUDSQL_PASSWORD = os.environ.get('CLOUDSQL_PASSWORD')
	CLOUDSQL_DB = os.environ.get('CLOUDSQL_DB')
	db = None

	#Initiates the connection to the database
	def __init__(self):
	    # When deployed to App Engine, the `SERVER_SOFTWARE` environment variable
    	# will be set to 'Google App Engine/version'.

		if os.getenv('SERVER_SOFTWARE', '').startswith('Google App Engine/'):
    	    # Connect using the unix socket located at
    	    # /cloudsql/cloudsql-connection-name.
			cloudsql_unix_socket = os.path.join(
			'/cloudsql', self.CLOUDSQL_CONNECTION_NAME)

    	    #This function here is what you use to connect to the SQL database
			self.db = MySQLdb.connect(
				unix_socket=cloudsql_unix_socket,
				user=self.CLOUDSQL_USER,
				passwd=self.CLOUDSQL_PASSWORD,
				db=self.CLOUDSQL_DB,
				charset='utf8')

    	# If the unix socket is unavailable, then try to connect using TCP. This
    	# will work if you're running a local MySQL server or using the Cloud SQL
    	# proxy, for example:
    	#
    	#   $ cloud_sql_proxy -instances=your-connection-name=tcp:3306
    	#
		else:
			self.db = MySQLdb.connect(
				host='127.0.0.1', user=self.CLOUDSQL_USER, passwd=self.CLOUDSQL_PASSWORD, 
				db=self.CLOUDSQL_DB, charset='utf8')

	def close_connection(self):
		self.db.close()

	def __enter__(self):
		return self

	def __exit__(self, type, value, traceback):
		self.close_connection()

	def get_connection(self):
		return self.db

	#The SQL queries that will be called from the database
	def get_all_locations(self):
		cur = self.db.cursor()
			
		cur.execute("SELECT place.x_coord, place.y_coord, place.likes, place.localeName, place.descript_fr, localtype.icon FROM \
					place INNER JOIN localtype ON place.localtype=localtype.localtype")

		return cur.fetchall()

	def get_all_open_locations(self):
		cur = self.db.cursor()

		cur.execute("SELECT place.x_coord, place.y_coord, place.likes, localtype.icon FROM \
					place INNER JOIN localtype ON place.localtype=localtype.localtype WHERE \
					place.currentopen = 1")

		return cur.fetchall()

	def get_all_open_in_area(self, left_long, up_lat, right_long, bottom_lat):
		cur = self.db.cursor()

		cur.execute("SELECT place.localename, place.x_coord, place.y_coord, place.likes, localtype.icon FROM \
			place INNER JOIN localtype ON place.localtype=localtype.localtype WHERE \
			place.currentopen = 1 AND place.x_coord < "+str(up_lat)+" AND place.x_coord > "+str(bottom_lat)+" \
			AND place.y_coord > "+str(left_long)+" AND place.y_coord < "+str(right_long))

		return cur.fetchall()

	def get_all_with_rating(self):
		cur = self.db.cursor()

		cur.execute("SELECT place.x_coord, place.y_coord, localtype.icon FROM \
					place INNER JOIN localtype ON place.localtype=localtype.localtype WHERE \
					place.likes > 0")

		return cur.fetchall()

	def get_all_open_type_in_area(self, place_type, left_long, up_lat, right_long, bottom_lat):
		cur = self.db.cursor()

		cur.execute("SELECT place.x_coord, place.y_coord, place.likes, localtype.icon FROM \
					place INNER JOIN localtype ON place.localtype=localtype.localtype WHERE \
					place.currentopen = 1 AND place.x_coord < "+str(up_lat)+" AND place.x_coord > "+str(bottom_lat)+" \
					AND place.y_coord > "+str(left_long)+" AND place.y_coord < "+str(right_long)+" \
					AND place.localtype = '"+place_type+"'")

		return cur.fetchall()

	def addReview(self, lat, lng, username, liked, review):
		cur = self.db.cursor()

		if liked == "Yes":
			liked = 1
		else:
			liked = 0

		#Add translate function here

		query = "INSERT into rating(x_coord, y_coord, username, liked, review) \
			VALUES ('" + str(lat) + "', '" + str(lng) + "', '"  + username + "', '" + str(liked) + "', '" + review + "');"

		cur.execute(query)
		self.db.commit()


		return cur.fetchall()

	def checkIfPlace(self, lat, lng):
		placeExists = False
		cur = self.db.cursor()

		query = "SELECT * FROM place WHERE x_coord = '" + str(lat) + "' AND y_coord = '" + str(lng) + "';"

		print(query)

		cur.execute(query)

		result = cur.fetchall()

		if not result:
			placeExists = False
		else:
			placeExists = True

		return placeExists

	def addTown(self, town, state, country):
		cur = self.db.cursor()

		query = "SELECT * FROM location WHERE town = '" + town + "' AND state = '" + state + "';"

		cur.execute(query)

		result = cur.fetchall()

		if not result:
			addQuery = "INSERT into location (town, state, country) values ('" + town + "', '" + state + "', '" + country + "');"
			cur.execute(addQuery)
			self.db.commit()

	def addPlace(self, lat, lng, placeName, address, town, state, country, email, phone, website, description, placeType):
		cur = self.db.cursor()

		#Add translate function here

		query = "INSERT INTO place (x_coord, y_coord, localeName, address, town, state, email, telephone, website, likes, dislikes, description, localtype) \
				values (" + str(lat) + ", " + str(lng) + ", '" + placeName + "', '"  + address + "', '" + town + "', '" \
				+ state + "', '" + email + "', '" + phone + "', '" + website + "', " + str(0) + ", " + str(0) + ", '" \
				+ description + "', '" + placeType + "');"
		
		cur.execute(query)
		self.db.commit()

	def addPubInfo(self, placeSpecific, lat, lng):
		cur = self.db.cursor()

		query = "INSERT INTO infoBar (x_coord, y_coord, craftBeer, beerGarden, rooftopDeck, pokies, sportsBar, atmosphere, animalPermitted) \
			 values (" + str(lat) + ", " + str(lng) + ", '" + placeSpecific["craftBeer"] + "', '" + placeSpecific["beerGarden"] \
			+ "', '" + placeSpecific["rooftopDeck"] + "', '" + placeSpecific["pokies"] + "', '" + placeSpecific["sportsBar"] \
			+ "', '" + placeSpecific['atmosphere'] + "', '" + placeSpecific['animalPermitted'] + "');"

		logging.info(query)

		cur.execute(query)
		self.db.commit()

	def addMuseumInfo(self, placeSpecific, lat, lng):
		cur = self.db.cursor()

		query = "INSERT INTO infoMuseum (x_coord, y_coord, entryFee, timeAllowed) \
			values(" + str(lat) + ", " + str(lng) + ", '" + placeSpecific['entryFee'] + "', '" \
			+ placeSpecific['timeAllowed'] + "');"

		cur.execute(query)
		self.db.commit()

	def addCafeInfo(self, placeSpecific, lat, lng):
		cur = self.db.cursor()

		query = "INSERT INTO infoCafe (x_coord, y_coord, coffee, tea, teaPot, sugar, keepCupDiscount) \
			values(" + str(lat) + ", " + str(lng) + ", '" + placeSpecific['coffee'] + "', '" + placeSpecific['tea'] \
			+ "', '" + placeSpecific['teaPot'] + "', '" + placeSpecific['sugar'] + "', '" + placeSpecific['keepCupDiscount'] \
			+ "');"

		cur.execute(query)
		self.db.commit()

	def addTakeawayInfo(self, placeSpecific, lat, lng):
		cur = self.db.cursor()

		query = "INSERT INTO infoTakeaway (x_coord, y_coord, value, containers) \
			values(" + str(lat) + ", " + str(lng) + ", '" + placeSpecific['value'] + "', '" \
			+ placeSpecific['containers'] + "');"

		cur.execute(query)
		self.db.commit()









