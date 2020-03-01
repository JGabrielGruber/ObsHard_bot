import tweepy
import json

__CONFPATH__ = "../config.json"
api: tweepy.API = None


def loadConfigs():
	try:
		with open(__CONFPATH__) as f:
			return json.load(f)
	except:
		return None


def defineConfigs():
	global api

	confs = loadConfigs()
	if confs:
		try:
			auth = tweepy.OAuthHandler(confs["TWITTER_API"]["CONSUMER_KEY"],
			                           confs["TWITTER_API"]["CONSUMER_SECRET"])
			auth.set_access_token(
			    confs["TWITTER_API"]["ACCESS_TOKEN"]["KEY"],
			    confs["TWITTER_API"]["ACCESS_TOKEN"]["SECRET"])

			api = tweepy.API(auth)
		except ValueError as e:
			raise Exception(
			    "Please, define the config.json file as the config.json.example!"
			)

	else:
		raise Exception(
		    "Please, create the config.json file as the config.json.example!")


defineConfigs()