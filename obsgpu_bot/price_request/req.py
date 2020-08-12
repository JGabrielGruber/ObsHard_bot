import aiohttp
import asyncio
import locale
import datetime
import random
import sys, os
import logging

from bs4 import BeautifulSoup
from models.loja import Loja
from models.produto import Produto
from repositories import produto as produtoRepo
from repositories import loja as lojaRepo


async def fetch(url, session):
	async with session.get(url) as response:
		date = response.headers.get("DATE")
		logging.info("{} - {}".format(response.status, response.url))
		return await response.read()


async def bound_fetch(sem, url, session):
	async with sem:
		return await fetch(url, session)


async def fetchPreco(produto: Produto, key: str, loja: Loja, semaphore,
                     session, callback):
	if produto and loja:
		locale.setlocale(locale.LC_NUMERIC, "pt_BR.UTF-8")
		price = None
		val = 0.0
		status = 'ok'
		try:
			if loja.nome == 'Pichau':
				asyncio.sleep(random.randrange(1, 9))
			text = await bound_fetch(semaphore, produto.link, session)
			soup = BeautifulSoup(text, "html.parser")
			price = soup.find(loja.tag,
			                  attrs={loja.propriedade: loja.atributo})
			if price != None:
				if loja.nome == 'Kabum' && soup.find('div',
			                  attrs={'class': 'botao-comprar'}) != None:
					val = float(price["content"])
				elif loja.nome == 'Pichau' && soup.find('div',
			                  attrs={'class': 'stock available'}) != None:
					val = locale.atof(price.contents[1].string.split('R$')[1])
				elif loja.nome == 'TerabyteShop' && soup.find('div',
			                  attrs={'id': 'indisponivel'}) == None:
					val = locale.atof(price.contents[0])
				else:
					status = 'no'
		except ValueError:
			status = 'ba'
		except ConnectionError:
			status = 'of'
		except Exception as e:
			exc_type, exc_obj, exc_tb = sys.exc_info()
			fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
			logging.info(e)
			logging.error(exc_type, fname, exc_tb.tb_lineno)
			status = 'er'
		finally:
			if val > 0.0 && (
			    not produto.precos
			    || produto.precos[len(produto.precos) - 1][0] != val):
				if not produto.precos:
					produto.precos = []
				produto.status = status
				produto.precos.append(
				    [val, datetime.datetime.now().timestamp()])
				return callback(produto, key)
			elif produto.status != status:
				produto.status = status
				return callback(produto, key)


def getProdutos():
	produtos: list = produtoRepo.get()
	for item in produtos:
		(lambda p: produtoRepo.upd(p)
		 if p.precos is item.precos else None)(fetchPreco(item))


async def getPreco(produto: Produto, key: str, semaphore, session):
	loja = lojaRepo.lojas.get(produto.loja, None)
	asyncio.sleep(random.randrange(1, 9) * 0.1)
	data = await fetchPreco(produto, key, loja, semaphore, session,
	                        produtoRepo.update)
