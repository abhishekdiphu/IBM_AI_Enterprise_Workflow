#!/usr/bin/env python

"""
Watson machine learning tutorial

NOTE: this script requires scikit-learn==0.20.3

"""


import os
import sys
import json
import pickle
import pandas as pd
import numpy as np

from ibm_watson_machine_learning import APIClient
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split


## check for correct version of sklearn
SKLEARN_VERSION = "0.23"

## ID of the deployment space. (# change by the ID of your deployment space)
DEPLOYMENT_SPACE_ID = "385d623c-f899-4e5e-a0e5-4c6e0cea8f16"
## ID of the deployement
DEPLOYMENT_ID = "YOUR DEPLOYMENT UID"
## ID of the deployed model
MOLDE_UID = "YOUR MODEL UID"

from sklearn import __version__
if __version__[:4] != SKLEARN_VERSION:
    raise Exception("sklearn version must be {}".format(SKLEARN_VERSION))

def load_wml_credentials():
    """
    fetch the saved watson machine learning credentials
    """

    wmlcreds_dir = ""
    wmlcreds_file = os.path.join(wmlcreds_dir,'wml.json')

    if not os.path.exists(wmlcreds_file):
        raise Exception("cannot find {}".format(wmlcreds_file))
    
    with open(wmlcreds_file, "r") as read_file:
        wmlcreds = json.load(read_file)

    return(wmlcreds)
        
def connect_wml_service():
    """
    Instantiate a client using credentials
    """

    wmlcreds = load_wml_credentials()
    wml_credentials = {
        "apikey": wmlcreds['apikey'],
        "url": wmlcreds['url']
    }

    client = APIClient(wml_credentials)
    return(client)

def load_aavail_data():
    data_dir = os.path.join(".", "data")
    df = pd.read_csv(os.path.join(data_dir, r"aavail-target.csv"))
       
    ## pull out the target and remove uneeded columns
    _y = df['is_subscriber']
    y = np.zeros(_y.size)
    y[_y==0] = 1 
    X = df.drop(columns=['customer_id', 'customer_name', 'is_subscriber'])
    return(X, y)

if __name__ == "__main__":


    ## connect to the wml service with saved credentials
    print("...Connecting to WML client")
    client = connect_wml_service()
    # Set the default space of your client to your deployment space
    client.set.default_space(DEPLOYMENT_SPACE_ID)
    instance_details = client.service_instance.get_details()
    print("connected")

    print("...Preparing input data")
    ## prepare the data
    X, y = load_aavail_data()
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)

    print("list models :")
    client.repository.list()
    print("list deployments :")
    client.deployments.list()
    
    ## use your model uid to get the model details
    print("...Getting model from WML")
    model_uid = MOLDE_UID
    model_details = client.repository.get_model_details(model_uid)

    deployment_uid = DEPLOYMENT_ID
    deployment_details = client.deployments.get_details(deployment_uid)
    deployment_id = deployment_details['metadata']['id']

    print("...Testing model")
    ## test model
    payload = {client.deployments.ScoringMetaNames.INPUT_DATA:
           [
               {'fields': X_test.columns.tolist(), 
                'values': X_test.values.tolist()}
           ]
          }
    prediction = client.deployments.score(deployment_id, payload)
    #print(json.dumps(prediction, indent=4, sort_keys=True))

    print("Prediction received from the EndPoint")

