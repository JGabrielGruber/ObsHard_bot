import tweepy

from main import tw_api


def setStatus():
	tw_api.update_status("Hello Tweepy(World)")