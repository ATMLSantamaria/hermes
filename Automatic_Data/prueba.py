import urllib.request, urllib.parse, urllib.error
import ssl
import json
import requests
import sqlite3
import threading, time
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
#url=serviceurl+version+caracteristica+simbol+'/quote?token='+CLAVE
#url2=serviceurl+version+caracteristica+simbol+'/company?token='+CLAVE
#url3=url=serviceurl+version+caracteristica+simbol+'/quote/companyName?token='+CLAVE
#print('https://sandbox.iexapis.com/stable/stock/aapl/quote?token=Tpk_385aaf6516544f10bbd63f3ff5f87b4b')
#print(url)

#datos=raw_datos.json()
print("---------------")
#datos1 = requests.get(url).json()
#datos2 = requests.get(url2).json()
def Descargar_Datos(serviceurl,version,caracteristica,symbol,tipo,CLAVE):
    #threading.Timer(5.0, Descargar_Datos.start()
    url_local=serviceurl+version+caracteristica+symbol+tipo+'?token='+CLAVE
    print(url_local)
    data=requests.get(url_local).json()
    url_local='hsjsjh'
    return data
#datos3 = requests.get(url3).json()
#request3 = requests.get('https://sandbox.iexapis.com/stable/stock/aapl/quote?token=Tpk_385aaf6516544f10bbd63f3ff5f87b4b').json()
#print("datos",datos1)
#print("---------------")
#print(datos2)
#print("-----------")
#print(datos3)

#datos es un diccionatio
#print("--------")
#lista_claves=datos1.keys()
#for i in lista_claves:
#    print (i,"=",datos1[i]) 
#request2 = urllib.request.get(url)

#EL PROGRAMA HA RECIBIDO EL STRING Y LO IMPRIMO para
#ENTENDERLO
#print('------------------')
#print(data)
vector_relevant_keys=['symbol','companyName','latestPrice','peRatio',]
#for element in vector_relevant_keys:
#    print(element,"=",datos1[element])

#print('------------------hfhfhfhfh')




#EL PROBLEMA CON ESTA BASE DE DATOS ES QUE NO SE VA A ACTUALIZAR
def Introduce_In_DB(d):
    conn = sqlite3.connect('stocks.sqlite')
    cur = conn.cursor()

    cur.executescript('''
    DROP TABLE IF EXISTS STOCKS2;
    CREATE TABLE IF NOT EXISTS STOCKS_TODAY (
        id   INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        symbol TEXT UNIQUE,
        companyName TEXT,
        latestPrice TEXT,
        peRATIO TEXT
        )
    ''')
    #cur.execute('''
    #CREATE TABLE IF NOT EXISTS STOCKS2 (SYMBOL TEXT, COMPANY_NAME TEXT, latestPrice REAL, peRATIO REAL)''')
    print(d['symbol'])
    print(d['companyName'])
    print(d['latestPrice'])
    print(d['peRatio'])
    cur.execute('''INSERT OR IGNORE INTO STOCKS_TODAY (symbol, companyName, latestPrice, peRatio)
                VALUES (?, ?, ?, ? )''', (d['symbol'],d['companyName'],d['latestPrice'],d['peRatio'] ) )

    conn.commit()

    return 0
connn = sqlite3.connect('stocks.sqlite')
curr = connn.cursor()
curr.executescript('''DROP TABLE IF EXISTS STOCKS_TODAY''')
connn.commit()
list_stocks=['/xom','/vod','/upwk','']

for k in list_stocks:
    print(k)
    d=Descargar_Datos(serviceurl,version,caracteristica,k,tipo,CLAVE)
    #print(d['symbol'])
    #print(d)
    #print("estamos en el bucle")
    Introduce_In_DB(d)


