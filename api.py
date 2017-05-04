from flask import Flask, request
from flask_restful import Resource, Api

import click

#pyserial
import serial
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
    Classe responsavel, por retornar as portas seriais, conectadas no dispositivo.
"""
class serialDevices(Resource):
    def get(self,nome=None):
        print (nome)
        #Quando não for passado o nome, retorna todas as portas disponiveis
        if not nome:
            '''
                Retorno da lista: ('dispositivo','nome','descricao')
            '''
            devices = serial.tools.list_ports.comports()
        
        res = {'devices': devices}
        #return json.dumps(res) para retornar em string
        return res



api.add_resource(SimpleRest, '/<string:todo_id>')
api.add_resource(serialDevices, '/serialDevices','/serialDevices/<string:nome>')

if __name__ == '__main__':
    startup()
