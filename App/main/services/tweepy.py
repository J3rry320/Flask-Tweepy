import tweepy
from os import getenv

if getenv("consumer_key") != None:
    auth = tweepy.OAuthHandler(
        getenv("consumer_key"), getenv("consumer_secret"))
    auth.set_access_token(getenv("access_key"),
                          getenv("access_secret"))
    twitter = tweepy.API(auth)
else:
    twitter = None
