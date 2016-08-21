#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import struct
import sys
import time

from serial import Serial
import paho.mqtt.client as mqtt


log = logging.getLogger('send_serial')



class MyMQTTClient:
    def __init__(self, serial):
        self.serial = serial
        self.client = mqtt.Client('send-serial')
        self.client.on_connect = self.mqtt_connect
        self.client.on_disconnect = self.mqtt_disconnect
        self.client.on_message = self.handle_mqtt

    def loop(self):
        self.client.connect('localhost', 1883)
        log.debug("Starting MQTT thread...")
        self.client.loop_start()

    def mqtt_connect(self, client, userdata, flags, rc):
        log.debug("MQTT connect: %s", mqtt.connack_string(rc))
        if rc == 0:
            client.subscribe([('joystick/#', 0)])

    def mqtt_disconnect(self, client, userdata, rc):
        log.debug("MQTT disconnect: %s", mqtt.error_string(rc))

    def handle_mqtt(self, client, userdata, msg):
        log.debug("MQTT recv: %s %r", msg.topic, msg.payload)
        try:
            val = int(msg.payload)
            if msg.topic == 'joystick/switch':
                self.send(b'S', val)
            elif msg.topic == 'joystick/x-axis':
                self.send(b'X', val)
            elif msg.topic == 'joystick/y-axis':
                self.send(b'Y', val)
        except:
            log.exception("Error handling MQTT message.")

    def send(self, cmd, val):
        self.serial.write(cmd + struct.pack('>H', val))


def main():
    try:
        serial_name = sys.argv[1]
    except:
        serial_name = '/dev/ttyACM0'

    logging.basicConfig(level=logging.DEBUG)
    serial = Serial(serial_name)
    mqttclient = MyMQTTClient(serial)
    mqttclient.loop()

    try:
        log.info("Entering main loop.")
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        log.info("Interrupted.")
    finally:
        serial.close()
        log.info("Done.")


if __name__ == '__main__':
    sys.exit(main())
