from models.bot import Bot
from repositories import bot
import main

import inspect
from firebase_admin.db import Reference

id: str = None


def test_sync():
	if main.fb_app is None:
		main.defineConfigs()
	print("aaaaaaaaaaaaaaaaaaaaaaa")
	liste = bot.sync()
	b = bot.bot
	print(liste)
	t = 20
	while t:
		mins, secs = divmod(t, 60)
		timer = '{:02d}:{:02d}'.format(mins, secs)
		print(timer, end="\r")
		print(b.ativo)
		time.sleep(1)
		t -= 1
	assert True
