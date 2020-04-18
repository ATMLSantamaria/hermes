#!/usr/bin/python3
#PROGRAMA QUE VA A EXTRAER NÚMEROS DE UN TEXTO
import re

sm=0
count=0
superlinea=list()
fname=input("Enter name of file: ")
if len(fname) < 1 : 
	fname = "regex_sum_336793.txt"
fhandle=open(fname,"r")
for line in fhandle:
	line=line.rstrip()
	y=re.findall("([0-9]+)",line)
	superlinea=superlinea+y
for num in superlinea:
	count=count+1
	sm=sm+float(num)

#print(superlinea)

print("sum",sm)

