from models.produto import Produto
from models.variacao import Variacao
from models.loja import Loja
from models.arquitetura import Arquitetura
from models.modelo import Modelo
from models.marca import Marca
from repositories import produto
import main

import inspect
from firebase_admin.db import Reference

id: str = None


def test_get():
	if main.fb_app is None:
		main.defineConfigs()
	assert type(produto.get()) is list


def test_add():
	global id
	if main.fb_app is None:
		main.defineConfigs()
	t = produto.add(Produto(Loja("Kabum", "meta", "itemprop", "price"), Variacao(Modelo(Marca(""), Arquitetura("", 0), 2020, "teste"), "ASRock B450M-HDV R4.0"), "https://www.kabum.com.br/produto/111107/placa-m-e-asrock-b450m-hdv-r4-0-amd-am4-micro-atx-ddr4-"))
	id = t._id
	assert type(t) is Produto


def test_getById():
	if main.fb_app is None:
		main.defineConfigs()
	if id is None:
		test_add()
	t = produto.getById(id)
	test_rmv()
	assert type(t) is Produto


def test_upd():
	if main.fb_app is None:
		main.defineConfigs()
	if id is None:
		test_add()
	t = produto.upd(
	    Produto(Loja("test", "tag", "prop", "atrib"), Variacao(Modelo(Marca(""), Arquitetura("", 0), 2020, "teste"), "teste"), "teste", id))
	test_rmv()
	assert type(t) is Produto


def test_rmv():
	if main.fb_app is None:
		main.defineConfigs()
	if id is None:
		test_add()
	assert produto.rmv(Produto(Loja("test", "tag", "prop", "atrib"), Variacao(Modelo(Marca(""), Arquitetura("", 0), 2020, "teste"), "teste"), "teste", id)) is None
