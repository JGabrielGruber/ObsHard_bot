from firebase_admin import db

from repositories import modelo
from repositories.json import FirebaseJSON

variacoes: dict = {}
etag: str = None


def change(event):
	global variacoes
	global etag
	if etag == None:
		ret = db.reference('/variacoes').get(etag=True)
		etag = ret[1]
		for key, item in ret[0].items():
			variacao = Variacao.fromJSON(item, key)
			variacoes.update({ key: variacao })
	else:
		ret = db.reference('/variacoes').get_if_changed(etag)
		if ret[0]:
			etag = ret[2]
			variacoes.clear()
			for key, item in ret[1].items():
				variacao = Variacao.fromJSON(item, key)
				variacoes.update({ key: variacao })


def sync():
	return change()
