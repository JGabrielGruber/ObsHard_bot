from firebase_admin import db


def teste():
	print(db.reference('/').get())