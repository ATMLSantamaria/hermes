import urllib.request, urllib.parse, urllib.error
import ssl
import json
import requests
import sqlite3
import threading, time
from Funciones import Descargar_Dividendos, Descargar_Datos, Introduce_In_DB, Analisis_Dividendos


election = input("elija modo funcional(f) o de prueba(p)")
if (election=='f'):
    #hacer funcion que lea del fichero mi clave
    CLAVE = 
    serviceurl = 
    database= 'real_stocks_db.sqlite'
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
list_interesting_stocks=['/xom','/t','/abbv','/rtx','/emr','/vod']
list_stocks=list_interesting_stocks
#['/xom','/vod','/upwk','/acs']
connn = sqlite3.connect(database)
curr = connn.cursor()
curr.executescript('''DROP TABLE IF EXISTS STOCKS_TODAY''')
curr.executescript('''DROP TABLE IF EXISTS STOCKS2''')
connn.commit()

tabla_dividendos=[["5y","4y","3y","2y","1y","name"]]
for stock in list_stocks:

    #print(stock)
    
    datos = Descargar_Datos(serviceurl,version,caracteristica,stock,tipo,CLAVE)
    dividendos_last_years,frecuencia_dividendos = Descargar_Dividendos(serviceurl,version,caracteristica,stock,tipo,CLAVE)
    data_about_dividend = Analisis_Dividendos(dividendos_last_years,datos,frecuencia_dividendos)
    
    #print(d)
    Introduce_In_DB(datos,data_about_dividend,database)
    dividendos_last_years.append(stock) #para añadir el nombre al final
    tabla_dividendos.append(dividendos_last_years)





print("----------------")


for iii in tabla_dividendos:
    print(iii)

