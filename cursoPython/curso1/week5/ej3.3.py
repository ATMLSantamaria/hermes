#!/usr/bin/python3

score=input("Enter score")
try:
	x=float(score)
except:
	print("NUMBER PLEASE")
if x > 1 or x < 0:
	print("ERROR, score should be between 0 and 1")
else:
	if x >= 0.9:
		print("A")
	elif x >= 0.8:
		print("B")
	elif x >= 0.7:
		print("C")
	elif x >= 0.6:
		print("D")
	else:
		print("F")
 
