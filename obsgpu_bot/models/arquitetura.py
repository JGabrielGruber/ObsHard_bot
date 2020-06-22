class Arquitetura():
	def __init__(self, nome: str, ano: int, _id: str = None):
		self._id = _id
		self.nome = nome
		self.ano = ano

	@classmethod
	def fromJSON(cls, json, id=None):
		return cls(json['nome'], json['ano'], id if id else None)
