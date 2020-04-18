#!/usr/bin/env python3
import sqlite3
import re
#ESTOS DOS SIGUIENTES COMANDOS SON NECESARIOS PARA
#ABRIR Y USAR LA BASE DE DATOS.
#EL PRIMERO "CONECTA" Y EL SEGUNDO "SE USA PARA DAR ORDENES"

cons=sqlite3.connect('emaildb.sqlite')
cur=cons.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')
#Ahora usando cur.executepuedo dar ordenes en sqlite
cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

#AHORA VOY HACER LO QUE HACIA SIEMPRE PARA LEER ARCHIVO

fname=input("Enter file name: ")
if len(fname)<1:
    fname='mbox-short.txt'
fhandle=open(fname,'r')

for line in fhandle:
    if not line.startswith('From: '):
        continue
    pieces=line.split()
    email=pieces[1]
    org2=re.findall('@(.+)',email)
    org=org2[0]
    #print(email,org)

    cur.execute('SELECT count FROM Counts WHERE org = ?', (org,))
    row=cur.fetchone()
    if row is None:
        cur.execute('INSERT INTO Counts (org,count) VALUES(?,1)',(org,))
    else:
        cur.execute('UPDATE Counts SET count=count+1 WHERE org=?',(org,))
    cons.commit()
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()
