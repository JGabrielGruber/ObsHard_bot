from models.marca import Marca
from models.arquitetura import Arquitetura


class Modelo():
	def __init__(self,
	             ano: int,
	             nome: str,
	             marca: str = None,
	             arquitetura: str = None,
	             _id: str = None):
		self._id = _id
		self.ano = ano
		self.nome = nome
		self.marca = marca
		self.arquitetura = arquitetura

	@classmethod
	def fromJSON(cls, json, id=None):
		return cls(json['ano'], json['nome'], json.get('marca', None),
		           json.get('arquitetura', None), id or None)
