from firebase_admin import db

from models.produto import Produto
from repositories import variacao, loja
from repositories.json import FirebaseJSON

produtos: list = None


def get():
	query = db.reference('/produtos').get()
	produtos = []
	if type(query) is dict:
		for item in query:
			produto = Produto.fromJSON(query[item], item)
			if 'loja' in query[item]:
				produto.loja = loja.getById(query[item]['loja'])
			if 'variacao' in query[item]:
				produto.variacao = variacao.getById(
				    query[item]['variacao'])
			produtos.append(produto)
	return produtos


def getById(id):
	query = db.reference('/produtos/' + id).get()
	if type(query) is dict:
		produto = Produto.fromJSON(query, id)
		if 'loja' in query:
			produto.loja = loja.getById(query['loja'])
		if 'variacao' in query:
			produto.variacao = variacao.getById(query['variacao'])
		return produto
	return None


def add(produto: Produto):
	k = db.reference('/produtos').push(FirebaseJSON().encode(produto)).key
	return Produto.fromJSON(db.reference('/produtos/' + k).get(), k)


def upd(produto: Produto):
	id = produto._id
	db.reference('/produtos/' + id).set(FirebaseJSON().encode(produto))
	return Produto.fromJSON(db.reference('/produtos/' + id).get(), id)


def rmv(produto: Produto):
	return db.reference('/produtos/' + produto._id).delete()
