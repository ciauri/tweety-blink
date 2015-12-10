from app.authenticator import authenticator
from app.listener import listener
from tweepy import Stream
import json

AUTH_FILENAME = 'auth.json'

#TODO: Make classier
try:
    with open(AUTH_FILENAME) as auth_data:
        credientials = json.load(auth_data)
except FileNotFoundError as e:
    raise RuntimeError("auth.json file not found")
except ValueError as e:
    raise ValueError("Your auth.json file is malformed")

tweet_listener = listener.TweetListener()
stream = Stream(auth=authenticator.authenticate(credientials).auth, listener=tweet_listener)
stream.filter(track=['#yolo'])
