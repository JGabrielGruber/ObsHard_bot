import main
import asyncio
import concurrent.futures
import datetime
import logging

from aiohttp import ClientSession

from repositories import bot as botRepo
from repositories import loja as lojaRepo
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
	print('Waiting for Repos...')
	await asyncio.create_task(waitUntil(produtoRepo))
	await asyncio.create_task(waitUntil(lojaRepo))
	await asyncio.create_task(waitUntil(botRepo))
	print('Done')
	semaphore = asyncio.Semaphore(
	    10)  # Max limit 1000, limited to 10 to avoid spamming

	while True:
		if botRepo.bot.ativo:
			print('Requesting prices...')
			async with ClientSession() as session:
				await asyncio.gather(
				    *(req.getPreco(produto, key, semaphore, session)
				      for key, produto in produtoRepo.produtos.items()))
			print('Done')
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

print = logging.info

print('Starting the bot...')

if main.fb_app is None:
	print('Configuring Firebase...')
	main.defineConfigs()
	print('Done')

print('Starting Repos Sync...')
botRepo.sync()
lojaRepo.sync()
produtoRepo.sync()
print('Done')

asyncio.run(run())