from firebase_admin import db

from models.loja import Loja
from repositories.json import FirebaseJSON

lojas: list = None


def get():
	query = db.reference('/lojas').get()
	lojas = []
	if type(query) is dict:
		for item in query:
			lojas.append(Loja.fromJSON(query[item], item))
	return lojas


def add(loja: Loja):
	k = db.reference('/lojas').push(FirebaseJSON().encode(loja)).key
	return Loja.fromJSON(db.reference('/lojas/' + k).get(), k)


def upd(loja: Loja):
	id = loja._id
	db.reference('/lojas/' + id).set(FirebaseJSON().encode(loja))
	return Loja.fromJSON(db.reference('/lojas/' + id).get(), id)


def rmv(loja: Loja):
	return db.reference('/lojas/' + loja._id).delete()
