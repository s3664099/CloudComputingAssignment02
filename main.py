from flask import Flask, render_template, request
import build_map as main_map
import login as login
from user import user

app = Flask(__name__,
	static_folder = 'static')

#Function to return the main map template
def render_template_return():

    print(user.logged_in)

    #Sets an empty dictionary to handle the template values
    #These are the values that wull be used by the HTML file
    template_values = main_map.get_values()

    #This code sends the template values to the HTML file.
    #We've called the code as a json temple_values, but are now pulling them out
    #Individually

    if template_values['user'] == None:
    	return render_template('index.html', 
    		main_page = template_values['main_page'],
	    	location_details = template_values['location_details'],
	    	selection = template_values['selection'])

    return render_template('index.html', 
    	main_page = template_values['main_page'],
    	user = template_values['user'], 
    	location_details = template_values['location_details'],
    	selection = template_values['selection'])


@app.route('/')
#The get function, while it sounds odd, the get is actually being called
#from the HTML file as opposed to this file.
def main():

	return render_template_return()

@app.route('/show_locations', methods = ["POST"])
def change_locations():

	if request.method == 'POST':
		option = request.form['location']
		main_map.change_locations(option)

	return render_template_return()

#Login Functions
@app.route('/login', methods = ["POST","GET"])
def login_page():

	#Diverts user to Login Page
	if request.method == 'GET':
		return render_template('login.html')

	#Performs login functions
	elif request.method == 'POST':
		entered_email = request.form['email']
		entered_password = request.form['password']
		authenticate = login.login(entered_email,entered_password)

		if authenticate == "correct":
			return render_template_return()
		else:
			return render_template('login.html',
				message = authenticate)

#Sign out function
@app.route('/signout')
def sign_out():
	user.logged_in = False
	return render_template_return()

#Only used for running locally
if __name__ == '__main__':
	app.run(host='127.0.0.1', port=8080, debug=True)