from flask import Flask, request, abort
from flask_restful import Resource, Api

import click

#pyserial
import serial.tools.list_ports

import json

app = Flask(__name__)
api = Api(app)

todos = {}


@click.command()
@click.option('-p', default=5000, help='Port Number')
def startup(p):
    """

    :param p:
    :return:
    """
    app.run(host='0.0.0.0', port=p, debug=True)


class SimpleRest(Resource):
    def get(self, todo_id):
        return {todo_id: todos[todo_id]}

    def put(self, todo_id):
        todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}
"""
    Class that returns the ports connected to the device.
"""
class serialDevices(Resource):
    def get(self,nome=None):
        #When the name is not passed in the url, it returns all the available ports.
        if not nome:
            '''
                Returns list in format: ('device', 'name', description).
            '''
            devices = serial.tools.list_ports.comports()
        else:
            try:
                devices = next(serial.tools.list_ports.grep(nome))
            except:
                #When you can not find devices
                abort(404)
        if len(devices)== 0:
            #When you can not find devices
            abort(404)
        else:
            res = {'devices': devices}
        #Use return json.dumps(res) to return in string
        return res



api.add_resource(SimpleRest, '/<string:todo_id>')
api.add_resource(serialDevices, '/serialDevices','/serialDevices/<string:nome>')

if __name__ == '__main__':
    startup()
