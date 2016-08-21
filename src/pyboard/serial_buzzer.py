import pyb
import struct

from buzzer import buzz

COMMANDS = (83, 88, 89)  # 'S', 'X', 'Y'

def main():
    serial = pyb.USB_VCP()
    serial.setinterrupt(-1)
    led1 = pyb.LED(1)
    led2 = pyb.LED(2)
    data = bytearray(3)

    while True:
        if serial.any():
            serial.readinto(data, 3)
            cmd, val = data[0], data[1:]

            if cmd in COMMANDS:
                val = struct.unpack('>H', val)[0]

                if cmd == 83 and val:  # switch
                    buzz('Y1', 400)
                elif cmd == 88:
                    if val >= 900:
                        led1.on()
                    elif val <= 200:
                        led2.on()
                    else:
                        led1.off()
                        led2.off()
                elif cmd == 89:
                    pass  # handle Y-axis change here

        pyb.delay(50)
