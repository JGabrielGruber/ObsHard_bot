from firebase_admin import db

from models.marca import Marca
from repositories.json import FirebaseJSON

marcas: dict = {}
etag: str = None


def change(event):
	global marcas
	global etag
	if etag == None:
		ret = db.reference('/marcas').get(etag=True)
		etag = ret[1]
		for key, item in ret[0].items():
			marca = Marca.fromJSON(item, key)
			marcas.update({ key: marca })
	else:
		ret = db.reference('/marcas').get_if_changed(etag)
		if ret[0]:
			etag = ret[2]
			marcas.clear()
			for key, item in ret[1].items():
				marca = Marca.fromJSON(item, key)
				marcas.update({ key: marca })


def sync():
	return db.reference('/marcas').listen(change)
