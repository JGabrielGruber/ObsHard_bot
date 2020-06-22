from models.modelo import Modelo


class Variacao():
	def __init__(self, modelo: Modelo, nome: str, _id: str = None):
		self._id = _id
		self.modelo = modelo
		self.nome = nome

	@classmethod
	def fromJSON(cls, json, id=None):
		return cls(None, json['nome'], id if id else None)