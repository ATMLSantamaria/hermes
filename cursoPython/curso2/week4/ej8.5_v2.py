#!/usr/bin/python3

fname=input("Enter file name: ")
if len(fname) < 1 :
	fname = "mbox-short.txt"
fhand=open(fname,'r')
count=0
for line in fhand:
	a=line.rstrip()
	words=a.split()
	#print(words)
	if len(words) < 1:
		continue
	if words[0] != 'From' :
		continue
	print(words[1])
	count=count+1
print("There were", count, "lines in the file with From as the first word")
