import asyncio
import locale

from models.marca import Marca
from models.modelo import Modelo
from models.notification import Notification
from models.produto import Produto
from repositories import marca as marcaRepo
from repositories import modelo as modeloRepo
from repositories import notification as notificationRepo

async def sendNotification(produto: Produto):
	locale.setlocale(locale.LC_MONETARY, "pt_BR.UTF-8")
	modelo: Modelo = modeloRepo.modelos.get(produto.modelo, None)
	marca: Marca = marcaRepo.marcas.get(modelo.marca, None) if modelo else None
	modelo = modelo.nome if modelo else ''
	marca = marca.nome if marca else ''
	title = f'{marca} {modelo}'
	pm = locale.currency(produto.precos[-2:][0][0], grouping=True)
	pa = locale.currency(produto.precos[-1:][0][0], grouping=True)
	content = f'{pm} -> {pa}'
	timestamp = produto.precos[-1:][0][1]
	notification = Notification(
		title,
		content,
		timestamp,
		key=produto._id
	)
	return notificationRepo.addNotification(notification)