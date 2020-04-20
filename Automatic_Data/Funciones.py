import urllib.request, urllib.parse, urllib.error
import ssl
import json
import requests
import sqlite3
import threading, time
def Descargar_Dividendos(serviceurl,version,caracteristica,symbol,tipo,CLAVE):
    name="Info_Dividendos/log_divididend_"+str(symbol)[1:]+".txt"
    handle=open(name,'w')
    #CLAVE = 'Tpk_385aaf6516544f10bbd63f3ff5f87b4b'
        
    #serviceurl = 'https://sandbox.iexapis.com'
    #database= 'prueba_stocks_db.sqlite'
    #version = '/stable'
    #/stock/{symbol}/dividends/{range}
    #caracteristica= '/stock' #
    #simbol= '/xom'
    #tipo = '/quote' # /company
    #list_stocks=['/xom'] #,'/vod','/upwk','/acs']

    #symbol=list_stocks[0]
    print("LOS DATOS DE DIVIDENDOS DE", symbol)
    handle.write("LOS DATOS DE DIVIDENDOS DE -> ")
    handle.write(str(symbol))
    handle.write("\n\n")
        
    historia_dividends=[]
    contador=5
    while(contador > 0):

        a=str(contador)
        url_dividends=serviceurl+version+caracteristica+symbol+'/dividends/'+a+'y'+'?token='+CLAVE
        #print(url_dividens)
        print(a+"y atras")
        data_dividends=requests.get(url_dividends).json()
        try:
            print(data_dividends[0]['amount'])
            handle.write(str(data_dividends[0]))
            lista_claves=data_dividends[0].keys()
            for i in lista_claves:
                handle.write("i es")
                handle.write(str(i)+'\n')
                handle.write(str(i)+" = "+str(data_dividends[0][i])+"\n")
                handle.write("-------------\n")
            historia_dividends.append(data_dividends[0]['amount'])
        except:
            print("No hay data de dividendos este año")
            historia_dividends.append(0)
        contador -=1
    handle.close()
    print(historia_dividends)
    return historia_dividends

#CLAVE = 'Tpk_385aaf6516544f10bbd63f3ff5f87b4b'
        
#serviceurl = 'https://sandbox.iexapis.com'
#database= 'prueba_stocks_db.sqlite'
#version = '/stable'
#/stock/{symbol}/dividends/{range}
#caracteristica= '/stock' #
#simbol= '/xom'
#tipo = '/quote' # /company
#list_stocks=['/xom'] #,'/vod','/upwk','/acs']
#symbol=list_stocks[0]

#historic_dividend=Descargar_Dividendos(serviceurl,version,caracteristica,symbol,tipo,CLAVE)
#print(historic_dividend)