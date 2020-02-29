import json
filename = "testdict.json"
sample = dict(name = "Fred", age = 31, grades = [1, 34, 55])

def writedict (obj):
    with open(filename, "wt") as f:
        json.dump(obj,f)

writedict(sample)

print(sample)