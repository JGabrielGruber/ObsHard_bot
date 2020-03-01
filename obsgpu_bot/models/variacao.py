from obsgpu_bot.models.modelo import Modelo


class Variacao():
	def __init__(self, modelo: Modelo, nome: str):
		self.modelo = modelo
		self.nome = nome
