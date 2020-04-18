#!/usr/bin/python3

fname=input("Enter file name: ")
if len(fname) < 1 :
	fname = "mbox-short.txt"
fhand=open(fname,'r')
count=0
for line in fhand:
	if not line.startswith("From "):
		continue
	a=line.rstrip()
	words=a.split()
	print(words[1])
	count=count+1
print("There were", count, "lines in the file with From as the first word")
