from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def fun1():
    if(request.method == 'GET'):
        data = "Hello Hyma"
        return jsonify({'data':data})

@app.route('/n/<int:number>', methods = ['POST'])
def fun2(number):
    return jsonify({'number':number/2})


if __name__ == '__main__':
    app.run()