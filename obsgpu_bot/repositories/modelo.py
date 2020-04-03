from firebase_admin import db

from models.modelo import Modelo
from repositories import arquitetura, marca
from repositories.json import FirebaseJSON

modelos: list = None


def get():
	query = db.reference('/modelos').get()
	modelos = []
	if type(query) is dict:
		for item in query:
			modelo = Modelo.fromJSON(query[item], item)
			if 'marca' in query[item]:
				modelo.marca = marca.getById(query[item]['marca'])
			if 'arquitetura' in query[item]:
				modelo.arquitetura = arquitetura.getById(
				    query[item]['arquitetura'])
			modelos.append(modelo)
	return modelos


def getById(id):
	query = db.reference('/modelos/' + id).get()
	if type(query) is dict:
		modelo = Modelo.fromJSON(query, id)
		if 'marca' in query:
			modelo.marca = marca.getById(query['marca'])
		if 'arquitetura' in query:
			modelo.arquitetura = arquitetura.getById(query['arquitetura'])
		return modelo
	return None


def add(modelo: Modelo):
	k = db.reference('/modelos').push(FirebaseJSON().encode(modelo)).key
	return Modelo.fromJSON(db.reference('/modelos/' + k).get(), k)


def upd(modelo: Modelo):
	id = modelo._id
	db.reference('/modelos/' + id).set(FirebaseJSON().encode(modelo))
	return Modelo.fromJSON(db.reference('/modelos/' + id).get(), id)


def rmv(modelo: Modelo):
	return db.reference('/modelos/' + modelo._id).delete()
