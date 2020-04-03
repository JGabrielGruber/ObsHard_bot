class Marca():
	def __init__(self, nome: str, _id: str = None):
		self.nome = nome
		self._id = _id

	@classmethod
	def fromJSON(cls, json, id):
		return cls(json['nome'], id if id else None)
