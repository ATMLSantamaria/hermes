#!/usr/bin/env python3
import json

data = '''
[
  { "id" : "001",
    "x" : "2",
    "name" : "Chuck"
  } ,
  { "id" : "009",
    "x" : "7",
    "name" : "Brent"
  }
]'''

json_leido = json.loads(data)
print('User count:', len(json_leido))

for elemnt in json_leido:
    print('Name', elemnt['name'])
    print('Id', elemnt['id'])
    print('Attribute', elemnt['x'])
