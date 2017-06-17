from flask import Flask, request, abort, g
from flask_restful import Resource, Api


import click

import serial.tools.list_ports

from threading import RLock, Thread
import xbee
import serial
import sqlite3
# import json

class act():
	lock = RLock()

	"""
	connection to actors
	"""
	commands = {
		'P0':b'P0',
		'AT':b'AT',
		'NT':b'NT',
		'ATND':b'ATND'
	}

	parameters={
		'ON':b'\x05',
		'OFF':b'\x04'
	}
	
	network={}
	#ser = serial.Serial('/dev/ttyUSB0', 9600)
	try:
		bee = xbee.ZigBee(serial.Serial('/dev/ttyUSB0', 9600))
		#network = 		
		
	except:
		print("Falha na conecao com controlador")
		pass
	
	#def __innit__(self):
	#	act.bee.
	#COMMAND : sensor

	def add(code, info):
		info=info.split(' ')
		name = code
		addr = info[1]
		return {name:addr}
	
	def find(code=None):
		if code in act.network:
			act.bee.send('at', b'AT')
		#while True: 

	"""
	def find(code=None):
		#print("inside act pip")
		if not code:
			# Returns list in format: ('device', 'name', description).
			print("inside not code")
			devices = serial.tools.list_ports.comports()
		else:
			print('inside else')
			try:
			   devices = next(serial.tools.list_ports.grep(code))
			except:
				# When you can not find devices
				abort(404)
		if len(devices) == 0:
			# When you can not find devices
			abort(404)
		else:
			res = {'devices': devices}
		# Use return json.dumps(res) to return in string
		return res
	"""
	def get(code=None):
		
		return "Result"


	def do(code, cmd):
		args = cmd.split(' ')
		args.pop(0)
		print(args)
		cmd = args.pop(0)
		if args.__len__() is 1 :
			act.bee.send(('at', command=act.commands.get(cmd), parameter=act.parameters.get(args.pop(0))))
		else:
			print('PRINT ' + cmd)
			print(act.bee.send('at',command=act.commands.get(cmd)))
			#print(act.bee.send('at',command=act.commands.get(cmd), parameter=act.parameters.get(args.pop(0)), addr_long=act.parameters.get(args.pop(0))))
			#print(act.bee.send('at',command=act.commands.get(cmd), parameter=act.parameters.get(args.pop(0)), addr_long=act.  code  ))
		

DATABASE = 'database.sqlite'

def get_db():
	db = getattr(g, '_database', None)
	if db is None:
		db = g._database = sqlite3.connect(DATABASE)
	return db


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


class SimpleRest(Resource):
	def get(self, sensor_id):
		return {sensor_id: sensors[sensors_id]}

	def put(self, sensor_id):
		sensors[sensor_id] = request.form['data']
		return {sensor_id: sensors[sensor_id]}


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
	
	def put(self, code):
		comm = request.form['data']
		print(type(comm))
		print("Executing " + comm + "in" + code) 
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
api.add_resource(serialDevices,'/serialDevices','/serialDevices/<string:code>')

if __name__ == '__main__':
	startup()
