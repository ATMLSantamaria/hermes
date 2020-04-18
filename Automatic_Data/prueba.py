import urllib.request, urllib.parse, urllib.error
import ssl
import json
import requests

#curl -k 'https://sandbox.iexapis.com/stable/stock/aapl/quote?token=YOUR_TOKEN_HERE'
# -> para usar con bash -> curl -k 'https://cloud.iexapis.com/stable/stock/aapl/quote?token=YOUR_TOKEN_HERE'
#NECESARIO PARA ENTRAR A LA API DE GOOGLE CON MI CUENTA
CLAVE_API = 'Tpk_385aaf6516544f10bbd63f3ff5f87b4b'
#serviceurl = 'https://cloud.iexapis.com/'
serviceurl = 'https://sandbox.iexapis.com'

# Ignore SSL certificate errors
#ctx = ssl.create_default_context()
#ctx.check_hostname = False
#ctx.verify_mode = ssl.CERT_NONE

#EN ADDRESS PREPARO LA URL A LA QUE DEBO ACCEDER PARA QUE LA api
#ME DEVUELVA LO QUE QUIERO
version = '/stable'
#/stock/{symbol}/dividends/{range}
caracteristica= '/stock'
simbol= '/xom'


url=serviceurl+version+caracteristica+simbol+'/quote?token='+CLAVE_API

print('https://sandbox.iexapis.com/stable/stock/aapl/quote?token=Tpk_385aaf6516544f10bbd63f3ff5f87b4b')
print(url)
datos = requests.get(url).json()
#request3 = requests.get('https://sandbox.iexapis.com/stable/stock/aapl/quote?token=Tpk_385aaf6516544f10bbd63f3ff5f87b4b').json()
print(datos)
#datos es un diccionatio
print("--------")
lista_claves=datos.keys()
for i in lista_claves:
    print (i,"=",datos[i]) 
#request2 = urllib.request.get(url)
#EL PROGRAMA SE CONECTA Y RECIBE UN STRING
##print('RETRIEVING',url)
#print('hasta aqui funciona')
#fhand=urllib.request.urlopen(url)
#data=fhand.read().decode()
#data=urllib.request.urlopen(url,context=ctx).read().decode()
#print('RETRIEVED',len(data),'characters')
#EL PROGRAMA HA RECIBIDO EL STRING Y LO IMPRIMO para
#ENTENDERLO
print('------------------')
#print(data)
print('------------------')
#json.loads(data) lee json y lo convierte en un diccionario-lista
#js=json.loads(data)
#print(js)
#ahora unicamente tengo que acceder a lo que yo QUIERO
#pst_code=js['results'][0]['address_components'][5]['long_name']
#print('postal_code',pst_code)