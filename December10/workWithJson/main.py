import json

json_file_path = "example_1.json"
# Convert json data values to dict
with open(json_file_path,'r') as json_file:
    data = json.load(json_file)
    print(data)
    print(type(data))