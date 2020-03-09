import tweepy
import json
import firebase_admin

from firebase_admin import db, credentials

__CONFPATH__ = "config.json"
tw_api: tweepy.API = None
fb_app: firebase_admin.App = None


def loadConfigs():
	try:
		with open(__CONFPATH__) as f:
			return json.load(f)
	except Exception:
		return None


def defineConfigs():
	global tw_api
	global fb_app

	confs = loadConfigs()
	if confs:
		try:
			auth = tweepy.OAuthHandler(confs["TWITTER_API"]["CONSUMER_KEY"],
			                           confs["TWITTER_API"]["CONSUMER_SECRET"])
			auth.set_access_token(
			    confs["TWITTER_API"]["ACCESS_TOKEN"]["KEY"],
			    confs["TWITTER_API"]["ACCESS_TOKEN"]["SECRET"])

			tw_api = tweepy.API(auth)

			fb_cre = firebase_admin.credentials.Certificate(
			    confs["FIREBASE_API"]["SERVICEACOUNTKEY_PATH"])
			fb_app = firebase_admin.initialize_app(
			    fb_cre, {"databaseURL": confs["FIREBASE_API"]["DATABASE_URL"]})
		except ValueError as e:
			raise Exception(
			    "Please, define the config.json file as the config.json.example!"
			)

	else:
		raise Exception(
		    "Please, create the config.json file as the config.json.example!")


def main():
	defineConfigs()

	from repositories import repo
	from twitter_bot import bot
	from price_request import req