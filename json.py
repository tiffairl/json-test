import json

x = '{"name": "Yamcha", "age": 51}'

y = json.loads(x)

print(y["name"])