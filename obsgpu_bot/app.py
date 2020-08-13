import main
import asyncio
import concurrent.futures
import datetime
import logging

from aiohttp import ClientSession

from repositories import bot as botRepo
from repositories import loja as lojaRepo
from repositories import marca as marcaRepo
from repositories import modelo as modeloRepo
from repositories import notification as notificationRepo
from repositories import produto as produtoRepo
from price_request import req
from models.produto import Produto
from lib.callbackHandler import CallbackHandler


async def waitUntil(repo):
	c = True
	while c:
		if repo.etag != None:
			c = False
			return
		await asyncio.sleep(0.5)


async def run():
	logging.info('Waiting for Repos...')
	await asyncio.create_task(waitUntil(produtoRepo))
	await asyncio.create_task(waitUntil(lojaRepo))
	await asyncio.create_task(waitUntil(botRepo))
	logging.info('Done')
	semaphore = asyncio.Semaphore(
	    10)  # Max limit 1000, limited to 10 to avoid spamming

	while True:
		if botRepo.bot.ativo:
			logging.info('Requesting prices...')
			async with ClientSession() as session:
				await asyncio.gather(
				    *(req.getPreco(produto, key, semaphore, session)
				      for key, produto in produtoRepo.produtos.items()))
			logging.info('Done')
			await asyncio.sleep((float(botRepo.bot.intervalo) or 1) * 60)
		await asyncio.sleep(1)


logging.basicConfig(
    filename='obshard.log',
    filemode='a',
    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
    datefmt='%H:%M:%S',
    level=logging.INFO)
console = logging.StreamHandler()
console.setLevel(logging.INFO)
logging.getLogger('').addHandler(console)
botLog = CallbackHandler()
botLog.setLevel(logging.INFO)
botLog.callback = botRepo.addLog
logging.getLogger('').addHandler(botLog)

logging.info('Starting the bot...')

if main.fb_app is None:
	logging.info('Configuring Firebase...')
	main.defineConfigs()
	logging.info('Done')

logging.info('Starting Repos Sync...')
botRepo.sync()
lojaRepo.sync()
marcaRepo.sync()
modeloRepo.sync()
notificationRepo.sync()
produtoRepo.sync()
logging.info('Done')

asyncio.run(run())