from tweepy import StreamListener

class TweetListener(StreamListener):

    def on_status(self, status):
        print("Tweet: {}".format(status.text))
        # And anything else we want to do AKA make light blink or whatever