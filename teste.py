#!/home/samuel/Documentos/HermesProj/venv/bin/python3
import serial
from xbee import XBee, ZigBee

ADDR = b'\x00\x13\xA2\x00\x40\x8C\x70\x27'

def cb(arg):
	print(arg)

serial_port = serial.Serial('/dev/ttyUSB2', 9600)
xbee = ZigBee(serial_port)

xbee.send('at', command=b'VR')
print(serial_port.readline());
