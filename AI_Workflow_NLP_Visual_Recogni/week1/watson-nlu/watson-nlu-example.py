#!/usr/bin/env python

"""
Example to showcase how to use the Watson NLU service

to store you API key

~$ mkdir ~/.ibm
~$ touch ~/.ibm/ibmauth.py

then edit the file to contain

ibmauth_key = "your api key"

"""



import sys
import os
import json
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_watson.natural_language_understanding_v1 import Features, EntitiesOptions, KeywordsOptions
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

### import API key
apikey_dir = os.path.join(os.path.expanduser("~"),".ibm")
sys.path.append(apikey_dir)

if not os.path.exists(apikey_dir):
    raise Exception("please store you API key in file within 'apikey_dir' before proceeding")

from ibmauth import NLU_KEY, NLU_URL, NLU_VERSION


def connect_watson_nlu():
    """
    establish a connection to watson nlu service
    """
    
    authenticator = IAMAuthenticator(NLU_KEY)
    service = NaturalLanguageUnderstandingV1(version=NLU_VERSION,
                                             authenticator=authenticator)

    service.set_service_url(NLU_URL)

    print("\nConnection established.\n")
    return(service)



if __name__ == "__main__":
    

    service = connect_watson_nlu()

    text = 'NYC is a great city, but the winters are cold.  JFK and Newark are close by so it is easy to get away'
    response = service.analyze(text=text,
                               features=Features(entities=EntitiesOptions(),
                                                 keywords=KeywordsOptions())).get_result()

    

    print(json.dumps(response, indent=2))
    
