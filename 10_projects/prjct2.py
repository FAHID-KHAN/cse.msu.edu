"""
    Json cleaner and formatter project
"""


import json 

required_fields = ["name","email","age"]
RENAME_MAP = {"active": "is_active", "score": "rating"}

def read_json(filename):
    with open (filename,"r") as file:
       return json.load(file)

def save_json(filename,data):
    with open(filename,"w") as file:
        json.dump(data,file,indent=4,sort_keys=True)
        print(f"Saved to {filename}")

def pretty_print(data):
    print(json.dumps(data,indent=4,sort_keys=True))

def remove_empty(data):
    cleaned = {}
    for key,value in data.items():
        if isinstance(value,dict):
            value = remove_empty(value)
        if value is not None and value != "" and value !={}:
            cleaned[key] = value
    return cleaned



def normalize_values(data):
    result = {}
    for key,value in data.items():
        if isinstance(value,dict):
            value = normalize_values(value)
        elif value == "true":
            value = True
        elif value == "false":
            value = False
        elif isinstance(value,str) and value.lstrip("-").isdigit():
            value = int(value)
        result[key] = value
    return result


def check_required(data,required):
    for field in required:
        if field not in data:
            print(f"Warning: missing required field")



def rename_keys(data,rename_map):
    result = {}
    for key,value in data.items():
        new_key = rename_map.get(key,key)
        result[new_key] = value
    return result 

if __name__ == "__main__":
    data = read_json("messy.json")
    data = normalize_values(data)
    data = remove_empty(data)
    check_required(data,required_fields)
    data = rename_keys(data,RENAME_MAP)
    pretty_print(data)
    save_json("cleaned.json",data)


