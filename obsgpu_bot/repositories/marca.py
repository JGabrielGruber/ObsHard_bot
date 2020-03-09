from firebase_admin import db

from models.marca import Marca
from repositories.json import FirebaseJSON

marcas = None

def get():
	return db.reference('/marcas').get(etag=True)

def add(marca: Marca):
	return db.reference('/marcas').push(FirebaseJSON().encode(marca)).get(etag=True)
