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

myConnection.close()

