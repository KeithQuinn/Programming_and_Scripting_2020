import json
filename = "testdict.json"

def readdict():
    with open(filename) as f:
        return json.load(f)

somedict = readdict()

print(somedict)