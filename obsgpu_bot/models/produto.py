from models.loja import Loja
from models.variacao import Variacao


class Produto:
	def __init__(self,
	             loja: Loja,
	             variacao: Variacao,
	             link: str,
	             status: str = "ok",
	             precos: list = None,
	             _id: str = None):
		self._id = _id
		self.loja = loja
		self.variacao = variacao
		self.link = link
		self.status = status
		self.precos = precos

	@classmethod
	def fromJSON(cls, json, id=None):
		return cls(None, None, json['link'], json.get('status', None), json.get('precos', None), id if id else None)