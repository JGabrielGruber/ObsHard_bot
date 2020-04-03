from json import JSONEncoder

class FirebaseJSON(JSONEncoder):
	def encode(self, o):
		obj = o.__dict__
		for attrib in obj:
			if attrib is '_id':
				obj[attrib] = None
			if hasattr(obj[attrib], '__dict__'):
				obj[attrib] = obj[attrib]._id
		return obj