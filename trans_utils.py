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
		"select": select,
		"beer": beer,
		"coffee": coffee,
		"lock_location": lock_location,
		"lang": lang,
		"lang_set": language
	}

	return main_page