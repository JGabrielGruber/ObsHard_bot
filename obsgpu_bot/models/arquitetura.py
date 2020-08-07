from models.categoria import Categoria


class Arquitetura():
	def __init__(self,
	             nome: str,
	             ano: int,
	             categoria: str = None,
	             _id: str = None):
		self.categoria = categoria
		self._id = _id
		self.nome = nome
		self.ano = ano

	@classmethod
	def fromJSON(cls, json, id=None):
		return cls(json['nome'], json['ano'], json.get('categoria', None), id
		           or None)
