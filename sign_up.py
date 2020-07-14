import re
from user import user

def validate(name, email, password, confirm_password):

	regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
	error = {
		'password_error': "",
		'email_error': "",
		'first_name_error': "",
		'is_error': False
	}

	#Validates the imput to make sure that important fields have been
	#Included. Also validates that the email is a valid email type
	if (name == ""):
		error['first_name_error'] = "Please enter a valid first name."
		error['is_error'] = True
		
	if (email == ""):
		error['email_error'] = "Please enter a valid email address."
		error['is_error'] = True

	#Source: https://www.geeksforgeeks.org/check-if-email-address-valid-or-not-in-python/
	if (re.search(regex, email)):
		error['is_error'] = False
	else:
		print("Hello")
		error['email_error'] = "Please enter a valid email address."
		error['is_error'] = True

	#Password validation to confirm password is sufficiently secure
	#source: https://www.geeksforgeeks.org/password-validation-in-python/
	if (password == "" or confirm_password == ""):
		error['password_error'] = "Please enter a password."
		error['is_error'] = True

	elif (len(password) < 6):
		error['password_error'] = "\nPlease enter a password length greater than 5 characters"
		error['is_error'] = True
		
	elif (password != confirm_password):
		error['password_error'] = "\nYour passwords do not match."
		error['is_error'] = True

	elif not any(char.isdigit() for char in password): 
		error['password_error'] = '\nPassword should have at least one numeral'
		error['is_error'] = True
          
	elif not any(char.isupper() for char in password): 
		error['password_error'] = '\nPassword should have at least one uppercase letter'
		error['is_error'] = True
          
	elif not any(char.islower() for char in password): 
		error['password_error'] = '\nPassword should have at least one lowercase letter'
		error['is_error'] = True

	return error	

def sign_up(password, email, name):
	user.password = password
	user.email = email
	user.name = name

	return

