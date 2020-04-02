from models.arquitetura import Arquitetura
from repositories import arquitetura
import main

import inspect
from firebase_admin.db import Reference

id: str = None

def test_get():
	if main.fb_app is None:
		main.defineConfigs()
	assert type(arquitetura.get()) is list

def test_add():
	global id
	if main.fb_app is None:
		main.defineConfigs()
	t = arquitetura.add(
		Arquitetura(
			"teste",
			2020
		)
	)
	id = t[1]
	assert type(t) is tuple

def test_upd():
	if main.fb_app is None:
		main.defineConfigs()
	if id is None:
		test_add()
	t = arquitetura.upd(
		Arquitetura(
			"testa atualizado",
			2020,
			id
		)
	)
	assert type(t) is tuple

def test_rmv():
	if main.fb_app is None:
		main.defineConfigs()
	if id is None:
		test_add()
	assert arquitetura.rmv(
		Arquitetura(
			"",
			0,
			id
		)
	) is None