import argparse
from flask import Flask, jsonify, request
from flask import render_template, send_from_directory
import joblib
import socket
import json
import numpy as np
import pandas as pd
import os
import re

## import model specific functions and variables
from model import model_train, model_load, model_predict
from model import MODEL_VERSION, MODEL_VERSION_NOTE

app = Flask(__name__)

@app.route("/")
def landing():
    return render_template('index.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/running', methods=['POST'])
def running():
    return render_template('running.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    """
    basic predict function for the API
    """

    ## input checking
    if not request.json:
        print("ERROR: API (predict): did not receive request data")
        return jsonify([])

    if 'query' not in request.json:
        print("ERROR API (predict): received request, but no 'query' found within")
        return jsonify([])

    if 'type' not in request.json:
        print("WARNING API (predict): received request, but no 'type' was found assuming 'numpy'")
        query_type = 'numpy'

    query = request.json['query']
        
    if request.json['type'] == 'dict':
        pass
    else:
        print("ERROR API (predict): only dict data types have been implemented")
        return jsonify([])
        
    ## load model
    model = model_load()
    
    if not model:
        print("ERROR: model is not available")
        return jsonify([])
    

    _result = model_predict(query, model)
    result = {}

    ## convert numpy objects so ensure they are serializable
    for key, item in _result.items():
        if isinstance(item, np.ndarray):
            result[key] = item.tolist()
        else:
            result[key] = item
    return(jsonify(result))


@app.route('/train', methods=['GET', 'POST'])
def train():
    """
    basic predict function for the API
    """

    if not request.json:
        print("ERROR: API (train): did not receive request data")
        return jsonify(False)

    print("... training model")
    model = model_train()
    print("... training complete")

    return(jsonify(True))


@app.route('/logs/<filename>', methods=['GET'])
def logs(filename):
    """
    API endpoint to get logs
    """

    ## YOUR CODE HERE
    ## get the log directory (log_dir) and raise exceptions if you cannot find the log files.
    ## Then return the content of the logs using the flask function send_from-directory()



if __name__ == '__main__':


    ## parse arguments for debug mode
    ap = argparse.ArgumentParser()
    ap.add_argument("-d", "--debug", action="store_true", help="debug flask")
    args = vars(ap.parse_args())

    if args["debug"]:
        app.run(debug=True, port=8080)
    else:
        app.run(host='0.0.0.0', threaded=True ,port=8080)

