from obsgpu_bot.models.marca import Marca
from obsgpu_bot.models.arquitetura import Arquitetura


class Modelo():
	def __init__(self, marca: Marca, arquitetura: Arquitetura, ano: int,
	             nome: str):
		self.marca = marca
		self.arquitetura = arquitetura
		self.ano = ano
		self.nome = nome
