from firebase_admin import db

from models.loja import Loja
from repositories.json import FirebaseJSON

lojas: dict = {}
etag: str = None


def change(event):
	global lojas
	global etag
	if etag == None:
		ret = db.reference('/lojas').get(etag=True)
		etag = ret[1]
		for key, item in ret[0].items():
			loja = Arquitetura.fromJSON(item, key)
			lojas.update({ key: loja })
	else:
		ret = db.reference('/lojas').get_if_changed(etag)
		if ret[0]:
			etag = ret[2]
			lojas.clear()
			for key, item in ret[1].items():
				loja = Arquitetura.fromJSON(item, key)
				lojas.update({ key: loja })


def sync():
	return db.reference('/lojas').listen(change)
