from models.loja import Loja
from models.variacao import Variacao
from models.modelo import Modelo


class Produto:
	def __init__(self,
	             link: str,
	             status: str = "ok",
	             precos: list = None,
	             loja: str = None,
	             variacao: str = None,
	             modelo: str = None,
	             _id: str = None):
		self._id = _id
		self.link = link
		self.status = status
		self.precos = precos
		self.loja = loja
		self.variacao = variacao
		self.modelo = modelo

	@classmethod
	def fromJSON(cls, json, id=None):
		return cls(json['link'], json.get('status', None),
		           json.get('precos', None), json.get('loja', None),
		           json.get('variacao', None), json.get('modelo', None),
		           id or None)
