import json

data = json.load(open('./lib/db/object.json'))

print(data["species"]["locaton"])