from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome To Prime Pay"



@app.route('/hello', methods=['GET'])
def hello():
    return "Hello, World!"


@app.route('/greet/<name>', methods=['GET'])
def greet(name):
    return f"Hello, {name}!"


def data():
    data = request.json
    return jsonify(data), 201


if __name__ == '__main__':
    app.run(debug=True)






