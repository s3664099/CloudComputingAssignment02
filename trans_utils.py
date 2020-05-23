from googletrans import Translator

translate_client = Translator()

def translate_text(description):

	language = translate_client.detect(description)

	descript_en = translate_client.translate(description,dest = 'en')
	descript_fr = translate_client.translate(description,dest = 'fr')
	descript_it = translate_client.translate(description,dest = 'it')
	descript_de = translate_client.translate(description,dest = 'de')

	if language.lang == 'fr':
		descript_fr.text = description
	elif language.lang == 'de':
		descript_de.text = description
	elif language.lang == 'it':
		descript_it.text = description
	elif language.lang == 'en':
		descript_en.text = description

	translations = {
		"original": description,
		"french": descript_fr.text,
		"german": descript_de.text,
		"italian": descript_it.text,
		"english": descript_en.text
	}

	return translations

def get_db_language(language):

	selected_language = "description"

	if language == 'fr':
		selected_language = "descript_fr"
	elif language == 'de':
		selected_language = "descript_de"
	elif language == 'it':
		selected_language = "descript_it"

	return selected_language


def main_page(language):

	if language == 'de':
		login = "Anmeldung"
		signup = "Anmelden"
		signout = "Ausloggen"
		addplace = u"Platz hinzuf\xfcgen"
		reviewlocation = u"Ort \xfcberpr\xfcfen"
		nosignin = "Nicht eingeloggt"
		yessignin = "Eingeloggt als"
		lang = "Sprache"
		logins = "Anmeldungen heute"
		visited = "Besuchte Orte"
		everything = "Alles"
		select = u"w\xe4hlen"
		beer = "Bier"
		coffee = "Kaffee"
		lock_location = "speicherort sperren"

	elif language == 'fr':
		login = "S'identifier"
		signup = "S'inscrire"
		signout = u"D\xe9connexion"
		addplace = "Ajouter un lieu"
 		reviewlocation = u"V\xe9rifier l'emplacement"
		nosignin = u"Pas connect\xe9"
		yessignin = u"Connect\xe9 en tant que"
		lang = "Langue"
		logins = u"Se connecter aujourd\xe9hui"
		visited = "Lieux visit\xe9s"
		everything = "Tout"
		select = u"s\xe9lectionner"
		beer = u"bi\xe8re"
		coffee = u"caf\xe9"
		lock_location = "Emplacement du verrou"

	elif language == 'it':
		login = "Accesso"
		signup = "Iscriviti"
		signout = "Disconnessione"
		addplace = "Aggiungi luogo"
		reviewlocation = "Rivedi posizione"
		nosignin = "Non registrato"
		yessignin = "Accesso come"
		lang = "linguaggio"
		logins = "Accedi oggi"
		everything = "Qualunque cosa"
		visited = "Luoghi visitati"
		select = "Selezionare"
		beer = "birra"
		coffee = u"caff\xe8"
		lock_location = "Blocca posizione"

	else:
		login = "Login"
		signup = "Sign Up"
		signout = "Sign Out"
		addplace = "Add Place"
		reviewlocation = "Review Location"
		nosignin = "Not signed in"
		yessignin = "Signed in as"
		lang = "Language"
		logins = "logins today"
		everything = "everything"
		visited = "Places Visited"
		select = "select"
		beer = "birra"
		coffee = "coffee"
		lock_location = "lock location"


	main_page = {
		"login": login,
		"signup": signup,
		"signout": signout,
		"addplace": addplace,
		"reviewlocation": reviewlocation,
		"nosignin": nosignin,
		"yessignin": yessignin,
		"logins": logins,
		"everything": everything,
		"places_visited": visited,
		"select": select,
		"beer": beer,
		"coffee": coffee,
		"lock_location": lock_location,
		"lang": lang,
		"lang_set": language
	}

	return main_page

def view_page(language):
	if language == 'de':
		login = "Anmeldung"
		signup = "Anmelden"
		signout = "Ausloggen"
		reviewlocation = u"Ort \xfcberpr\xfcfen"
		nosignin = "Nicht eingeloggt"
		yessignin = "Eingeloggt als"
		back = u"Zur\xfcck zu den Karten"
		address= "Adresse"
		phone = "Telefonnummer"
		website = "Webseite"
		craft_beer = u"bi\xe9re artisanale"
		beer_garden = "Biergarten"
		rooftop_deck = "Dachterrasse"
		pokies_lots = "Viele Pokies"
		pokies_few = "Ein paar Pokies"
		pokies_none = "Keine Pokies"
		sport_bar = "Sport-Bar"
		tacky_atmosphere = u"Atmosph\xe4re: klebrig"
		grungy_atmosphere = u"Atmosph\xe4re: schmuddelig"
		hip_atmosphere = "Atmosph\xe4re: hip"
		animals = "Tiere erlaubt"
		great_coffee = "toller Kaffee"
		good_coffee = "guter Kaffee"
		bad_coffee = "schlecter Kaffee"
		strong_tea = "starker Tee"
		good_tea = "guter Tee"
		bad_tea = "schlecter Tee"
		big_teapot = u"gro\x9ee Teekanne"
		small_teapot = "kleine Teekanne"
		tea_cup = "nur Teetasse"
		no_tea = "keine Tee"
		good_sugar = "guter Zuker"
		bad_sugar = "schlecter Zuker"
		keep_cup = "Keep-Cup-Rabatt"
		description = "Beschreibung"
		reviews = "Benutzerbewertungen"
		atmosphere_trendy = u"Atmosph\xe4re: trendy"

	elif language == 'fr':
		login = "S'identifier"
		signup = "S'inscrire"
		signout = u"D\xe9connexion"
 		reviewlocation = u"V\xe9rifier l'emplacement"
		nosignin = u"Pas connect\xe9"
		yessignin = u"Connect\xe9 en tant que"
		back = "Retour aux cartes"
		address = "Adresse"
		phone = u"Num\xe9ro de t\xe9l\xe9phone"
		website = "site Internet"
		craft_beer = u"bi\xe9re artisanale"
		beer_garden = u"jardin de bi\xe8re"
		rooftop_deck = "terrasse sur le toit"
		pokies_lots = "Beaucoup de Pokies"
		pokies_few = "Quelques pokies"
		pokies_none = "pas de pokies"
		sport_bar = "bar sportif"
		tacky_atmosphere = "ambiance: collant"
		grungy_atmosphere = "ambiance: grungy"
		hip_atmosphere = "ambiance: hip"
		animals = u"animaux accept\xe9s"
		great_coffee = u"bon caf\xe9"
		good_coffee = u"bon caf\xe9"
		bad_coffee = u"mauvais caf\xe9"
		strong_tea = u"th\xe9 fort"
		good_tea = u"bon th\xe9"
		bad_tea = u"mauvais th\xe9"
		big_teapot = u"grande th\xe9i\xe8re"
		small_teapot = u"petite th\xe9i\xe8re"
		tea_cup = u"tasse de th\xe9 seulement"
		no_tea = u"ne fait pas de th\xe9"
		good_sugar = "bon sucre"
		bad_sugar = "mauvais sucre"
		keep_cup = "remise de coupe"
		description = "La description"
		reviews = "Critiques d'utilisateurs"
		atmosphere_trendy = "Ambiance: tendance"

	elif language == 'it':
		login = "Accesso"
		signup = "Iscriviti"
		signout = "Disconnessione"
		reviewlocation = "Rivedi posizione"
		nosignin = "Non registrato"
		yessignin = "Accesso come"
		back = "Torna a Maps"
		address = "Indirizzo"
		phone = "Numero di telefono"
		website = "sito web"
		craft_beer = "birra artigianale"
		beer_garden = "birreria all'aperto"
		rooftop_deck = "terrazza sul tetto"
		pokies_lots = "Molti Pokies"
		pokies_few = "Alcuni pokies"
		pokies_none = "niente scherzi"
		sport_bar = "bar dello sport"
		tacky_atmosphere = "atmosfera: pacchiana"
		grungy_atmosphere = "atmosfera: sgangherata"
		hip_atmosphere = "atmosfera: alla moda"
		animals = "animali ammessi"
		great_coffee = u"ottimo caff\xe8"
		good_coffee = u"buon caff\xe8"
		bad_coffee = u"cattivo caff\xe8"
		strong_tea = u"t\xe8 forte"
		good_tea = u"buon t\xe8"
		bad_tea = u"brutto t\xe8"
		big_teapot = "grande teiera"
		small_teapot = "piccola teiera"
		tea_cup = u"solo tazza di t\xe8"
		no_tea = u"non fa il t\xe8"
		good_sugar = "buon zucchero"
		bad_sugar = "zucchero cattivo"
		keep_cup = "sconto keep-cup"
		description = "Descrizione"
		reviews = "Recensioni degli utenti"

	else:
		login = "Login"
		signup = "Sign Up"
		signout = "Sign Out"
		reviewlocation = "Review Location"
		nosignin = "Not signed in"
		yessignin = "Signed in as"
		back = "Back to maps"
		address = "address"
		phone = "Phone"
		website = "website"
		craft_beer = "craft beer"
		beer_garden = "beer garden"
		rooftop_deck = "roof top deck"
		pokies_lots = "lots of pokies"
		pokies_few = "A few pokies"
		pokies_none = "No pokies"
		sport_bar = "Sports Bar"
		tacky_atmosphere = "Atmosphere: Tacky"
		grungy_atmosphere = "Atmosphere: Grungy"
		hip_atmosphere = "Atmosphere: Hip"
		animals = "Animals Allowed"
		great_coffee = "Great Coffee"
		good_coffee = "Good coffee"
		bad_coffee = "bad coffee"
		strong_tea = "Strong tea"
		good_tea = "Good tea"
		bad_tea = "Bad tea"
		big_teapot = "Bit teapot"
		small_teapot = "small teapot"
		tea_cup = "Tea cup only"
		no_tea = "Doesn't do tea"
		good_sugar = "good sugar"
		bad_sugar = "bad sugar"
		keep_cup = "Keep cup discount"
		description = "Description"
		reviews = "User Reviews"
		atmosphere_trendy = "Atmosphere: trendy"

	main_page = {
		"login": login,
		"signup": signup,
		"signout": signout,
		"reviewlocation": reviewlocation,
		"nosignin": nosignin,
		"yessignin": yessignin,
		"back": back,
		"address": address,
		"website": website,
		"craft_beer": craft_beer,
		"beer_garden": beer_garden,
		"rooftop_deck": rooftop_deck,
		"pokies_lots": pokies_lots,
		"pokies_few": pokies_few,
		"pokies_none": pokies_none,
		"sport_bar": sport_bar,
		"tacky_atmosphere": tacky_atmosphere,
		"grungy_atmosphere": grungy_atmosphere,
		"hip_atmosphere": hip_atmosphere,
		"trendy_atmosphere": atmosphere_trendy,
		"animals": animals,
		"great_coffee": great_coffee,
		"good_coffee": good_coffee,
		"bad_coffee": bad_coffee,
		"strong_tea": strong_tea,
		"good_tea": good_tea,
		"bad_tea": bad_tea,
		"big_teapot": big_teapot,
		"small_teapot": small_teapot,
		"tea_cup": tea_cup,
		"no_tea": no_tea,
		"good_sugar": good_sugar,
		"bad_sugar": bad_sugar,
		"keep_cup": keep_cup,
		"description": description,
		"reviews": reviews
	}

	return main_page