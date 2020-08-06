class Bot():
	def __init__(self, intervalo: int = 0, ativo: bool = false, status: str = '', log: list = []):
		self.status = status
		self.intervalo = intervalo
		self.ativo = ativo
		self.log = log

	@classmethod
	def fromJSON(cls, json):
		return cls(json['intervalo'], json['ativo'], json['status'], json['log'])
