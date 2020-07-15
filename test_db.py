import database_utils as database

db = database.database_utils()

db.addPlace(-34.990903, 137.401228, "Warooka Park", "Main St, Sturt Bay Rd, Warooka SA 5577", "Yorketown", "SA", "Aus", "", "", "", 
	"A rather pleasant park in the middle of town.", "Park")

for localename, descript_en, descript_fr, descript_it, descript_de in db.get_place(-34.990903, 137.401228):
	print(localename)
	print(descript_en)
	print(descript_fr)
	print(descript_it)
	print(descript_de)