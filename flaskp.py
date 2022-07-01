from flask import Flask, jsonify, request
from collections import OrderedDict

app = Flask(__name__)

@app.route('/data/<_name>', methods = ['POST'])
def json_data(_name):
    _id = request.args.get('id')
    _pass = request.args.get('pass')
    return jsonify(OrderedDict({'name':_name, 'id':_id, 'pass':_pass}))


if __name__ == '__main__':
    app.run()