from flask import Flask, render_template
import build_map as main_map

app = Flask(__name__,
	static_folder = 'static')

@app.route('/')
#The get function, while it sounds odd, the get is actually being called
#from the HTML file as opposed to this file.
def main():
    """Simple request handler that shows all of the MySQL variables."""

    #Sets an empty dictionary to handle the template values
    #These are the values that wull be used by the HTML file
    template_values = main_map.get_values()

    #This code sends the template values to the HTML file.
    #We've called the code as a json temple_values, but are now pulling them out
    #Individually
    return render_template('index.html', 
    	main_page = template_values['main_page'], 
    	location_details = template_values['location_details'],
    	selection = template_values['selection'])

@app.route('/show_locations/<location>', methods = ["POST"])
def change_locations(location):

	main_map.change_locations(option)
	main()

#Only used for running locally
if __name__ == '__main__':
	app.run(host='127.0.0.1', port=8080, debug=True)