#!/usr/bin/env python3

import urllib.request
import ssl
import json

url=input('Introduce URL')
if len(url)<1:
    url="http://py4e-data.dr-chuck.net/comments_42.json"
#aqui abro la url
url_o=urllib.request.urlopen(url)
#aqui leo la url en forma de un string
url_handle=url_o.read().decode()
#aqui uso json para convertir este string en un objeto diccionario
data_json=json.loads(url_handle)
sm=0
data_age=data_json['comments']

for keys in data_age:
    edad=int(keys['count'])
    sm=sm+edad

#print(data_age)
print(sm)
