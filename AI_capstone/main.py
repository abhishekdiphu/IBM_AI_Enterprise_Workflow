# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 15:13:27 2021

@author: abhishek buragohaibn
"""
## import model specific functions and variables

from solution_guidance.model import *

from solution_guidance.logger import * 
from solution_guidance.cslib import *

if __name__ == '__main__':
    

    ## train the model
    print("TRAINING MODELS")
    data_dir = os.path.join("cs-train")
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
    
    
    
    
    
    