from models.modelo import Modelo
from models.arquitetura import Arquitetura
from models.marca import Marca
from repositories import modelo
import main

import inspect
from firebase_admin.db import Reference

id: str = None


def test_get():
	if main.fb_app is None:
		main.defineConfigs()
	assert type(modelo.get()) is list


def test_add():
	global id
	if main.fb_app is None:
		main.defineConfigs()
	t = modelo.add(Modelo(Marca(""), Arquitetura("", 0), 2020, "teste"))
	id = t._id
	assert type(t) is Modelo


def test_getById():
	if main.fb_app is None:
		main.defineConfigs()
	if id is None:
		test_add()
	t = modelo.getById(id)
	test_rmv()
	assert type(t) is Modelo


def test_upd():
	if main.fb_app is None:
		main.defineConfigs()
	if id is None:
		test_add()
	t = modelo.upd(
	    Modelo(Marca(""), Arquitetura("", 0), 2020, "teste atualizado", id))
	test_rmv()
	assert type(t) is Modelo


def test_rmv():
	if main.fb_app is None:
		main.defineConfigs()
	if id is None:
		test_add()
	assert modelo.rmv(Modelo(Marca(""), Arquitetura("", 0), 0, "", id)) is None
