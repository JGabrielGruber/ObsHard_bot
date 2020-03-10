class Loja:
	def __init__(self,
	             nome: str,
	             tag: str,
	             propriedade: str,
	             atributo: str,
	             _id: str = None):
		self._id = _id
		self.nome = nome
		self.tag = tag
		self.propriedade = propriedade
		self.atributo = atributo