#!/usr/bin/env python3
import urllib.request,urllib.parse,urllib.error
import http
import sqlite3
import json
import time
import ssl
import sys

#CLAVE_API=False

CLAVE_API='AIzaSyAfbHH3oH0Gz7v_6Rq3s8yX0ENBjcfcssA'

if CLAVE_API is False:
    CLAVE_API = 42
    serviceurl = "http://py4e-data.dr-chuck.net/json?"
else :
    serviceurl = "https://maps.googleapis.com/maps/api/geocode/json?"

#crear base de datos

conn=sqlite3.connect('geodata.sqlite')
cur=conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS Locations(address TEXT,geodata TEXT)''')

#Ignore ssl certificate errors

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

fhandle=open("where.data")
count=0
for line in fhandle:
    if count > 200:
        print('retrieved 5 locations, restart to retrieve more')
        break
    print(line)
    print('--------')
    address=line.strip()
    print(address)
    cur.execute("SELECT geodata FROM Locations WHERE address= ?",(memoryview(address.encode()),))
    try:
        data=cur.fetchone()[0]
        print("Found in data base ", address)
        continue
    except:
        pass
    parms=dict()
    parms["address"]=address
    if CLAVE_API is not False:
        parms["key"]=CLAVE_API
    url=serviceurl+urllib.parse.urlencode(parms)
    print('Retrieving', url)
    url_handle=urllib.request.urlopen(url,context=ctx)
    data=url_handle.read().decode()
    print('Retrieved',len(data),"characters")
    #print(data)
    count=count+1

    try:
        js=json.loads(data)
        #print(js)
    except:
        print(data)
        continue
    if 'status' not in js or (js['status'] != 'OK' and js['status'] != 'ZERO_RESULTS'):
        print('====FAILURE TO RETRIEVE====')
        print(data)
        break
    cur.execute('INSERT INTO Locations (address,geodata) VALUES(?,?)',(memoryview(address.encode()),memoryview(data.encode())))
    conn.commit()
    if count %10 ==0:
        print('Pausing for a bit...')
        time.sleep(5)
print("Run geodump.py to read the data from the database so you can vizualize it on a map.")
