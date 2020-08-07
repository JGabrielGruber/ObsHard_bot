class Marca():
	def __init__(self, nome: str, _id: str = None):
		self.nome = nome
		self._id = _id

	@classmethod
	def fromJSON(cls, json, id=None):
		return cls(json['nome'], id or None)
