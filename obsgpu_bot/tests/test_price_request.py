from models.produto import Produto
from models.loja import Loja
from models.variacao import Variacao
from models.modelo import Modelo
from models.arquitetura import Arquitetura
from models.marca import Marca
from repositories import modelo
from repositories import loja
from price_request import req
import main

import inspect
from firebase_admin.db import Reference

id: str = None


def test_get():
	if main.fb_app is None:
		main.defineConfigs()
	l = Loja("Kabum", "meta", "itemprop", "price")
	p = Produto(l, Variacao(Modelo(Marca(""), Arquitetura("", 0), 2020, "teste"), "ASRock B450M-HDV R4.0"), "https://www.kabum.com.br/produto/111107/placa-m-e-asrock-b450m-hdv-r4-0-amd-am4-micro-atx-ddr4-")
	preco = req.getPreco(p)
	print(preco)
	assert type(preco) is float