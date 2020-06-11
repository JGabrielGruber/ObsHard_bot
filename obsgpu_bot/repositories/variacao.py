from firebase_admin import db

from models.variacao import Variacao
from repositories import modelo
from repositories.json import FirebaseJSON

produtos: list = None


def get():
	query = db.reference('/produtos').get()
	produtos = []
	if type(query) is dict:
		for item in query:
			variacao = Variacao.fromJSON(query[item], item)
			if 'modelo' in query[item]:
				variacao.modelo = modelo.getById(query[item]['modelo'])
			produtos.append(variacao)
	return produtos


def getById(id):
	query = db.reference('/produtos/' + id).get()
	if type(query) is dict:
		variacao = Variacao.fromJSON(query, id)
		if 'modelo' in query:
			variacao.modelo = modelo.getById(query['modelo'])
		return variacao
	return None


def add(variacao: Variacao):
	k = db.reference('/produtos').push(FirebaseJSON().encode(variacao)).key
	return Variacao.fromJSON(db.reference('/produtos/' + k).get(), k)


def upd(variacao: Variacao):
	id = variacao._id
	db.reference('/produtos/' + id).set(FirebaseJSON().encode(variacao))
	return Variacao.fromJSON(db.reference('/produtos/' + id).get(), id)


def rmv(variacao: Variacao):
	return db.reference('/produtos/' + variacao._id).delete()
