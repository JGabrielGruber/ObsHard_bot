from firebase_admin import db

from models.marca import Marca
from repositories.json import FirebaseJSON

marcas: list = None


def get():
	query = db.reference('/marcas').get(etag=True)
	marcas = []
	if query[0] is list:
		for item in query[0]:
			marcas.append(Marca(query[0][item]['nome'], item))
	return marcas


def add(marca: Marca):
	k = db.reference('/marcas').push(FirebaseJSON().encode(marca)).key
	return (db.reference('/marcas/' + k).get(), k)


def upd(marca: Marca):
	db.reference('/marcas/' + marca._id).set(FirebaseJSON().encode(marca))
	return (db.reference('/marcas/' + marca._id).get(), marca._id)


def rmv(marca: Marca):
	return db.reference('/marcas/' + marca._id).delete()
