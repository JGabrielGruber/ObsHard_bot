import requests
import locale

from bs4 import BeautifulSoup
from models.loja import Loja
from models.produto import Produto
from repositories import produto


def getPreco(produto: Produto) -> float:
	locale.setlocale(locale.LC_NUMERIC, "pt_BR.UTF-8")
	price = {}
	try:
		html = requests.get(produto.link)
		soup = BeautifulSoup(html.text, "html.parser")
		price = soup.find(
		    produto.loja.tag,
		    attrs={produto.loja.propriedade: produto.loja.atributo})
		return float(price["content"])
	except ValueError:
		try:
			return locale.atof(price["content"])
		except KeyError:
			return locale.atof(price.contents[0].string.split(" ", 1)[1])
	finally:
		return 0.0


def getProdutos():
	produtos: list = produto.get()
	precos: list = []
	for item in produtos:
		precos.append(getPreco(item))
	return precos