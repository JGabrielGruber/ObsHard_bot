from firebase_admin import db

from models.notification import Notification
from repositories.json import FirebaseJSON

notifications: list = []
etag: str = None


def change(event):
	global notifications
	global etag
	if etag == None:
		ret = db.reference('/notificacoes').get(etag=True)
		etag = ret[1]
		i = 0
		for key, item in ret[0].items():
			notification = Notification.fromJSON(item)
			notifications.insert(i, notification)
			i += 1
	else:
		ret = db.reference('/notificacoes').get_if_changed(etag)
		if ret[0]:
			etag = ret[2]
			notifications.clear()
			i = 0
			for key, item in ret[1].items():
				notification = Notification.fromJSON(item)
				notifications.insert(i, notification)
				i += 1


def sync():
	return db.reference('/notificacoes').listen(change)


def addNotification(notification):
	if etag != None:
		db.reference('/notificacoes').push(FirebaseJSON().encode(notification))
