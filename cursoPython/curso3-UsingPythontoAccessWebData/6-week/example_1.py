#!/usr/bin/env python3
import json

data = '''
{
  "name" : "Chuck",
  "phone" : {
    "type" : "intl",
    "number" : "+1 734 303 4456"
   },
   "email" : {
     "hide" : "yes"
   }
}'''

data2='''
{ "id" : "001",
  "x" : "2",
  "name" : "Chuck"
}
'''
data2_json=json.loads(data2)
json_leido=json.loads(data) # esto es un diccionario
print(json_leido) #esto imprime el diccionario
print('Name',json_leido["name"]) #esto busca el valor para la clave "name"



print("-------------------")
print(data2_json)
