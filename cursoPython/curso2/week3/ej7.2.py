#!/usr/bin/python3

fname = input("Enter file name: ")
fh = open(fname)
count=0
sm=0
for line in fh:
	if not line.startswith("X-DSPAM-Confidence:") : 
		continue
	count=count+1
	pospun=line.find(":")
	a=line[pospun+1:]
	a=float(a)
	sm=sm+a

resultado=sm/count
print("Average spam confidence:",resultado)


