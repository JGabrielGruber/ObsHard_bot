from models.produto import Produto
from models.loja import Loja
from models.variacao import Variacao
from models.modelo import Modelo
from models.arquitetura import Arquitetura
from models.marca import Marca
from repositories import modelo as rep_modelo
from repositories import loja as rep_loja
from repositories import produto as rep_produto
from price_request import req
import main

import inspect
from firebase_admin.db import Reference

id: str = None


def test_fetchPreco():
	if main.fb_app is None:
		main.defineConfigs()
	l = Loja("Kabum", "meta", "itemprop", "price")
	l = rep_loja.add(l)
	l = rep_loja.getById(l._id)
	p = Produto(l, Variacao(Modelo(Marca(""), Arquitetura("", 0), 2020, "teste"), "AMD Ryzen 5 1600"), "https://www.kabum.com.br/produto/107545/processador-amd-ryzen-5-1600-cache-19mb-3-2ghz-3-6ghz-max-turbo-am4-yd1600bbafbox")
	p = rep_produto.add(p)
	p = rep_produto.getById(p._id)
	preco = req.fetchPreco(p)
	assert type(preco) is Produto

def test_getProdutosPrecos():
	if main.fb_app is None:
		main.defineConfigs()
	assert req.getProdutos() is None