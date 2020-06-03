from .tweepy import twitter
from flask import jsonify


def search_users(query):
    if twitter != None:
        users = []
        responses = twitter.search_users(query)
        for response in responses:
            users.append(response._json)
        return jsonify(users)
