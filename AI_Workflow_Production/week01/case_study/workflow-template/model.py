import time,os,re,csv,sys,uuid,joblib
from datetime import date
import numpy as np
import pandas as pd
from sklearn import svm
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

from logger import update_predict_log, update_train_log

## model specific variables (iterate the version and note with each change)
if not os.path.exists(os.path.join(".", "models")):
    os.mkdir("models") 

MODEL_VERSION = 0.1
MODEL_VERSION_NOTE = "example random forest on toy data"
SAVED_MODEL = os.path.join("models", "model-{}.joblib".format(re.sub("\.","_", str(MODEL_VERSION))))


def fetch_data():
    """
    example function to fetch data for training
    """
    
    ## import some data to play with
    iris = datasets.load_iris()
    X = iris.data[:,:2]
    y = iris.target

    return(X, y)
    
def model_train():
    """
    example funtion to train model
    """

    ## start timer for runtime
    time_start = time.time()

    ## data ingestion
    X, y = fetch_data()

    ## Perform a train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

    ## Specify parameters and model
    params = {'C':1.0, 'kernel':'linear', 'gamma':0.5}
    clf = svm.SVC(**params, probability=True)

    ## fit model on training data
    clf = clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    eval_test = classification_report(y_test, y_pred, output_dict=True)

    ## retrain using all data
    clf.fit(X, y)
    print("... saving model: {}".format(SAVED_MODEL))
    joblib.dump(clf, SAVED_MODEL)


    m, s = divmod(time.time()-time_start, 60)
    h, m = divmod(m, 60)
    runtime = "%03d:%02d:%02d"%(h, m, s)

    update_train_log(X.shape, eval_test, runtime,
                     MODEL_VERSION, MODEL_VERSION_NOTE, test=False)



def model_predict(query, model=None):
    """
    example funtion to predict from model
    """

    ## start timer for runtime
    time_start = time.time()

    ## input checks
    if isinstance(query, dict):
        query = pd.DataFrame(query)
    elif isinstance(query, pd.DataFrame):
        pass
    else:
        raise Exception("ERROR (model_predict) - invalid input. {} was given".format(type(query)))

    ## load model if needed
    if not model:
        model = model_load()
    
    ## output checking
    if len(query.shape) == 1:
        query = query.reshape(1, -1)

    
    
    ## make prediction and gather data for log entry
    y_pred = model.predict(query)
    y_proba = model.predict_proba(query)

    m, s = divmod(time.time()-time_start, 60)
    h, m = divmod(m, 60)
    runtime = "%03d:%02d:%02d"%(h, m, s)

    for i in range(query.shape[0]):
        update_predict_log(y_pred[i], y_proba, query.iloc[i].values.tolist(), 
                           runtime, MODEL_VERSION, test=False)



        
    return({'y_pred':y_pred, 'y_proba':y_proba})



def model_load():
    """
    example funtion to load model
    """
    if not os.path.exists(SAVED_MODEL):
        raise Exception("Model '{}' cannot be found did you train the model?".format(SAVED_MODEL))
    
    model = joblib.load(SAVED_MODEL)

    return(model)


if __name__ == "__main__":

    """
    basic test procedure for model.py
    """
    
    ## train the model
    model_train()

    ## load the model
    model = model_load()
    
    ## example predict
    for query in [np.array([[6.1, 2.8]]), np.array([[7.7, 2.5]]), np.array([[5.8, 3.8]])]:
        result = model_predict(query, model)
        y_pred = result['y_pred']
        print("predicted: {}".format(y_pred))



