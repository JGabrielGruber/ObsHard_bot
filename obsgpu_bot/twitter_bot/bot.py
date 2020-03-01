import tweepy

from obsgpu_bot.main import api


def setStatus():
	api.update_status("Hello Tweepy(World)")