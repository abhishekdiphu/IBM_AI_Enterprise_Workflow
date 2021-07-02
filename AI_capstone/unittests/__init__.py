# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 01:09:49 2021

@author: abhishek buragohaibn
"""
import unittest
import getopt
import sys
import os

## parse inputs
try:
    optlist, args = getopt.getopt(sys.argv[1:],'v')
except getopt.GetoptError:
    print(getopt.GetoptError)
    print(sys.argv[0] + "-v")
    print("... the verbose flag (-v) may be used")
    sys.exit()

VERBOSE = False
RUNALL = False

sys.path.append(os.path.realpath(os.path.dirname(__file__)))

for o, a in optlist:
    if o == '-v':
        VERBOSE = True


## model tests
from model_test import *

ModelTestSuite = unittest.TestLoader().loadTestsFromTestCase(ModelTest)



MainSuite = unittest.TestSuite([ModelTestSuite])