from tweepy import StreamListener

import RPi.GPIO as GPIO
import time

# Configure the Pi to use the BCM (Broadcom) pin names, rather than the pin positions
GPIO.setmode(GPIO.BCM)

red_pin = 27
blue_pin = 18
green_pin = 17

GPIO.setup(red_pin, GPIO.OUT)

class TweetListener(StreamListener):

    def on_status(self, status):
        print("Tweet: {}".format(status.text))
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(red_pin, GPIO.OUT)
        GPIO.setup(green_pin, GPIO.OUT)
        GPIO.setup(blue_pin, GPIO.OUT)
        try:
                if "#yolo" in status.text:
                    pin = red_pin
                elif "#blessed" in status.text:
                    pin = blue_pin
                else:
                    pin = green_pin

                GPIO.output(pin, True)  # LED on
                time.sleep(0.5)             # delay 0.5 seconds
                GPIO.output(pin, False) # LED off
        finally:
                print("Cleaning up")
                GPIO.cleanup()
                # And anything else we want to do AKA make light blink or whatever