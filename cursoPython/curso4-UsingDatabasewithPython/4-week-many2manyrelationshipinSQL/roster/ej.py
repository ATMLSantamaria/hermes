#!/usr/bin/env python3
import json
import sqlite3

conn=sqlite3.connect('sqlite_json_db.sqlite')
cur=conn.cursor()

#Mandamos la orden de crear las tablas dentro de la db:

cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;

CREATE TABLE User (
    id   INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
);
CREATE TABLE Course (
    id    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT UNIQUE
);
CREATE TABLE Member(
    user_id   INTEGER,
    course_id INTEGER,
    role      INTEGER,
    PRIMARY KEY (user_id,course_id)
);
''')
fname=input("Introduzca el nombre")
if len(fname)<1:
    fname='roster_data_sample.json'
#AHORA OPEN().READ() VA A LEER TODO EL ARCHIVO Y CONVERTIRLO
#EN UN STRING. El stirng que esta abajo es el archivo que leemo
'''
  [["Charley","si110",1],[ "Mea", "si110", 0 ],...]
'''
string_data=open(fname).read() #en un string raro json superdesordenado
json_data=json.loads(string_data) #en forma de listas y diccionarios
'''
print (string_data)
print('----------')
print(json_data)
'''
for element in json_data:
    nombre=element[0];
    titulo=element[1];
    role=element[2]
    print(nombre,titulo,role)

    cur.execute(''' INSERT OR IGNORE INTO User(name) VALUES (?)''',(nombre,))
    cur.execute('SELECT id FROM User WHERE  name= ?',(nombre, ))
    user_id=cur.fetchone()[0]

    cur.execute(''' INSERT OR IGNORE INTO Course(title) VALUES (?)''',(titulo,))
    cur.execute('SELECT id FROM Course WHERE  title = ?',(titulo, ))
    course_id=cur.fetchone()[0]

    cur.execute(''' INSERT OR REPLACE INTO Member(user_id,course_id,role) VALUES(?,?,?)''',(user_id,course_id,role))

    conn.commit()
