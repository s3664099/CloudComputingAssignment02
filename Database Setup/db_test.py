import pymysql

hostname = '127.0.0.1'
username = 'root'
password = 'root'
database = 'mapmarker'

print("Connecting")
#The main function. The database is opened, and the functions are executed
myConnection = pymysql.connect(host=hostname, user = username, passwd = password, db = database, charset='utf8')
cur = myConnection.cursor()
print("Connected")

cur.execute('SET NAMES utf8')
cur.execute('SET CHARACTER SET utf8')
cur.execute('SET character_set_connection=utf8')

cur.execute("SELECT place.x_coord, place.y_coord, place.likes, localtype.icon FROM \
			place INNER JOIN localtype ON place.localtype=localtype.localtype")

print(len(cur.fetchall()))

left_long = 144.979169
right_long = 145.014274
up_lat = -37.793378
bottom_lat = -37.820096
place_type = "cafe"

cur.execute("SELECT place.localename, place.currentopen, place.x_coord, place.y_coord, place.likes, localtype.icon FROM \
			place INNER JOIN localtype ON place.localtype=localtype.localtype WHERE \
			place.x_coord < "+str(up_lat)+" AND place.x_coord > "+str(bottom_lat)+" \
			AND place.y_coord > "+str(left_long)+" AND place.y_coord < "+str(right_long)+" \
			AND place.localtype = '"+place_type+"'")

results = cur.fetchall()
print(len(results))
for i in results:
	print(i[0], i[1])

cur.execute("SELECT place.localename, place.currentopen, place.x_coord, place.y_coord, place.likes, localtype.icon FROM \
					place INNER JOIN localtype ON place.localtype=localtype.localtype WHERE \
					place.currentopen = 1 AND place.x_coord < "+str(up_lat)+" AND place.x_coord > "+str(bottom_lat)+" \
					AND place.y_coord > "+str(left_long)+" AND place.y_coord < "+str(right_long)+" \
					AND place.localtype = '"+place_type+"'")

results = cur.fetchall()
print(len(results))
for i in results:
	print(i[0], i[1])

myConnection.close()

