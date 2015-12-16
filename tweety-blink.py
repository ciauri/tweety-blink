from app.authenticator import authenticator
from app.listener import listener
from tweepy import Stream
import sys
import json

AUTH_FILENAME = 'auth.json'

#TODO: Make classier
try:
    with open(AUTH_FILENAME) as auth_data:
        credentials = json.load(auth_data)
except FileNotFoundError as e:
    raise RuntimeError("auth.json file not found")
except ValueError as e:
    raise ValueError("Your auth.json file is malformed")
except:
    print("Unexpected exception: {}".format(sys.exc_info()[0]))
    raise


tweet_listener = listener.TweetListener()
try:
    stream = Stream(auth=authenticator.authenticate(credentials).auth, listener=tweet_listener)
    stream.filter(track=['#yolo','#blessed','#christmas','#christmakkuh'])
except KeyboardInterrupt:
    tweet_listener.__exit__(0,0,0)
    print("\nGraceful shutdown successful.")
except:
    print("Unexpected exception: {}".format(sys.exc_info()[0]))
    raise
