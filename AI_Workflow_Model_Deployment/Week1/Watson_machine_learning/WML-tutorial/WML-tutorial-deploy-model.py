#!/usr/bin/env python

"""
Watson machine learning tutorial

NOTE: this script requires scikit-learn==0.20.3

"""


import os
import json
import pandas as pd
import numpy as np

from ibm_watson_machine_learning import APIClient
from sklearn.pipeline import Pipeline
from sklearn import ensemble
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.metrics import classification_report


## check for correct version of sklearn
SKLEARN_VERSION = "0.23"

## ID of the deployment space. (# change by the ID of your deployment space)
DEPLOYMENT_SPACE_ID = "385d623c-f899-4e5e-a0e5-4c6e0cea8f16"

from sklearn import __version__
if __version__[:4] != SKLEARN_VERSION:
    raise Exception("sklearn version must be {}".format(SKLEARN_VERSION))

def load_wml_credentials():
    """
    fetch the saved watson machine learning credentials
    """

    wmlcreds_dir = "."
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

def get_preprocessor():
    """
    create a preprocessor for the pipeline
    """
    
    ## preprocessing pipeline
    numeric_features = ['age', 'num_streams']
    numeric_transformer = Pipeline(steps=[('imputer', SimpleImputer(strategy='mean')),
                                          ('scaler', StandardScaler())])

    categorical_features = ['country', 'subscriber_type']
    categorical_transformer = Pipeline(steps=[('imputer', SimpleImputer(strategy='constant', fill_value='missing')),
                                              ('onehot', OneHotEncoder(handle_unknown='ignore'))])

    preprocessor = ColumnTransformer(transformers=[('num', numeric_transformer, numeric_features),
                                                   ('cat', categorical_transformer, categorical_features)])
    return(preprocessor)


def load_aavail_data():
    data_dir = os.path.join(".", "data")
    df = pd.read_csv(os.path.join(data_dir, r"aavail-target.csv"))
       
    ## pull out the target and remove uneeded columns
    _y = df.pop('is_subscriber')
    y = np.zeros(_y.size)
    y[_y==0] = 1 
    df.drop(columns=['customer_id', 'customer_name'], inplace=True)
    df.head()
    X = df

    return(X, y)

# def clear_deployment_space():


if __name__ == "__main__":


    ## connect to the wml service with saved credentials
    print("...Connecting to WML Client")
    client = connect_wml_service()
    # Set the default space of your client to your deployment space
    client.set.default_space(DEPLOYMENT_SPACE_ID)
    

    ## prepare the data
    print("...Preparing the data")
    X, y = load_aavail_data()
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)

    ## prepare the model

    params = {'n_estimators':100, 'max_depth':2}   
    clf = ensemble.RandomForestClassifier(**params)
    preprocessor = get_preprocessor()
    pipe = Pipeline(steps=[('pre', preprocessor),
                           ('clf', clf)])

    print("...Training the model")
    ## train the model
    pipe.fit(X_train, y_train)
    y_pred = pipe.predict(X_test)
    print(classification_report(y_test,y_pred))

    # save the model in the WML service
    print("... Saving the mode to WML service")
    software_spec_uid = client.software_specifications.get_uid_by_name("scikit-learn_0.22-py3.6")
    metadata_model = {
           client.repository.ModelMetaNames.NAME: 'model_WML_tuto',
           client.repository.ModelMetaNames.TYPE: 'scikit-learn_0.22',
           client.repository.ModelMetaNames.SOFTWARE_SPEC_UID: software_spec_uid
    }
    model_details = client.repository.store_model(pipe, meta_props=metadata_model)
    model_uid = client.repository.get_model_uid(model_details)
    print("model saved successfully")
    print("model uid : {}".format(model_uid))


    ## deploy model in the WML service
    print("...Deploying the model in the WML service")
    metadata_deployment = {
    client.deployments.ConfigurationMetaNames.NAME: "model_WML_tuto_deployment",
    client.deployments.ConfigurationMetaNames.ONLINE: {}
    }
    deployment_details = client.deployments.create(model_uid, meta_props=metadata_deployment)
    print("model deployed successfully")

    

