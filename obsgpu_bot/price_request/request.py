import requests
import locale

from bs4 import BeautifulSoup

class Loja:
	def __init__(self, nome: str, tag: str, propriedade: str, atributo: str):
		self.nome = nome
		self.tag = tag
		self.propriedade = propriedade
		self.atributo = atributo


class Produto:
	def __init__(self, loja: Loja, link: str):
		self.loja = loja
		self.link = link
		locale.setlocale(locale.LC_NUMERIC, "nl")


def getPreco(produto: Produto) -> float:
	try:
		html = requests.get(produto.link)
		soup = BeautifulSoup(html.text, "html.parser")
		price = soup.find(
		    produto.loja.tag,
		    attrs={produto.loja.propriedade: produto.loja.atributo})
		return float(price["content"])
	except ValueError:
		return locale.atof(price["content"])
	except KeyError:
		return locale.atof(price.contents[0].string.split(" ", 1)[1])
	except Exception:
		return 0.0


produto_um = Produto(
    Loja("Pichau", "meta", "property", "product:price:amount"),
    "https://www.pichau.com.br/processador-amd-ryzen-3-3200g-quad-core-3-6ghz-4ghz-turbo-6mb-cache-am4-yd3200c5fhbox",
)

produto_dois = Produto(
    Loja("Kabum", "meta", "itemprop", "price"),
    "https://www.kabum.com.br/produto/102248/processador-amd-ryzen-3-3200g-cache-4mb-3-6ghz-4ghz-max-turbo-am4-yd3200c5fhbox/?tag=ryzen%203%203200g",
)

produto_tres = Produto(
    Loja("Terabyte", "p", "id", "valVista"),
    "https://www.terabyteshop.com.br/produto/11543/processador-amd-ryzen-3-3200g-36ghz-40ghz-turbo-4-core-4-thread-cooler-wraith-stealth-am4",
)

print(getPreco(produto_um))
print(getPreco(produto_dois))
print(getPreco(produto_tres))