from firebase_admin import db

from models.notification import Notification
from repositories.json import FirebaseJSON

from time import sleep

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
	return change()


def addNotification(notification):
	try:
		if etag != None:
			db.reference('/notificacoes').push(FirebaseJSON().encode(notification))
	except Exception:
		sleep(1)
		addNotification(notification)
