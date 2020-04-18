#!/usr/bin/python3

#Programa 1 semana 5

hrs=input ("Enter Hours:")
h = float(hrs)
rate=input("Enter Rate")
rt=float(rate)

if h < 40:
	pay=h*rt
	print(pay)
else:
	hours_above=h-40
	pay=hours_above*rt*1.5+40*rt
	print(pay)

