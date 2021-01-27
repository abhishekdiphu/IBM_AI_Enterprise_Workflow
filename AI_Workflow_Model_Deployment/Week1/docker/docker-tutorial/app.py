
from flask import Flask, jsonify, request
import joblib
import socket
import json
import pandas as pd
import os

MODEL_DIR = "models"
DATA_DIR = "data"

app = Flask(__name__)

@app.route("/")
def hello():
    html = "<h3>Hello {name}!</h3>" \
           "<b>Hostname:</b> {hostname}<br/>"
    return html.format(name=os.getenv("NAME", "world"), hostname=socket.gethostname())

@app.route('/predict', methods=['GET','POST'])
def predict():
    
    ## input checking
    if not request.json:
        print("ERROR: API (predict): did not receive request data")
        return jsonify([])

    query = request.json
    query = pd.DataFrame(query)
    
    if len(query.shape) == 1:
         query = query.reshape(1, -1)

    y_pred = model.predict(query)
    
    return(jsonify(y_pred.tolist()))        
            
if __name__ == '__main__':
    saved_model = 'aavail-rf.joblib'
    model = joblib.load(os.path.join(MODEL_DIR, saved_model))
    app.run(host='0.0.0.0', port=8080,debug=True)
