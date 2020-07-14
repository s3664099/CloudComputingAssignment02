from flask import render_template
import database_utils as database
from user import user

def get_reviews(longitude, latitude):
	
	db = database.database_utils()
	reviews = db.getReviews(latitude, longitude)

	return render_template('review.html',
		reviews = reviews,
		latitude = latitude,
		longitude = longitude,
		user = user.name)

def post_review(longitude, latitude, review, liked):

	db = database.database_utils()
	reviews = db.getReviews(latitude, longitude)

	if db.checkIfPlace(latitude, longitude):

		true_liked = 0
		user_key = user.name

		if (liked == 'Yes'):
			true_liked = 1

		try:
			db.addReview(latitude, longitude, user_key, user_key, user_key, true_liked, review)
			reviews = db.getReviews(latitude,longitude)
			return render_template('review.html',
				message = "Review successfully submitted!",
				reviews = reviews,
				latitude = latitude,
				longitude = longitude,
				user = user.name)
		except:
			reviews = db.getReviews(latitude,longitude)
			return render_template('review.html',
				message = "You've already submitted a review for this location!",
				reviews = reviews,
				latitude = latitude,
				longitude = longitude,
				user = user.name)	
	else:
		return render_template('review.html',
			message = "No place was detected at your location. Please add your place before reviewing.",
			reviews = reviews,
			latitude = latitude,
			longitude = longitude,
			user = user.name)					


