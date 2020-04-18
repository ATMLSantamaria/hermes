#!/usr/bin/env python3

import urllib.request, urllib.parse
import json
import ssl
CLAVE_API=42
serviceurl='http://py4e-data.dr-chuck.net/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address=input("Introduce tu direccion: ")
if len(address)<1:
    address="South Federal University"

parms=dict()
parms['address']=address
parms['key']=CLAVE_API

url=serviceurl+urllib.parse.urlencode(parms)

print('RETIEVING',url)
#aqui abro la pagina web, en este caso la pagina web que abro
#es la base de datos de la información que le he pedido a la API
url_handle=urllib.request.urlopen(url,context=ctx)
data_string=url_handle.read().decode()
#print('RETRIEVED',len(data_string),'characters')
#print(data_string)
data_json=json.loads(data_string)

print("----------")
#print("numero de items",len(data_json["results"][0]))
print(data_json["results"][0]["place_id"])
