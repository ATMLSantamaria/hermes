#! /usr/bin/python3
def computepay(hrs,rate):
	h = float(hrs)
	rt=float(rate)
	if h < 40:
		pay=h*rt
	else:
		hours_above=h-40
		pay=hours_above*rt*1.5+40*rt
	return pay
horas=input ("Enter Hours:")
tasa=input("Enter Rate:")
payment=computepay(horas,tasa)

print(payment)
