import hashlib
from google.cloud import ndb
import binascii

#Class to store user details.
class user():

	language = 'en'
	selection = "everything"
	password = "Hello"
	name = "Johnny"
	email = "Johnny@email.com"
	logged_in = False

	#Dummy functions for testing only
	def check_user(self, entered_email):

		if (entered_email == self.email):
			return True

		return False

	def check_password(self, entered_password):

		if (entered_password == self.password):
			return True

		return False

	#Function hashes the email to compare with emails stored on the system
	def hash_email(self, entered_email):

		# Hash the email and attempt to get a key.
		hasher = hashlib.sha256()
		entered_email = entered_email.encode('utf-8')
		hasher.update(entered_email)
		return hasher.hexdigest()

	#Returns the key from the NoSQL DB for use in authenticating the password
	def get_key(self, hashed_email):

		# Constructing key to get user details.
		user_key = ndb.Key("User", hashed_email)
		return user_key.get()

	def authenticate_user(self, user_key, entered_password):

		# Check password.
		stored_pass = user_key.password
		stored_salt = user_key.salt

		pwdhash = hashlib.pbkdf2_hmac('sha256', entered_password.encode('utf-8'), stored_salt.encode('ascii'), 100000)
		pwdhash = binascii.hexlify(pwdhash).decode('ascii')

		if (pwdhash == stored_pass):
			#text = hashed_email + " logged into the application."
			#logging.info(text)

			#self.session['user'] = hashed_email

			return 'correct'
		else:
			return "incorrect"

	def get_selection(self):
		return self.selection

	def set_selection(self, selection):
		self.selection = selection

	def get_language(self):
		return self.language

	def set_language(self, language):
		self.language = language

