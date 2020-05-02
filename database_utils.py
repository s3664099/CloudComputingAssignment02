import MySQLdb
import os

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

	def get_all_locations(self):
		cur = self.db.cursor()
			
		cur.execute("SELECT place.x_coord, place.y_coord, place.likes, localtype.icon FROM \
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







