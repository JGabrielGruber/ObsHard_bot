class Notification():
	def __init__(self, title: str, content: str, timestamp: float, key: str):
		self.title = title
		self.content = content
		self.timestamp = timestamp
		self.key = key

	@classmethod
	def fromJSON(cls, json):
		return cls(json['title'], json['content'], json['timestamp'],
		           json.get('key', ''))
