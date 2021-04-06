from flask import Flask, render_template, request, jsonify
from flask_restful import Api, Resource, reqparse
from werkzeug.datastructures import Headers
#import datasets
#import pandas as pd
#from fastai.text.all import *
#from transformers import *

#from blurr.data.all import *
#from blurr.modeling.all import *
app = Flask(__name__)


@app.route('/')
def index():
	return render_template('index.html')

@app.route('/summary', methods=['POST'])
def summary():
	document = request.form['paper'] # "document variable" is the text
	# inf_learn = load_learner(fname='C:/Users/admin/Downloads/ft_cnndm_export.pkl')
	# result = inf_learn.blurr_generate(document)[0] # "result" will contain summary
	return {'summary' : document} # uncomment the above two lines and replace "document" with "result"

if __name__ == "__main__":
	app.run(debug = True)