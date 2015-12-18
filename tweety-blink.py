from app.authenticator import authenticator
from app.listener import listener
from tweepy import Stream
import sys
import json
from time import sleep

AUTH_FILENAME = 'auth.json'
search_terms = ['#yolo','#blessed','#christmas','#christmakkuh']

#TODO: Make classierer
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
stream = Stream(auth=authenticator.authenticate(credentials).auth, listener=tweet_listener)

try:
    stream.filter(track=search_terms,async=True)
    choice = input("Press enter to abort")
    raise KeyboardInterrupt
except KeyboardInterrupt:
    stream.disconnect()
    sleep(1)
    tweet_listener.__exit__(0,0,0)
    print("\nGraceful shutdown successful.")
except:
    print("Unexpected exception: {}".format(sys.exc_info()[0]))
    raise
