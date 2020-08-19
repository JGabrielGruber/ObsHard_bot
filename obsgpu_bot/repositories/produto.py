from firebase_admin import db

from models.produto import Produto
from repositories.json import FirebaseJSON

produtos: dict = {}
etag: str = None


def change(event):
	global produtos
	global etag
	if etag == None:
		ret = db.reference('/produtos').get(etag=True)
		etag = ret[1]
		for key, item in ret[0].items():
			produto = Produto.fromJSON(item, key)
			produtos.update({ key: produto })
	else:
		ret = db.reference('/produtos').get_if_changed(etag)
		if ret[0]:
			etag = ret[2]
			produtos.clear()
			for key, item in ret[1].items():
				produto = Produto.fromJSON(item, key)
				produtos.update({ key: produto })


def sync():
	return change()


def update(data, id):
	db.reference('/produtos').child(id).set(FirebaseJSON().encode(data))
