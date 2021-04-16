#!/usr/bin/env python
"""
module with functions to enable logging
"""

import time, os, re, csv, sys, uuid, joblib
from datetime import date

if not os.path.exists(os.path.join(".", "logs")):
    os.mkdir("logs")

def update_train_log(data_shape, eval_test, runtime, MODEL_VERSION, MODEL_VERSION_NOTE, test=False):
    """
    update train log file
    """

    ## name the logfile using something that cycles with date (day, month, year)    
    today = date.today()
    if test:
        logfile = os.path.join("logs", "train-test.log")
    else:
        logfile = os.path.join("logs", "train-{}-{}.log".format(today.year, today.month))

    ## YOUR CODE HERE 
    ## Following the example provided in the Hands on activity of the unit Feedback "loops and unit testing" 
    ## of this course, complete this function to update the train log file at the end of every training.



def update_predict_log(y_pred, y_proba, query, runtime, MODEL_VERSION, test=False):
    """
    update predict log file
    """


    today = date.today()
    if test:
        logfile = os.path.join("logs", "predict-test.log")
    else:
        logfile = os.path.join("logs", "predict-{}-{}.log".format(today.year, today.month))

    ## YOUR CODE HERE 
    ## Following the example provided in the Hands on activity of the unit Feedback "loops and unit testing" 
    ## of this course, complete this function to update the predict log file at the end of every prediction.




if __name__ == "__main__":

    """
    basic test procedure for logger.py
    """

    from model import MODEL_VERSION, MODEL_VERSION_NOTE
    
    ## train logger
    update_train_log("(100, 2)", "{'rmse':0.5}", "00:00:01",
                     MODEL_VERSION, MODEL_VERSION_NOTE, test=True)
    ## predict logger
    update_predict_log("[0]", "[0.6, 0.4]", "[5.1, 3.5]",
                       "00:00:01", MODEL_VERSION, test=True)
    
        
