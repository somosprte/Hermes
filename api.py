from flask import Flask, request
from flask_restful import Resource, Api

import click

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

api.add_resource(SimpleRest, '/<string:todo_id>')

if __name__ == '__main__':
    startup()
