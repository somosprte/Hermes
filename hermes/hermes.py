from flask import Flask, request, abort, g
from flask_restful import Resource, Api


import click

import serial.tools.list_ports

from threading import Lock, Thread
import xbee
import serial
from datetime import datetime
import sqlite3
# import json

class act():


	"""
	lock = Lock()
	lock.acquire()
	lock.release()

	"""
	adr={
		'SAMUEL':b'\x00\x13\xA2\x00\x40\x8C\x70\x27',
		'RIVA':b'\x00\x13\xA2\x00\x40\x8C\x70\x1E'
	}
	commands = {
		'COM':b'P0',
		'LED2':b'P2', #LED 2
		'LEDA':b'D5', #LED ASSOC AZUL 
		'LED4':b'D7', #LED LED 4
		'LED7':b'P1' #LED 7
	}

	parameters={
		'ON':b'\x05',
		'OFF':b'\x04'
	}
	
	try:
		bee = xbee.ZigBee(serial.Serial('/dev/ttyUSB0', 9600))
	except:
		print("Falha na conecao com controlador")
		exit
	def bdrecord(datanow, cmd, val, code):
		database = 'database.sqlite'
		con=sqlite3.connect(database)
		cur = con.cursor()	
		cur.execute("INSERT INTO Actions VALUES (?,?,?,?)", (datanow, cmd, val, code))
		con.close()
	def add(code, info):
		info=info.split(' ')
		name = code
		addr = info[1]
		return {name:addr}
	
	def find(code=None):
		if code in act.network:
			act.bee.send('at', b'AT')
		#while True: 

	def return_message(data):
		print(data)

	def get(code=None):
		
		return "Result"
	
	'''
	def parse(**kwargs):
		act.lock.acquire()
		try:
			print(ser = serial.Serial('/dev/ttyUSB0', 9600))
			bee = xbee.ZigBee(ser)	
			act.bee.remote_tr(**kwargs)
			act.bee.wait_read_frame()
			ser.close()
		except:
			print('connection falied')
		finally:
			act.lock.release()  
	'''	

	def do(code, cmd):
		args = cmd.split(' ')
		args.pop(0)
		print(code)
		cmd = args.pop(0)
		val = args.pop(0)
		print(code)
		if code == 'BASE':
			act.bee.remote_at( command=act.commands.get(cmd), parameter=act.parameters.get(val))
			act.bdrecord(datetime.now(), cmd, val, code)
			#act.cur.execute("INSERT INTO Actions VALUES (?,?,?,?)", (datetime.now(), cmd, val, code ))
			return str(datetime.now()) + " "+ cmd + " "  + val + " " + code 
		#if args.__len__() is 1 :
		#	act.parse( **{'command':act.commands.get(cmd), 'parameter':act.parameters.get(val)})
		elif args.__len__() is 0 :
			act.bee.remote_at( command=act.commands.get(cmd), parameter=act.parameters.get(val), dest_addr_long=act.adr.get(code) )
			act.bdrecord(datetime.now(), cmd, val, code)

			return str(datetime.now()) + " "+ cmd + " "  + val + " " + code  
		else:
			return "Command error. Possible combinations: Name, COMMAND, PORT, VALUE, and/or ADDRESS"
		


######################
app = Flask(__name__)
api = Api(app)

todos = {}
sensors = {}

@click.command()
@click.option('-p', default=5000, help='Port Number')
def startup(p):
	"""
	:param p:
	:return:
	"""
	app.run(host='0.0.0.0', port=p, debug=True)


class serialDevices(Resource):
	"""
	Class that returns the ports connected to the device.
	"""
	def get(self, code=None):
		if not act.find(code):
			pass
		else:
		#	while True:
				
			resp = act.get(code)
		return resp 
	
	def post(self, code):
		comm = request.form['data']
		print("Executing " + comm + " in " + code) 
		if comm.startswith("ADD") is True:
			return act.add(code,comm)
		
		if comm.startswith("DO"): 
			return act.do(code, comm)
	
		if not act.find(comm):
			pass
			#return "code not found"
		else:
			resp = act.put({code:comm})
		return resp

#api.add_resource(SimpleRest, '/<string:todo_id>')
api.add_resource(serialDevices,'/hermes','/hermes/<string:code>')

if __name__ == '__main__':
	startup()
