from models.loja import Loja
from repositories import loja
import main

import inspect
from firebase_admin.db import Reference

id: str = None


def test_get():
	if main.fb_app is None:
		main.defineConfigs()
	assert type(loja.get()) is list


def test_add():
	global id
	if main.fb_app is None:
		main.defineConfigs()
	t = loja.add(Loja("test", "tag", "prop", "atrib"))
	id = t[1]
	assert type(t) is tuple


def test_upd():
	if main.fb_app is None:
		main.defineConfigs()
	if id is None:
		test_add()
	t = loja.upd(Loja("test atualizado", "taga", "prop", "atrib", id))
	assert type(t) is tuple


def test_rmv():
	if main.fb_app is None:
		main.defineConfigs()
	if id is None:
		test_add()
	assert loja.rmv(Loja("", "", "", "", id)) is None
