from user import user

#Login function for testing only. Commented out code to be developed
#Once main program working. Need to be able to have each user have their own settings
def login(entered_email, entered_password):

		"""
		hashed_email = user.hash_email(entered_email)
		user_key = user.get_key(hashed_email)

		if (user_key is None):
			return "No Account"
		else:

			return user.authenticate_user(user_key, entered_password)
		"""

		new_user = user()

		if new_user.check_user(entered_email) == False:
			return "No Account with that email can be found"
		else:

			if new_user.check_password(entered_password) == False:
				return "Password is incorrect"

		user.logged_in = True
		return "correct"

