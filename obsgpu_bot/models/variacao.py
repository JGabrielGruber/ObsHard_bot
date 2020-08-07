from models.modelo import Modelo


class Variacao():
	def __init__(self, nome: str, _id: str = None):
		self._id = _id
		self.nome = nome

	@classmethod
	def fromJSON(cls, json, id=None):
		return cls(json['nome'], id or None)