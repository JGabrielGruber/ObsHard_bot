from firebase_admin import db

from models.arquitetura import Arquitetura
from repositories.json import FirebaseJSON

arquiteturas: list = None


def get():
	query = db.reference('/arquiteturas').get(etag=True)
	arquiteturas = []
	if query[0] is list:
		for item in query[0]:
			arquiteturas.append(Arquitetura(query[0][item]['nome'], item))
	return arquiteturas


def add(arquitetura: Arquitetura):
	k = db.reference('/arquiteturas').push(FirebaseJSON().encode(arquitetura)).key
	return (db.reference('/arquiteturas/' + k).get(), k)


def upd(arquitetura: Arquitetura):
	db.reference('/arquiteturas/' + arquitetura._id).set(FirebaseJSON().encode(arquitetura))
	return (db.reference('/arquiteturas/' + arquitetura._id).get(), arquitetura._id)


def rmv(arquitetura: Arquitetura):
	return db.reference('/arquiteturas/' + arquitetura._id).delete()
