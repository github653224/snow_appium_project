# -*- coding:utf-8 -*-
import json, os
from collections import OrderedDict
from datetime import datetime

def getEVENTJsonTemplate(request_type,event_name):
    # Open the JSON file in the project, read and convert it into a order dictionary type returned
    # print os.getcwd()
    if event_name=="EVENT":
        file_path = '../templates/'+event_name+'/'
        file_path = file_path + request_type + '.json'
    elif event_name=="GUEST":
        file_path = '../templates/' + event_name + '/'
        file_path = file_path + request_type + '.json'
    elif event_name == "SIGN":
        file_path = '../templates/' + event_name + '/'
        file_path = file_path + request_type + '.json'
    input_json = open(file_path).read()
    print input_json
    dict = eval(input_json)
    orderDict = OrderedDict(dict)
    # print orderDict
    # print type(orderDict)
    # print(orderDict)
    return orderDict

# getEVENTJsonTemplate("addevent","EVENT")
# getEVENTJsonTemplate("addguest","GUEST")
# getEVENTJsonTemplate("signevent","SIGN")
