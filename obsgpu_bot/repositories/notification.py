from firebase_admin import db

from models.notification import Notification
from repositories.json import FirebaseJSON

notifications: [] = []
etag: str = None


def change(event):
	global notifications
	global etag
	if etag == None:
		ret = db.reference('/notificacoes').get(etag=True)
		etag = ret[1]
		notifications.updateFromJSON(ret[0])
	else:
		ret = db.reference('/notificacoes').get_if_changed(etag)
		if ret[0]:
			etag = ret[2]
			notifications.updateFromJSON(ret[1])


def sync():
	return db.reference('/notificacoes').listen(change)


def addNotification(notification):
	data: list = notifications
	if len(data) > 100:
		data.pop(0)
	data.append(notification)
	if etag != None:
		update(data)