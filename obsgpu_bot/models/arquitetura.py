from models.categoria import Categoria

class Arquitetura():
	def __init__(self, categoria: Categoria, nome: str, ano: int, _id: str = None):
		self.categoria = categoria
		self._id = _id
		self.nome = nome
		self.ano = ano

	@classmethod
	def fromJSON(cls, json, id=None):
		return cls(None, json['nome'], json['ano'], id if id else None)
