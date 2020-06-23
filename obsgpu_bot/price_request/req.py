import requests
import locale
import datetime

from bs4 import BeautifulSoup
from models.loja import Loja
from models.produto import Produto
from repositories import produto as rep_produto


def fetchPreco(produto: Produto) -> Produto:
	locale.setlocale(locale.LC_NUMERIC, "pt_BR.UTF-8")
	price = {}
	val = 0.0
	status = 'ok'
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
	except ConnectionError:
		status = 'off'
	except Exception as e:
		print(e)
		status = 'err'
	finally:
		produto.status = status
		if val > 0.0 and (not produto.precos or produto.precos[len(produto.precos) - 1][0] != val):
			if not produto.precos:
				produto.precos = []
			produto.precos.append(
			    [
			        val,
			        datetime.datetime.now().timestamp()
			    ]
			)
		return produto


def getProdutos():
	produtos: list = rep_produto.get()
	for item in produtos:
		(lambda p : rep_produto.upd(p) if p.precos is item.precos else None)(fetchPreco(item))