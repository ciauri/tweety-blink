from tweepy import StreamListener

import RPi.GPIO as GPIO
import time

# Configure the Pi to use the BCM (Broadcom) pin names, rather than the pin positions
GPIO.setmode(GPIO.BCM)

red_pin = 18

GPIO.setup(red_pin, GPIO.OUT)

class TweetListener(StreamListener):

    def on_status(self, status):
        print("Tweet: {}".format(status.text))
        try:
            GPIO.output(red_pin, True)  # LED on
            time.sleep(0.5)             # delay 0.5 seconds
            GPIO.output(red_pin, False) # LED off
            time.sleep(0.5)             # delay 0.5 seconds
        finally:
            print("Cleaning up")
            GPIO.cleanup()
            # And anything else we want to do AKA make light blink or whatever