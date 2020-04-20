import urllib.request, urllib.parse, urllib.error
import ssl
import json
import requests
import sqlite3
import threading, time
from Funciones import Descargar_Dividendos

def Introduce_In_DB(received_data,db_name):
    conn = sqlite3.connect(db_name)
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
    print(d['symbol'])
    print(d['companyName'])
    print(d['latestPrice'])
    print(d['peRatio'])
    cur.execute('''INSERT OR IGNORE INTO STOCKS_TODAY (symbol, companyName, latestPrice, peRatio)
                VALUES (?, ?, ?, ? )''', (d['symbol'],d['companyName'],d['latestPrice'],d['peRatio'] ) )

    conn.commit()

    return 0

def Descargar_Datos(serviceurl,version,caracteristica,symbol,tipo,CLAVE):
    url_local=serviceurl+version+caracteristica+symbol+tipo+'?token='+CLAVE
    print(url_local)
    data=requests.get(url_local).json()
    url_dividens=serviceurl+version+caracteristica+symbol+'/dividends/5y'+'?token='+CLAVE
    #ESTE 5y implica que pedimos los dividendos de hace 5 años
    #Podemos poner 4y, 3y,2y,1y,ytd (este año), next (el proximo)
    data_dividends=requests.get(url_dividens).json()
    print("LOS DATOS DE DIVIDENDOS DE", symbol)
    try:
        lista_claves=data_dividends[0].keys()
        print("lista claves",lista_claves)
        for i in lista_claves:
            print("i es", i)
            print(i," = ",data_dividends[0][i])
            print("-------------")
        return data
    except:
        print("No hay datos de dividendos")
        return data


election = input("elija modo funcional(f) o de prueba(p)")
if (election=='f'):
    #CLAVE = 
    #serviceurl = 
    #database= 'real_stocks_db.sqlite'
    pass
elif(election=='p'):
    CLAVE = 'Tpk_385aaf6516544f10bbd63f3ff5f87b4b'
    serviceurl = 'https://sandbox.iexapis.com'
    database= 'prueba_stocks_db.sqlite'
else:
    CLAVE = 'Tpk_385aaf6516544f10bbd63f3ff5f87b4b'
    serviceurl = 'https://sandbox.iexapis.com'
    database= 'prueba_stocks_db.sqlite'


version = '/stable'
#/stock/{symbol}/dividends/{range}
caracteristica= '/stock' #
#simbol= '/xom'
tipo = '/quote' # /company
list_stocks=['/xom','/vod','/upwk','/acs']
connn = sqlite3.connect(database)
curr = connn.cursor()
curr.executescript('''DROP TABLE IF EXISTS STOCKS_TODAY''')
curr.executescript('''DROP TABLE IF EXISTS STOCKS2''')
connn.commit()


for k in list_stocks:
    print(k)
    d=Descargar_Datos(serviceurl,version,caracteristica,k,tipo,CLAVE)
    #print(d['symbol'])
    #print(d)
    d=Introduce_In_DB(d,database)
    e=Descargar_Dividendos(serviceurl,version,caracteristica,k,tipo,CLAVE)

