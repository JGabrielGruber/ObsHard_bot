from firebase_admin import db

from models.arquitetura import Arquitetura
from repositories.json import FirebaseJSON

arquiteturas: list = None


def get():
	query = db.reference('/arquiteturas').get()
	arquiteturas = []
	if type(query) is dict:
		for item in query:
			arquiteturas.append(Arquitetura.fromJSON(query[item], item))
	return arquiteturas


def getById(id):
	query = db.reference('/arquiteturas/' + id).get()
	if type(query) is dict:
		return Arquitetura.fromJSON(query, id)
	return None


def add(arquitetura: Arquitetura):
	k = db.reference('/arquiteturas').push(
	    FirebaseJSON().encode(arquitetura)).key
	return Arquitetura.fromJSON(db.reference('/arquiteturas/' + k).get(), k)


def upd(arquitetura: Arquitetura):
	id = arquitetura._id
	db.reference('/arquiteturas/' + id).set(FirebaseJSON().encode(arquitetura))
	return Arquitetura.fromJSON(db.reference('/arquiteturas/' + id).get(), id)


def rmv(arquitetura: Arquitetura):
	return db.reference('/arquiteturas/' + arquitetura._id).delete()
