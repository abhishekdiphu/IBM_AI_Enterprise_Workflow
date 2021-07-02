import time
import os
import re 
import csv
import sys
import uuid 
import joblib
from datetime import date
from collections import defaultdict
import numpy as np
import pandas as pd
from sklearn import svm
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.neural_network import MLPRegressor 
from sklearn.ensemble import AdaBoostRegressor
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.pipeline import Pipeline

from solution_guidance.logger import update_predict_log, update_train_log
from solution_guidance.cslib import fetch_ts, engineer_features
import wandb

## model specific variables (iterate the version and note with each change)
MODEL_DIR = "solution_guidance/models"
MODEL_VERSION = 0.1
MODEL_VERSION_NOTE = "supervised learing model for time-series"

#re_log = True
#if re_log :
#    wandb.login()
#idt =  wandb.util.generate_id()

#wandb.init(project="visualize-sklearn",name= "random forest", id = idt )

dashboard = False

def _model_train(df,tag,test=False):
    """
    example funtion to train model
    
    The 'test' flag when set to 'True':
        (1) subsets the data and serializes a test version
        (2) specifies that the use of the 'test' log file 

    """


    ## start timer for runtime
    time_start = time.time()
    #print(str(df))
    X,y,dates = engineer_features(df)

    if test:
        n_samples = int(np.round(0.3 * X.shape[0]))
        subset_indices = np.random.choice(np.arange(X.shape[0]),n_samples,
                                          replace=False).astype(int)
        mask = np.in1d(np.arange(y.size),subset_indices)
        y=y[mask]
        X=X[mask]
        dates=dates[mask]
        
    ## Perform a train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25,
                                                        shuffle=True, random_state=42)
    ## train a random forest model
    rf = True
    gb = False
    ada = False
    mlp = False
    
    
    if mlp :
        param_grid_rf = {
        'rf__criterion': ['mse','mae'],
        'rf__n_estimators': [10,15,20,100],
       
        }
    
    if rf :
        param_grid_rf = {
        'rf__criterion': ['mse','mae'],
        'rf__n_estimators': [10,15,20,30],
       
        }
        
    if gb :
         param_grid_rf = {
        'rf__n_estimators': [50, 60,100],
        'rf__learning_rate' :[0.1,1.0, 0.01],
        'rf__max_depth':[5,3,10],
        }
         
    if ada:
         param_grid_rf = {
        'rf__n_estimators': [10,15,20,100],
        'rf__learning_rate' :[0.1, 1.0],
        }
    if mlp:
         param_grid_rf = {
        'rf__hidden_layer_sizes': [(50,50),100,(60,60)],
        'rf__learning_rate_init' :[0.1, 0.01]
        }
   
    if rf:
        pipe_rf = Pipeline(steps=[('scaler', StandardScaler()),
                                  ('rf', RandomForestRegressor())])
    if gb:
        pipe_rf = Pipeline(steps=[('scaler', StandardScaler()),
                                  ('rf', GradientBoostingRegressor())])
        
    if ada :
        pipe_rf = Pipeline(steps=[('scaler', StandardScaler()),
                                  ('rf', AdaBoostRegressor())])
    if mlp :
        pipe_rf = Pipeline(steps=[('scaler', StandardScaler()),
                                  ('rf', MLPRegressor(activation='relu', 
                                        solver='adam', alpha=0.0001, batch_size='auto', 
                                        learning_rate='constant', 
                                        power_t=0.5, max_iter=200, warm_start=False))])
                                        
        
    grid = GridSearchCV(pipe_rf, param_grid=param_grid_rf, cv=5, n_jobs=-1)
    
    grid.fit(X_train, y_train)
    
    y_pred = grid.predict(X_test)
    
    eval_rmse =  round(np.sqrt(mean_squared_error(y_test,y_pred)))
    
    print("means quared error loss : ", eval_rmse)
    
    ## retrain using all data
    grid.fit(X, y)
    model_name = re.sub("\.","_",str(MODEL_VERSION))
    if dashboard :
            re_log = True
            if re_log :
                wandb.login()
            idt =  wandb.util.generate_id()
            name = "gradient_boosting"+tag
            wandb.init(project="IBM-Project_gradient_boosting",name= name, id = idt )

    if test:
        saved_model = os.path.join(MODEL_DIR,
                                   "test-{}-{}.joblib".format(tag,model_name))
        print("... saving test version of model: {}".format(saved_model))
    else:
        saved_model = os.path.join(MODEL_DIR,
                                   "sl-{}-{}.joblib".format(tag,model_name))
        print("... saving model: {}".format(saved_model))
        
    #wandb.sklearn.plot_regressor(grid, X_train, X_test, y_train, y_test,model_name='RandomForestRegressor')
    # Make individual plots
    
    if dashboard :
            wandb.sklearn.plot_outlier_candidates(grid, X, y)
            
            wandb.sklearn.plot_learning_curve(grid, X, y)
            
            wandb.sklearn.plot_residuals(grid, X, y,)
    joblib.dump(grid,saved_model)

    m, s = divmod(time.time()-time_start, 60)
    h, m = divmod(m, 60)
    runtime = "%03d:%02d:%02d"%(h, m, s)

    ## update log
    update_train_log(tag,(str(dates[0]),str(dates[-1])),{'rmse':eval_rmse},runtime,
                     MODEL_VERSION, MODEL_VERSION_NOTE,test=True)
  







def model_train(data_dir,test=False):
    """
    funtion to train model given a df
    
    'mode' -  can be used to subset data essentially simulating a train
    """
    
    if not os.path.isdir(MODEL_DIR):
        os.mkdir(MODEL_DIR)

    if test:
        print("... test flag on")
        print("...... subseting data")
        print("...... subseting countries")
        
    ## fetch time-series formatted data
    ts_data = fetch_ts(data_dir)

    ## train a different model for each data sets
    for country,df in ts_data.items():
        
        if test and country not in ['all','united_kingdom']:
            continue
        
        _model_train(df,country,test=test)
  
    print("done training model")






def model_load(prefix='sl',data_dir=None,training=True):
    """
    example funtion to load model
    
    The prefix allows the loading of different models
    """

    if not data_dir:
        data_dir = os.path.join("..","cs-train")
    
    models = [f for f in os.listdir(os.path.join("solution_guidance/models")) if re.search("sl",f)]

    if len(models) == 0:
        raise Exception("Models with prefix '{}' cannot be found did you train?".format(prefix))

    all_models = {}
    for model in models:
        all_models[re.split("-",model)[1]] = joblib.load(os.path.join("solution_guidance/models",model))

    ## load data
    print(data_dir)
    ts_data = fetch_ts(data_dir)
    
    all_data = {}
    for country, df in ts_data.items():
        X,y,dates = engineer_features(df,training=training)
        dates = np.array([str(d) for d in dates])
        all_data[country] = {"X":X,"y":y,"dates": dates}
        
    return(all_data, all_models)











def model_predict(country,year,month,day,all_models=None,test=True, data_dir  = None ):
    """
    example funtion to predict from model
    """

    ## start timer for runtime
    time_start = time.time()
    if data_dir :
        data_dir = data_dir 
        
    ## load model if needed
    if not all_models:
       
        all_data,all_models = model_load(data_dir = data_dir , training=False)
    
    ## input checks
    if country not in all_models.keys():
        raise Exception("ERROR (model_predict) - model for country '{}' could not be found".format(country))

    for d in [year,month,day]:
        if re.search("\D",d):
            raise Exception("ERROR (model_predict) - invalid year, month or day")
    
    ## load data
    model = all_models[country]
    data = all_data[country]

    ## check date
    target_date = "{}-{}-{}".format(year,str(month).zfill(2),str(day).zfill(2))
    print(target_date)

    if target_date not in data['dates']:
        raise Exception("ERROR (model_predict) - date {} not in range {}-{}".format(target_date,
                                                                                    data['dates'][0],
                                                                                    data['dates'][-1]))
    date_indx = np.where(data['dates'] == target_date)[0][0]
    query = data['X'].iloc[[date_indx]]
    
    ## sainty check
    if data['dates'].shape[0] != data['X'].shape[0]:
        raise Exception("ERROR (model_predict) - dimensions mismatch")

    ## make prediction and gather data for log entry
    y_pred = model.predict(query)
    y_proba = None
    if 'predict_proba' in dir(model) and 'probability' in dir(model):
        if model.probability == True:
            y_proba = model.predict_proba(query)


    m, s = divmod(time.time()-time_start, 60)
    h, m = divmod(m, 60)
    runtime = "%03d:%02d:%02d"%(h, m, s)

    ## update predict log
    update_predict_log(country,y_pred,y_proba,target_date,
                       runtime, MODEL_VERSION, test=test)
    
    return({'y_pred':y_pred,'y_proba':y_proba})











if __name__ == "__main__":

    """
    basic test procedure for model.py
    """

    ## train the model
    print("TRAINING MODELS")
    data_dir = os.path.join("..","cs-train")
    print(data_dir)
    model_train(data_dir,test=False)

    ## load the model
    print("LOADING MODELS")
    all_data, all_models = model_load(data_dir = data_dir)
    print("... models loaded: ",",".join(all_models.keys()))

    ## test predict
    country='all'
    year='2018'
    month='01'
    day='05'
    result = model_predict(country,year,month,day)
    print(result)
