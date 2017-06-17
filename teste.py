#!/home/pi/Documents/HermesProj/venv/bin/python3
import serial
from xbee import XBee, ZigBee

ADDR = b'\x00\x13\xA2\x00\x40\x8C\x70\x27'

def cb(arg):
	print(arg)

serial_port = serial.Serial('/dev/ttyUSB0', 9600)
xbee = ZigBee(serial_port)

while True:
    try:
        print(xbee.wait_read_frame())
    except KeyboardInterrupt:
        break

serial_port.close()