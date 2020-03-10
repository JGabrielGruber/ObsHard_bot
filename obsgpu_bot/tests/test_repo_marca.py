from models.marca import Marca
from repositories import marca
import main

import inspect
from firebase_admin.db import Reference

def test_get():
	main.defineConfigs()
	assert type(marca.get()) is list

def test_add():
	main.defineConfigs()
	t = marca.add(
		Marca(
			"teste"
		)
	)
	assert type(t) is tuple