from flask import Flask, jsonify, request
from container import Container

app = Flask(__name__)
container = Container()
controller = container.controller()

@app.route('/salut')
def hello():
    result = controller.search('a')
    return jsonify(result)

@app.route('/search', methods=['POST'])
def search():
    data = request.json
    result = controller.search(data['recherche'])
    return jsonify(result)