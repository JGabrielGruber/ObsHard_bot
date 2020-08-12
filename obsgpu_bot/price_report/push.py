import asyncio

from models.marca import Marca
from models.modelo import Modelo
from models.notification import Notification
from models.produto import Produto
from repositories import marca as marcaRepo
from repositories import modelo as modeloRepo
from repositories import notification as notificationRepo

async def sendNotification(produto: Produto):
	modelo: Modelo = modeloRepo.modelos.get(produto.modelo, '')
	marca: Marca = marcaRepo.marcas.get(modelo.marca or '', '')
	title = f'{marca} {modelo}'
	content = f'{produto.precos[-2:][0:][0:]} -> {produto.precos[-1:][0:]}'
	timestamp = produto.precos[-1:][1:]
	notification = Notification(
		title,
		content,
		timestamp,
		key=produto._id
	)
	return notificationRepo.addNotification(notification)