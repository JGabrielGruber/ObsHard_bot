from models.loja import Loja
from models.variacao import Variacao


class Produto:
	def __init__(self,
	             loja: Loja,
	             variacao: Variacao,
	             link: str,
	             _id: str = None):
		self._id = _id
		self.loja = loja
		self.variacao = variacao
		self.link = link

	@classmethod
	def fromJSON(cls, json, id):
		return cls(None, None, json['link'], id if id else None)