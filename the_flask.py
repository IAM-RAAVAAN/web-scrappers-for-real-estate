from flask import Flask,jsonify
from flask_restful import Api,Resource
app = Flask(__name__)
api = Api(app)
import time

class HelloWorld(Resource):
    def get(self):
        return jsonify({'about':'in the HelloWorld'})
    def post(self):
        return jsonify({'about':time.gmtime()})


@app.route('/')
def index():
    return jsonify({'about':'hello flask'})

api.add_resource(HelloWorld,"/HelloWorld")

@app.route('/multi/<int:n>')
def multi(n):
    result={
        'number':n,
        'output':n*10,
        'backend':'flask',
        'status':'good',
        'message':'keep running',
        'time': time.time()
    }
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
    