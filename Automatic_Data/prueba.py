import urllib.request, urllib.parse, urllib.error
import ssl
import json

#NECESARIO PARA ENTRAR A LA API DE GOOGLE CON MI CUENTA
CLAVE_API = 'AIzaSyAfbHH3oH0Gz7v_6Rq3s8yX0ENBjcfcssA'
serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#EN ADDRESS PREPARO LA URL A LA QUE DEBO ACCEDER PARA QUE LA api
#ME DEVUELVA LO QUE QUIERO

address=input('Introducir localizacion: ')
parms=dict()
parms['address']=address
parms['key']=CLAVE_API
print(parms)
url=serviceurl+urllib.parse.urlencode(parms)
print(url)

#EL PROGRAMA SE CONECTA Y RECIBE UN STRING
print('RETRIEVING',url)
#fhand=urllib.request.urlopen(url,context=ctx)
#data=fhand.read().decode()
data=urllib.request.urlopen(url,context=ctx).read().decode()
print('RETRIEVED',len(data),'characters')
#EL PROGRAMA HA RECIBIDO EL STRING Y LO IMPRIMO para
#ENTENDERLO
print('------------------')
print(data)
print('------------------')
#json.loads(data) lee json y lo convierte en un diccionario-lista
js=json.loads(data)
print(js)
#ahora unicamente tengo que acceder a lo que yo QUIERO
pst_code=js['results'][0]['address_components'][5]['long_name']
print('postal_code',pst_code)
