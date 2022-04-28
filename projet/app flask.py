from flask import Flask, jsonify, request, render_template
from container import Container

app = Flask(__name__)
container = Container()
anna = container.anna()

@app.route('/salut')
def hello():
    result = anna.search('a')
    return jsonify(result)

@app.route('/search', methods=['POST'])
def search():
    data = request.json
    result = anna.search(data['searchText'])
    return jsonify(result)

@app.route('/')
def index():
    return render_template('index.html')