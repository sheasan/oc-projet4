import json

## deserialization
with open('datafile.json') as json_file:
    data = json.load(json_file)
    print(data)

class PlayerManager:
    def __init__(self):
        self.registry = {}