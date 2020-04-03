from firebase_admin import db

from models.marca import Marca
from repositories.json import FirebaseJSON

marcas: list = None


def get():
	query = db.reference('/marcas').get()
	marcas = []
	if type(query) is dict:
		for item in query:
			marcas.append(Marca.fromJSON(query[item], item))
	return marcas


def add(marca: Marca):
	k = db.reference('/marcas').push(FirebaseJSON().encode(marca)).key
	return (db.reference('/marcas/' + k).get(), k)


def upd(marca: Marca):
	db.reference('/marcas/' + marca._id).set(FirebaseJSON().encode(marca))
	return (db.reference('/marcas/' + marca._id).get(), marca._id)


def rmv(marca: Marca):
	return db.reference('/marcas/' + marca._id).delete()
