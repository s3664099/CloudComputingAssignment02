from googletrans import Translator

translate_client = Translator()

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
	elif language == 'fr':
		login = "S'identifier"
		signup = "S'inscrire"
		signout = u"D\xe9connexion"
		addplace = "Ajouter un lieu"
 		reviewlocation = u"V\xe9rifier l'emplacement"
		nosignin = u"Pas connect\xe9"
		yessignin = u"Connect\xe9 en tant que"
		lang = "Langue"
	elif language == 'it':
		login = "Accesso"
		signup = "Iscriviti"
		signout = "Disconnessione"
		addplace = "Aggiungi luogo"
		reviewlocation = "Rivedi posizione"
		nosignin = "Non registrato"
		yessignin = "Accesso come"
		lang = "linguaggio"
	else:
		login = "Login"
		signup = "Sign Up"
		signout = "Sign Out"
		addplace = "Add Place"
		reviewlocation = "Review Location"
		nosignin = "Not signed in"
		yessignin = "Signed in as"
		lang = "Language"


	main_page = {
		"login": login,
		"signup": signup,
		"signout": signout,
		"addplace": addplace,
		"reviewlocation": reviewlocation,
		"nosignin": nosignin,
		"yessignin": yessignin,
		"lang": lang,
		"lang_set": language
	}

	return main_page