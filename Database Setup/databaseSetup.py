#Python DataBase Setup
#=====================
#
#This script is designed to take the contents of a specific txt
#file, created from a spreadsheet, and create a database around it.
#The initial database is cleared, and the contents of the file are then
#placed into the database.
#
#Try/Except statements are used for error handling, and are essential
#when working with databases (as is the case with files)

#This is required for python3 to create and manipulate mySql databases
import pymysql

hostname = '127.0.0.1'
username = 'davesarkies'
password = 'password'
database = 'locationdataformaps'
datafile = 'places.txt'
print("Hello")

#This function clears the database
def clearDatabases(conn):
	cur = conn.cursor()

	#Foreign Key checks are turned off to allow the tables
	#to be cleared, and dropped.
	cur.execute("SET FOREIGN_KEY_CHECKS = 0")
	
	try:
		cur.execute("DROP TABLE location")
	except:
		print("No such table as location")

	try:
		cur.execute("DROP TABLE localtype")
	except:
		print("No such table as localtype")
	try:
		cur.execute("DROP TABLE place")
	except:
		print("No such table as place")
	try:
		cur.execute("DROP TABLE admim")
	except:
		print("No such table as admin")	
	try:
		cur.execute("DROP TABLE businessowner")
	except:
		print("No such table as businessowner")
	try:
		cur.execute("DROP TABLE websiteuser")
	except:
		print("No such table as websiteuser")
	try:
		cur.execute("DROP TABLE rating")
	except:
		print("No such table as rating")


#This function creates the tables associated with the database
def createTables(conn):
	cur = conn.cursor()

	try:
		cur.execute("CREATE TABLE location (town VARCHAR(20), state VARCHAR(20), country VARCHAR(20), PRIMARY KEY (town, state))")
	except:
		print("Table location already exists")

	try:
		cur.execute("CREATE TABLE localtype(localtype VARCHAR(30), icon VARCHAR(50), PRIMARY KEY (localtype))")	
	except:
		print("Table localtype already exists")

	try:	
		cur.execute("CREATE TABLE place (x_coord DECIMAL (9,6), y_coord DECIMAL (9,6), localeName VARCHAR(255), address VARCHAR(255), town VARCHAR(20), state VARCHAR(30), email VARCHAR(100), telephone VARCHAR(30), website VARCHAR(100), likes INTEGER(5), dislikes INTEGER(5), currentopen BOOLEAN, description TEXT(5000), localtype VARCHAR(30), picture VARCHAR(20), PRIMARY KEY (x_coord, y_coord), FOREIGN KEY (localtype) REFERENCES localtype(localtype), FOREIGN KEY (town, state) REFERENCES location(town, state))")
	except pymysql.Error as e:
		print("Error ",e)


#This function loads the data from the .txt file and inserts it into the database.
def loadDataFile(conn):

	cur = conn.cursor()
	file = open(datafile,'r')
	number = 0

	#counter used for error handling
	number = 0

	#Each of the lines in the file are executed individually, and the contents inserted
	#into the database
	for line in file:

		#Certain elements are fixed up so as not to cause problems when inserting the contents
		#Each of the lines are also split up into individual fields
		line = line.replace("'","''")
		fields = line.split("\t")

		#We skip the first line - ie the title
		if fields[0] != "name" and fields[1] !="address":

			number+=1

			try:
				cur.execute("INSERT INTO localtype VALUES ('"+fields[10]+"','"+fields[11]+"')");
			except pymysql.Error as e:

				#a place holder un case we need to comment out
				#the errors so as to identify any specific problems
				i=1
				#print(str(number)+") Error: "+str(e))

			try:
				cur.execute("INSERT INTO location VALUES ('"+fields[2]+"','"+fields[3]+"','"+fields[4]+"')");
				
			except pymysql.Error as e:
				i=1
				#print(str(number)+") Error: "+str(e))

			x_coord = fields[7]
			y_coord = fields[8]	

			#We need to covert some of the fields into boolean operators
			#ie: 0 or 1
			try:
				print(number)
				isOpen = True
				likes = 0
				dislikes = 0

				if (fields[9] == 1):
					dislikes = 50
				elif (fields[9] == 2):
					likes = 20
					dislikes = 80
				elif (fields[9] == 3):
					likes = 50
					dislikes = 50
				elif (fields[9] == 4):
					likes = 80
					dislikes = 50
				else:
					likes = 50


				if (fields[12] == "Y"):
					fields[12] = "1"
				elif (fields[12] == "N"):
					fields[12] = "0"
				else:
					isOpen = False

				if (isOpen == True):
					cur.execute("INSERT INTO place(localename,x_coord,y_coord, address, town, state, telephone, website,currentopen, localtype, likes, dislikes ) VALUES ('"+fields[0]+"','"+str(x_coord)+"','"+str(y_coord)+"','"+fields[1]+"','"+fields[2]+"','"+fields[3]+"','"+fields[5]+"','"+fields[6]+"','"+fields[12]+"','"+fields[10]+"','"+str(likes)+"','"+str(dislikes)+"')")
				else:
					cur.execute("INSERT INTO place(localename,x_coord,y_coord, address, town, state, telephone, website,localtype, likes, dislikes ) VALUES ('"+fields[0]+"','"+str(x_coord)+"','"+str(y_coord)+"','"+fields[1]+"','"+fields[2]+"','"+fields[3]+"','"+fields[5]+"','"+fields[6]+"','"+fields[10]+"','"+str(likes)+"','"+str(dislikes)+"')")
			except pymysql.Error as e:
				print(str(number)+") Error: "+str(e))
				i=1

		#This is required, otherwise the contents of the database will
		#not be saved (interesting how none of the tutorials mentioned this)
		conn.commit()

		
#This function exists to test that the contents of the database were updated sufficiently
#Also for error handling
def testQuery(conn):
	cur = conn.cursor()

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

	cur.execute("SELECT localename, x_coord, y_coord FROM place WHERE localtype='Airport'")
	print(cur.fetchall())

print("Connecting")
#The main function. The database is opened, and the functions are executed
myConnection = pymysql.connect(host=hostname, user = username, passwd = password, db = database, charset='utf8')
cur = myConnection.cursor()
print("Connected")

cur.execute('SET NAMES utf8')
cur.execute('SET CHARACTER SET utf8')
cur.execute('SET character_set_connection=utf8')

clearDatabases(myConnection)
createTables(myConnection)
loadDataFile(myConnection)
testQuery(myConnection)
myConnection.close()


