from models.marca import Marca
from models.arquitetura import Arquitetura


class Modelo():
	def __init__(self,
	             marca: Marca,
	             arquitetura: Arquitetura,
	             ano: int,
	             nome: str,
	             _id: str = None):
		self._id = _id
		self.marca = marca
		self.arquitetura = arquitetura
		self.ano = ano
		self.nome = nome
