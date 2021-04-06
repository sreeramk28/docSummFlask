import json
from flask import Flask, request, jsonify
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)

@app.route('/summary', methods=['POST'])
def post():
    #response = flask.Response()
    #response.headers["Access-Control-Allow-Origin"] = "*"
    #response.headers[""]
    record = json.loads(request.data)
    
    return {"summary":record['paper']}, 200, [{"Access-Control-Allow-Origin" : "*"}, {"Access-Control-Allow-Credentials" : True}]

if __name__ == "__main__":
	app.run(debug = True)