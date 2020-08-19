from firebase_admin import db

from models.arquitetura import Arquitetura
from repositories.json import FirebaseJSON

arquiteturas: dict = {}
etag: str = None


def change(event):
	global arquiteturas
	global etag
	if etag == None:
		ret = db.reference('/arquiteturas').get(etag=True)
		etag = ret[1]
		for key, item in ret[0].items():
			arquitetura = Arquitetura.fromJSON(item, key)
			arquiteturas.update({ key: arquitetura })
	else:
		ret = db.reference('/arquiteturas').get_if_changed(etag)
		if ret[0]:
			etag = ret[2]
			arquiteturas.clear()
			for key, item in ret[1].items():
				arquitetura = Arquitetura.fromJSON(item, key)
				arquiteturas.update({ key: arquitetura })


def sync():
	return change()
