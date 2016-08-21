from time import sleep_ms
from machine import ADC, Pin
from umqtt_simple import MQTTClient


def main():
    """Read Joystick X-Axis and switch and publish it to MQTT."""
    mqtt = MQTTClient('esp8266', '192.168.4.2')
    adc = ADC(0)
    switch = Pin(0, Pin.IN, None)

    mqtt.connect()
    old_val = {'adc': 0, 'switch': 0}

    while True:
        value = adc.read()

        if value != old_val['adc']:
            mqtt.publish(b'joystick/x-axis', b'%i' % value)
            old_val['adc'] = value

        value = 0 if switch.value() else 1
        if value != old_val['switch']:
            mqtt.publish(b'joystick/switch', b'%i' % value)
            old_val['switch'] = value

        sleep_ms(200)
