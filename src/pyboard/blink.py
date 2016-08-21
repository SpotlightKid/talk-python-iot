# main.py

import pyb


def blink(n=1):
    led = pyb.LED(n)

    while True:
        led.on()
        pyb.delay(300)
        led.off()
        pyb.delay(300)
