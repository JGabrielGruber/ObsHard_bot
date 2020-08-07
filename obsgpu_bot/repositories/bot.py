from firebase_admin import db

from models.bot import Bot
from repositories.json import FirebaseJSON

bot: Bot = Bot()
etag: str = None


def change(event):
	global bot
	global etag
	if etag == None:
		ret = db.reference().child('bot').get(etag=True)
		etag = ret[1]
		bot.updateFromJSON(ret[0])
	else:
		ret = db.reference().child('bot').get_if_changed(etag)
		if ret[0]:
			etag = ret[2]
			bot.updateFromJSON(ret[1])
	print(bot.ativo)


def sync():
	return db.reference().child('bot').listen(change)


def update(data):
	db.reference().child('bot').set(FirebaseJSON().encode(data))
