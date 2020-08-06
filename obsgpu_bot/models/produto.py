from models.loja import Loja
from models.variacao import Variacao
from models.modelo import Modelo


class Produto:
	def __init__(self,
	             loja: Loja,
	             variacao: Variacao,
	             modelo: Modelo,
	             link: str,
	             status: str = "ok",
	             precos: list = None,
	             _id: str = None):
		self._id = _id
		self.loja = loja
		self.variacao = variacao
		self.modelo = modelo
		self.link = link
		self.status = status
		self.precos = precos

	@classmethod
	def fromJSON(cls, json, id=None):
		return cls(None, None, None, json['link'], json.get('status', None),
		           json.get('precos', None), id if id else None)
