from firebase_admin import db

from models.marca import Marca
from repositories.json import FirebaseJSON

marcas: list = None


def get():
	query = db.reference('/marcas').get(etag=True)
	marcas = []
	for item in query[0]:
		marcas.append(Marca(item, query[0][item]['nome']))
	return marcas


def add(marca: Marca):
	return db.reference('/marcas').push(
	    FirebaseJSON().encode(marca)).get(etag=True)
