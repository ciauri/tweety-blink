from tweepy import StreamListener

import RPi.GPIO as GPIO
import time
import asyncio
from threading import Thread

# Configure the Pi to use the BCM (Broadcom) pin names, rather than the pin positions
GPIO.setmode(GPIO.BCM)

red_pin = 27
blue_pin = 18
green_pin = 17

GPIO.setup(red_pin, GPIO.OUT)
GPIO.setup(green_pin, GPIO.OUT)
GPIO.setup(blue_pin, GPIO.OUT)


class TweetListener(StreamListener):
    def __init__(self):
        StreamListener.__init__(self)
        self.loop = asyncio.get_event_loop()
        t = Thread(target=self.loop_in_thread, args=(self.loop,))
        t.start()

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("ded")
        self.loop.close()
        GPIO.cleanup()

    def on_status(self, status):
        print("Tweet: {}".format(status.text).encode('ascii','replace'))
        self.loop.run_until_complete(self.blink(status.text.lower()))

    def loop_in_thread(self, loop):
        asyncio.set_event_loop(loop)

    @asyncio.coroutine
    def blink(self, text):
        pins = []
        if "yolo" in text:
            pins.append(red_pin)
            # self.pulse(red_pin)
        elif "blessed" in text:
            # self.pulse(blue_pin)
            pins.append(blue_pin)
        elif "christmakkuh" in text:
            # self.pulse(red_pin)
            pins.append(blue_pin)
            pins.append(red_pin)
        elif "christmas" in text:
            # self.pulse(green_pin)
            pins.append(green_pin)

        self.pulse(pins)

    def pulse(self, leds):
        # Use PWM to fade an LED.

        fades = []

        for led in leds:
            fade = GPIO.PWM(led, 100)
            fade.start(0)
            fades.append(fade)

        # Set up variables for the fading effect.
        value = 0
        increment = 2
        increasing = True
        count = 0

        while count < 1000:

            for fade in fades:
                fade.ChangeDutyCycle(value)

            if increasing:
                value += increment
                time.sleep(0.002)
            else:
                if not value:
                    break
                value -= increment
                time.sleep(0.002)

            if (value >= 100):
                increasing = False

            count += 1