import pymysql
import hashlib
import binascii
import os

#The following code for hashing, salting, and verifying a password was provided by
#https://www.vitoshacademy.com/hashing-passwords-in-python/
#This method hashes and salts the password
def hash_password(password, salt):
    """Hash a password for storing."""
   	salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), 
                                salt, 100000)
    pwdhash = binascii.hexlify(pwdhash)
    return (salt + pwdhash).decode('ascii')

#This method verifies the password
def verify_password(stored_password, provided_password):
    """Verify a stored password against one provided by user"""
    salt = stored_password[:64]
    stored_password = stored_password[64:]
    pwdhash = hashlib.pbkdf2_hmac('sha512', 
                                  provided_password.encode('utf-8'), 
                                  salt.encode('ascii'), 
                                  100000)
    pwdhash = binascii.hexlify(pwdhash).decode('ascii')
    return pwdhash == stored_password

#Method to create a new user
def new_user(user_name, first_name, last_name, email, password, db_connection):

	#Creates a cursor that connects to the database
	cur = db_connection.cursor()
	password = hash_password(password)

	#SQL to insert new user into the database
	try:
		cur.execute("INSERT INTO user VALUES ('"+user_name+"','"+first_name+"','"+last_name+"','"+password+"','"+email+"')")
	except:
		
		#Returns that the username has already been taken
		return False
	
	db_connection.commit()

	#Returns that the new user has been successfully created
	return True

def logon(user_name, user_password, db_connection):

	cur = db_connection.cursor()

	#SQL Query to search for the user and retrieves the password
	try:
		result = cur.execute("SELECT username, password FROM user WHERE username='"+user_name+"'")
	except pymysql.Error as e:
		print(e)
		return 1

	#Checks to see whether the user has been found
	if result:

		for username, password in cur.fetchall():

			#Verifies the password is correct
			new_key = verify_password(password, user_password)
			
			if (new_key == True):

				#Returns that the log in is successful
				return 2
			else:
				
				#Returns that the password is incorrect
				return 3
	else:
		
		#Returns that the user has not been found
		return 1




