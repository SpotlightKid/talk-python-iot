import pyb

def buzz(pin, freq=400, dur=1.0):
    pin = pyb.Pin(pin, pyb.Pin.OUT)
    duty = int(1000.0 / freq / 2.0)

    for i in range(int(dur * freq)):
        pin.high()
        pyb.delay(duty)
        pin.low()
        pyb.delay(duty)
