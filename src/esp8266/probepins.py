from machine import Pin
from time import  sleep_ms


def main():
    def probe(ms):
        for i in (0,2,5, 12, 13, 14, 15, 16):
            print("Probing pin %i" % i)
            pin = Pin(i, Pin.OUT)
            pin.low()
            sleep_ms(ms)
            pin.high()
            del pin


#probe(2000)
