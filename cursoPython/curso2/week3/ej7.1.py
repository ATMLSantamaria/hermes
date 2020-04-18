#!/usr/bin/python3
#CODIGO PARA ABRIR ARCHIVO, LEER A TRAVES DE EL,
#E IMPRIMIRLO CON MAYÚSCULAS
fname=input("Enter file name: ")
fhand = open(fname)
#By default, when only the filename is passed, the open function opens the file
#in read mode
for i in fhand:
	print(i.rstrip().upper())


