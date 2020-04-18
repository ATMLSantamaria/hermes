import urllib.request, urllib.parse, urllib.error
import ssl
import json
import requests
import sqlite3

#curl -k 'https://sandbox.iexapis.com/stable/stock/aapl/quote?token=YOUR_TOKEN_HERE'
# -> para usar con bash -> curl -k 'https://cloud.iexapis.com/stable/stock/aapl/quote?token=YOUR_TOKEN_HERE'
#NECESARIO PARA ENTRAR A LA API DE GOOGLE CON MI CUENTA
CLAVE = 'Tpk_385aaf6516544f10bbd63f3ff5f87b4b'
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
caracteristica= '/stock' #
simbol= '/xom'
tipo = '/quote' # /company
#/company te da otro tipo de datos

url=serviceurl+version+caracteristica+simbol+'/quote?token='+CLAVE
url2=serviceurl+version+caracteristica+simbol+'/company?token='+CLAVE
#url3=url=serviceurl+version+caracteristica+simbol+'/quote/companyName?token='+CLAVE
print('https://sandbox.iexapis.com/stable/stock/aapl/quote?token=Tpk_385aaf6516544f10bbd63f3ff5f87b4b')
print(url)

#datos=raw_datos.json()
print("---------------")
datos1 = requests.get(url).json()
datos2 = requests.get(url2).json()
#datos3 = requests.get(url3).json()
#request3 = requests.get('https://sandbox.iexapis.com/stable/stock/aapl/quote?token=Tpk_385aaf6516544f10bbd63f3ff5f87b4b').json()
print("datos",datos1)
print("---------------")
print(datos2)
print("-----------")
#print(datos3)

#datos es un diccionatio
print("--------")
lista_claves=datos1.keys()
for i in lista_claves:
    print (i,"=",datos1[i]) 
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
vector_relevant_keys=['symbol','companyName','latestPrice','peRatio',]
for element in vector_relevant_keys:
    print(element,"=",datos1[element])

print('------------------')
#json.loads(data) lee json y lo convierte en un diccionario-lista
#js=json.loads(data)
#print(js)
#ahora unicamente tengo que acceder a lo que yo QUIERO
#pst_code=js['results'][0]['address_components'][5]['long_name']
#print('postal_code',pst_code)


conn = sqlite3.connect('stocks.sqlite')
cur = conn.cursor()

cur.executescript('''
CREATE TABLE IF NOT EXISTS STOCKS_TODAY (
    id   INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    symbol TEXT UNIQUE,
    companyName TEXT,
    latestPrice TEXT,
    peRATIO TEXT
    )
''')
cur.execute('''
CREATE TABLE IF NOT EXISTS STOCKS2 (SYMBOL TEXT, COMPANY_NAME TEXT, latestPrice REAL, peRATIO REAL)''')
print(datos1['symbol'])
print(datos1['companyName'])
print(datos1['latestPrice'])
print(datos1['peRatio'])
cur.execute('''INSERT INTO STOCKS_TODAY (symbol, companyName, latestPrice, peRatio)
            VALUES (?, ?, ?, ? )''', (datos1['symbol'],datos1['companyName'],datos1['latestPrice'],datos1['peRatio'] ) )

conn.commit()

