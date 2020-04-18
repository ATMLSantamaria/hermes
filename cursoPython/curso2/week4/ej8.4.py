#!/usr/bin/python3

fname=input("Enter file name: ")
fhand=open(fname,'r')
lst=list()
for line in fhand:
	a=line.rstrip()
	words=a.split()
	#print(words)
	for word in words:
		if word in lst:
			continue
		lst.append(word)
	#print(lst)
lst.sort()
print(lst)	

