from flask import Flask, Blueprint
from flask_restful import Resource, Api
import os
import json
import flask

# Python files on which API would be created
from contactParse import contactInfo
from main import create_folder
import Constants

app = Flask(__name__)
api_bp = Blueprint('api', __name__)
api = Api(api_bp)


class ParseFile(object):
    #@app.route('/parse')
    def parsefile(self):
        path = #get file path
        try:
            for fname in os.listdir(path):
                filename = os.path.join(path, fname)
                break
        except StopIteration:
            print "No more files"
        self.obj = create_folder(fname)
        if self.obj:

            return self.obj
        else:
            return "Failed"

    #@app.route('/parseInfo')
    def test(self):
        folder_name = os.path.join(Constants.preprocessPath, self.obj)

        objc = Info()
        result = objc.parsecontact(folder_name)
        show= json.dumps(result,indent=2)
        parsedData = flask.Response(response=show, status=200, mimetype='application/json')
        return parsedData


    def __init__(self):
        self.obj = ""

class TodoItem(Resource):
    def get(self):
        return {'task': 'Say "Hello, World!"'}

api.add_resource(TodoItem, '/todos')
app.register_blueprint(api_bp)

pf = ParseFile()

# Default
@app.route('/')
def index():
    return 'Server has started'

# call API named "parse"
@app.route('/parse')
def parse():
    return pf.parsefile()

# Call to API named "parseInfo"
@app.route('/parseInfo')
def coninfo():
    return pf.test()

if __name__ == '__main__':

    #app.run(threaded=True)
    app.run(threaded = True)

