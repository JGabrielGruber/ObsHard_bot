import requests
import locale

from bs4 import BeautifulSoup
from models.loja import Loja
from models.produto import Produto
from repositories import produto


def getPreco(produto: Produto) -> float:
	locale.setlocale(locale.LC_NUMERIC, "pt_BR.UTF-8")
	price = {}
	val = 0.0
	try:
		html = requests.get(produto.link)
		soup = BeautifulSoup(html.text, "html.parser")
		price = soup.find(
		    produto.loja.tag,
		    attrs={produto.loja.propriedade: produto.loja.atributo})
		val = float(price["content"])
	except ValueError:
		try:
			val = locale.atof(price["content"])
		except KeyError:
			val = locale.atof(price.contents[0].string.split(" ", 1)[1])
	finally:
		return val


def getProdutos():
	produtos: list = produto.get()
	precos: list = []
	for item in produtos:
		precos.append(getPreco(item))
	return precos