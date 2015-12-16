from tweepy import StreamListener

import RPi.GPIO as GPIO
import time
# import asyncio
# from threading import Thread





class TweetListener(StreamListener):
    def __init__(self):
        StreamListener.__init__(self)
        self.scores = {}
        # Configure the Pi to use the BCM (Broadcom) pin names, rather than the pin positions
        GPIO.setmode(GPIO.BCM)
        self.red_pin = 27
        self.blue_pin = 18
        self.green_pin = 17
        GPIO.setup(self.red_pin, GPIO.OUT)
        GPIO.setup(self.green_pin, GPIO.OUT)
        GPIO.setup(self.blue_pin, GPIO.OUT)
        # self.loop = asyncio.get_event_loop()
        # t = Thread(target=self.loop_in_thread, args=(self.loop,))
        # t.start()

    def __exit__(self, exc_type, exc_val, exc_tb):
        # self.loop.close()
        self.printScoreboard()
        GPIO.cleanup()

    def on_status(self, status):
        print("Tweet: {}".format(status.text).encode('utf-8','replace'))
        self.lights(status.text.lower())
        return True
        # self.loop.run_until_complete(self.blink(status.text.lower()))

    def on_error(self, status_code):
        print("sheeeit")

    # def loop_in_thread(self, loop):
    #     asyncio.set_event_loop(loop)

    # @asyncio.coroutine
    def lights(self, text):
        pins = []
        if "yolo" in text: # Red
            pins.append(self.red_pin)
            self.scores['yolo'] = self.scores.get('yolo', 0) + 1
        elif "blessed" in text: # Blue
            pins.append(self.blue_pin)
            self.scores['blessed'] = self.scores.get('blessed', 0) + 1
        elif "christmakkuh" in text: # Purple
            pins.append(self.blue_pin)
            pins.append(self.red_pin)
            self.scores['christmakkuh'] = self.scores.get('christmakkuh', 0) + 1
        elif "christmas" in text: # Green
            pins.append(self.green_pin)
            self.scores['christmas'] = self.scores.get('christmas', 0) + 1
        else:
            print("should not reach this")

        if len(pins):
            self.blink(pins)
            # self.pulse(pins)

    def blink(self, leds):
        for led in leds:
            GPIO.output(led, True)  # LED on

        time.sleep(0.1)

        for led in leds:
            GPIO.output(led, False)

    # BUG: Error in `python3': double free or corruption (fasttop):
    # Has issues. Will cause errorless crash when sleeping.
    def pulse(self, leds):
        # Use PWM to fade an LED.

        fades = []

        for led in leds:
            fade = GPIO.PWM(led, 100)
            fade.start(0)
            fades.append(fade)

        # Set up variables for the fading effect.
        value = 100
        increment = 1

        while value:
            for fade in fades:
                fade.ChangeDutyCycle(value)

            print(value)
            value -= increment
            time.sleep(0.002)

        for fade in fades:
            fade.stop()



    def printScoreboard(self):
        print("***** SCOREBOARD *****")
        for team, score in self.scores.items():
            print("{}: \t\t{}".format(team,score))