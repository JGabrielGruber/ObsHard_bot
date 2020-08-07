from firebase_admin import db

from models.modelo import Modelo
from repositories.json import FirebaseJSON

modelos: dict = {}
etag: str = None


def change(event):
	global modelos
	global etag
	if etag == None:
		ret = db.reference('/modelos').get(etag=True)
		etag = ret[1]
		for key, item in ret[0].items():
			modelo = Modelo.fromJSON(item, key)
			modelos.update({ key: modelo })
	else:
		ret = db.reference('/modelos').get_if_changed(etag)
		if ret[0]:
			etag = ret[2]
			modelos.clear()
			for key, item in ret[1].items():
				modelo = Modelo.fromJSON(item, key)
				modelos.update({ key: modelo })


def sync():
	return db.reference('/modelos').listen(change)
