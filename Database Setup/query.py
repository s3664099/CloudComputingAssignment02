#This is required for python3 to create and manipulate mySql databases
import pymysql

hostname = '127.0.0.1'
username = 'davesarkies'
password = 'password'
database = 'locationdataformaps'
datafile = 'places.txt'

print("Connecting")
#The main function. The database is opened, and the functions are executed
myConnection = pymysql.connect(host=hostname, user = username, passwd = password, db = database, charset='utf8')
cur = myConnection.cursor()
print("Connected")

#This query lists all locqtions of a specific type in a specific suburb
def sql_query():
	cur.execute("SELECT localename, address FROM place WHERE town = 'Richmond' and state = 'Vic' and localtype = 'cafe'")

	number = 0
	for localename, address in cur.fetchall():
		number +=1
		print(str(number)+") "+localename+" "+address)

#This query will list all of the locations within a set range.
def range():
	cur.execute("SELECT localename, localtype FROM place WHERE x_coord < -34.8330599 and y_coord > 138.476008 and x_coord >-35.2504513 and y_coord<138.7979831")

	number = 0
	for localename, localtype in cur.fetchall():
		number+=1
		print(str(number)+") "+localename+" "+localtype)

def cafes_in_France():
	cur.execute("SELECT localename, address FROM place INNER JOIN location ON place.state=location.state WHERE country = 'Fr' and localtype = 'cafe'")

	number = 0
	for localename, address in cur.fetchall():
		number +=1
		print(str(number)+") "+localename+" "+address)

def restaurants_in_NSW():
	cur.execute("SELECT localename, address FROM place WHERE localtype LIKE 'Rest%' and state = 'NSW'")

	number = 0
	for localename, address in cur.fetchall():
		number +=1
		print(str(number)+") "+localename+" "+address)

def show_table():
	try:
		cur.execute("SHOW TABLES")

		for table in cur.fetchall():
			print(table)
	except:
		print("Error")

	try:
		cur.execute("SELECT localename, x_coord, y_coord FROM place")

		number=0

		#print(cur.fetchall())

		for localename, x_coord, y_coord in cur.fetchall():
			number+=1
			print(str(number)+") "+localename+" "+str(x_coord)+","+str(y_coord))
	except:
		print("Tables not in existence")

		cur.execute("SELECT localename, x_coord, y_coord FROM locale WHERE localtype='Airport'")
		print(cur.fetchall())\

#show_table()
#sql_query()
#range()
#cafes_in_France()
restaurants_in_NSW()