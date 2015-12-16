from app.authenticator import authenticator
from app.listener import listener
from tweepy import Stream
import json

AUTH_FILENAME = 'auth.json'

#TODO: Make classierd
try:
    with open(AUTH_FILENAME) as auth_data:
        credientials = json.load(auth_data)
except FileNotFoundError as e:
    raise RuntimeError("auth.json file not found")
except ValueError as e:
    raise ValueError("Your auth.json file is malformed")


tweet_listener = listener.TweetListener()
try:
    stream = Stream(auth=authenticator.authenticate(credientials).auth, listener=tweet_listener)
    stream.filter(track=['#yolo','#blessed','#christmas','#christmakkuh'])
except KeyboardInterrupt:
    tweet_listener.__exit__(0,0,0)
    print("\nGraceful shutdown successful.")
finally:
    print("something broke")
