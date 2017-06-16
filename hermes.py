from flask import Flask, request, abort, g
from flask_restful import Resource, Api


import click

import serial.tools.list_ports

import xbee
import serial
import sqlite3
# import json

class act():
	"""
	connection to actors
	"""
	def put(code={None:[None]}):
		print(code)

	def get(code=None):
		if not code:
			# Returns list in format: ('device', 'name', description).
			devices = serial.tools.list_ports.comports()
		else:
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
	def get(self, nome=None):
		resp = act.get(nome)
		return nome

	def put(self, nome):
		sensors[nome] = request.form['data']
		resp = {nome: sensors[nome]}
		act.put(resp)
		return resp

#api.add_resource(SimpleRest, '/<string:todo_id>')
api.add_resource(serialDevices,'/serialDevices','/serialDevices/<string:nome>')

if __name__ == '__main__':
	startup()
