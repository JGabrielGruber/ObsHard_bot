class Bot():
	def __init__(self,
	             intervalo: int = 0,
	             ativo: bool = False,
	             status: str = '',
	             log: list = []):
		self.status = status
		self.intervalo = intervalo
		self.ativo = ativo
		self.log = log

	@classmethod
	def fromJSON(cls, json):
		return cls(json.get('intervalo', None), json.get('ativo', None),
		           json.get('status', None), json.get('log', None))

	def updateFromJSON(self, json):
		self.intervalo = json.get('intervalo', self.intervalo)
		self.ativo = json.get('ativo', self.ativo)
		self.status = json.get('status', self.status)
		self.log = json.get('log', self.log)
