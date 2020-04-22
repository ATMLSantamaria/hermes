import urllib.request, urllib.parse, urllib.error
import ssl
import json
import requests
import sqlite3
import threading, time

def Introduce_In_DB(received_data,data_about_dividend,db_name):
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()

    cur.executescript('''
    DROP TABLE IF EXISTS STOCKS2;
    CREATE TABLE IF NOT EXISTS STOCKS_TODAY (
        id   INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        Symbol TEXT UNIQUE,
        CompanyName TEXT,
        LatestPrice TEXT,
        PER_Ratio TEXT,
        Average_Dividend REAL,
        Max_Dividend REAL,
        Yield REAL 
        )
    ''')
 
    cur.execute('''INSERT OR IGNORE INTO STOCKS_TODAY (Symbol, CompanyName, LatestPrice, PER_Ratio, Average_Dividend, Max_Dividend, Yield)
                VALUES (?, ?, ?, ? ,? ,? ,? )''', (received_data['symbol'],received_data['companyName'],received_data['latestPrice'],received_data['peRatio'],data_about_dividend[0],data_about_dividend[1],data_about_dividend[2] ) )

    conn.commit()

    return 0

def Descargar_Datos(serviceurl,version,caracteristica,symbol,tipo,CLAVE):
    url_local=serviceurl+version+caracteristica+symbol+tipo+'?token='+CLAVE
    #print(url_local)
    data=requests.get(url_local).json()
    return data

def Descargar_Dividendos(serviceurl,version,caracteristica,symbol,tipo,CLAVE):
    name="Info_Dividendos/log_divididend_"+str(symbol)[1:]+".txt"
    handle=open(name,'w')
    #print("LOS DATOS DE DIVIDENDOS DE", symbol)
    handle.write("LOS DATOS DE DIVIDENDOS DE -> ")
    handle.write(str(symbol))
    handle.write("\n\n")
        
    dividendos_last_years=[]
    frecuencia_dividendos_last_years=[]
    contador=5
    while(contador > 0):

        a=str(contador)
        url_dividends=serviceurl+version+caracteristica+symbol+'/dividends/'+a+'y'+'?token='+CLAVE
        #print(a+"y atras")
        data_dividends=requests.get(url_dividends).json()
        try:
            #print(data_dividends[0]['amount'])
            handle.write(str(data_dividends[0]))
            lista_claves=data_dividends[0].keys()
            for i in lista_claves:
                handle.write("i es")
                handle.write(str(i)+'\n')
                handle.write(str(i)+" = "+str(data_dividends[0][i])+"\n")
                handle.write("-------------\n")
            dividendos_last_years.append(data_dividends[0]['amount'])
        except:
            #print("No hay data de dividendos este año")
            #pass
            dividendos_last_years.append(0)
        contador -=1
        try:
            frecuencia_dividendos_last_years.append(data_dividends[0]["frequency"])
        except:
            frecuencia_dividendos_last_years.append("annual")
    handle.close()
    #print(dividendos_last_years)
    
    return dividendos_last_years,frecuencia_dividendos_last_years

def Analisis_Dividendos(historico_dividendos,datos,frecuencia_dividendos_last_years):
    average_dividend=0
    c=0
    max_div=0
    for div_year,freq_year in zip(historico_dividendos,frecuencia_dividendos_last_years):
        if(freq_year=="quarterly"):
            div_year = float(div_year) * 4
        elif(freq_year=="semi-annual"):
            div_year = float(div_year)*2
        else:
            div_year=float(div_year)
        average_dividend += div_year
        c += 1
        if (div_year==0):
            c -=1
        if div_year > max_div:
            max_div=div_year
    if (c==0):
        average_dividend==0
    else:
        average_dividend = average_dividend / c
    max_div
    if (average_dividend == 0):
        yield_dividend = 0
    else:
        

        yield_dividend = average_dividend / datos['latestPrice']  * 100
    
    data_about_dividend = [average_dividend,max_div,yield_dividend]
    return data_about_dividend
