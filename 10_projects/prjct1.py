data = {
    "device": "sensor-1",
    "values": [23, 25, 23, 21],
    "active": True
}


print(f"Type:{type(data).__name__}")
print(f"Keys:{len(data)}")
unique_count = len(set(data["values"]))
print(f"Unique value in 'values':{unique_count}")

for key,value in data.items():
    print(f"key:{key}")
    print(f"value:{value}")
    print(f"Type: {type(value).__name__}")
    if isinstance(value,list):
        print(f"length of list: {len(value)} ")
