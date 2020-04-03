from models.marca import Marca
from repositories import marca
import main

import inspect
from firebase_admin.db import Reference

id: str = None


def test_get():
	if main.fb_app is None:
		main.defineConfigs()
	assert type(marca.get()) is list


def test_add():
	global id
	if main.fb_app is None:
		main.defineConfigs()
	t = marca.add(Marca("teste"))
	id = t._id
	assert type(t) is Marca


def test_getByID():
	if main.fb_app is None:
		main.defineConfigs()
	if id is None:
		test_add()
	t = marca.getById(id)
	test_rmv()
	assert type(t) is Marca


def test_upd():
	if main.fb_app is None:
		main.defineConfigs()
	if id is None:
		test_add()
	t = marca.upd(Marca("testa atualizado", id))
	test_rmv()
	assert type(t) is Marca


def test_rmv():
	if main.fb_app is None:
		main.defineConfigs()
	if id is None:
		test_add()
	assert marca.rmv(Marca("", id)) is None
