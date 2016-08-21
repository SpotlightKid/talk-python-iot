from machine import Pin
from time import sleep_ms

LED = 2
FREQ = 5  # Hertz

def blink(pin, freq):
    ms = int(1000/freq/2)
    while True:
        pin.high()
        sleep_ms(ms)
        pin.low()
        sleep_ms(ms)

if __name__ == '__main__':
    pin = Pin(LED, Pin.OUT)
    blink(pin, FREQ)
