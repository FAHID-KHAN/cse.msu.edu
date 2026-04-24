"""
    Json cleaner and formatter project
"""


import json 

def read_json(filename):
    with open (filename,"r") as file:
       return json.load(file)

def save_json(filename,data):
    with open(filename,"w") as file:
        json.dump(data,file,indent=4,sort_keys=True)

def clean_data(data):
    cleaned = {}
    pass
