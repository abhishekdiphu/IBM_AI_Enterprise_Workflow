# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 01:07:42 2021

@author: abhishek buragohaibn
"""



import unittest

## import model specific functions and variables
from solution_guidance.model import *

class ModelTest(unittest.TestCase):
    """
    test the essential functionality
    """
        
    def test_01_train(self):
        """
        test the train functionality
        """

        ## train the model
        model_train(os.path.join("cs-train"),test=True)
        saved_model = os.path.join("solution_guidance/models","sl-netherlands-0_1.joblib")
        self.assertTrue(os.path.exists(saved_model))

    def test_02_load(self):
        """
        test the train functionality
        """
                        
        ## train the model
        data_dir = os.path.join("cs-train")
        all_data, all_models = model_load(data_dir = data_dir)
        model = all_models['netherlands']
        
        self.assertTrue('predict' in dir(model))
        self.assertTrue('fit' in dir(model))

       
    def test_03_predict(self):
        """
        test the predict function input
        """
        data_dir = os.path.join("cs-train")
        ## ensure that a list can be passed        
        result = model_predict('netherlands','2018','08','01',test=True,  data_dir = data_dir)
        y_pred = result['y_pred']
        self.assertTrue(y_pred >= 0.0)

          
### Run the tests
if __name__ == '__main__':
    unittest.main()