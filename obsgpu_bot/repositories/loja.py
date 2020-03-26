from firebase_admin import db

from models.loja import Loja
from repositories.json import FirebaseJSON

lojas: list = None


def get():
	query = db.reference('/lojas').get(etag=True)
	lojas = []
	if query[0] is list:
		for item in query[0]:
			lojas.append(Loja(query[0][item], item))
	return lojas


def add(loja: Loja):
	k = db.reference('/lojas').push(FirebaseJSON().encode(loja)).key
	return (db.reference('/lojas/' + k).get(), k)


def upd(loja: Loja):
	db.reference('/lojas/' + loja._id).set(FirebaseJSON().encode(loja))
	return (db.reference('/lojas/' + loja._id).get(), loja._id)


def rmv(loja: Loja):
	return db.reference('/lojas/' + loja._id).delete()
