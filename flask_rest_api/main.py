import json
from flask import Flask, jsonify, request

app = Flask(__name__)
data = [{'id': 0, 'name': 'Alex', 'surname': 'Turner'},
        {'id': 1, 'name': 'Thom', 'surname': 'Yorke'}]


@app.route('/users', methods=['GET'])
def get():
    return jsonify(data)


@app.route('/users', methods=['POST'])
def add():
    data.append(request.get_json())
    return jsonify(data)


@app.route('/users', methods=['DELETE'])
def delete():
    data.pop(request.get_json()['id'])
    return jsonify(data)


@app.route('/users', methods=['PUT'])
def update():
    data[request.get_json()['id']] = request.get_json()
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)