from json import JSONEncoder

class FirebaseJSON(JSONEncoder):
	def encode(self, o):
		return o.__dict__