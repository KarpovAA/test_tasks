import random
import flask
from flask import request, jsonify


app = flask.Flask(__name__)
# app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
@app.route('/api', methods=['GET'])
def home():
    if request.args and request.args['a'] and request.args['b']:
        return jsonify([random.randint(-100, 100) for i in range(random.randint(1, 100))])

    return "<h1>No args</h1>"


app.run()
