#!/usr/bin/env python
"""
model tests
"""


import unittest
## import model specific functions and variables
from model import *

class ModelTest(unittest.TestCase):
    """
    test the essential functionality
    """
        
    def test_01_train(self):
        """
        test the train functionality
        """

        ## train the model
        model_train()
        self.assertTrue(os.path.exists(SAVED_MODEL))

    def test_02_load(self):
        """
        test the train functionality
        """
                        
        ## load the model
        model = model_load()
        self.assertTrue('predict' in dir(model))
        self.assertTrue('fit' in dir(model))

    def test_03_predict(self):
        """
        test the predict functionality
        """

        ## load model first
        model = model_load()
        
        ## example predict
        for query in [{'lenght':[6.1],'width':[2.8]}, {'lenght':[7.7],'width':[2.5]}, {'lenght':[5.8],'width':[3.8]}]:
            result = model_predict(query,model)
            y_pred = result['y_pred']
            self.assertTrue(y_pred in [0,1,2])

        
### Run the tests
if __name__ == '__main__':
    unittest.main()
