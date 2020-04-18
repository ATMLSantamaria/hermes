#!/usr/bin/python3


fname = input("Enter file: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fhand=open(fname)
lst=list()
for line in fhand:
	if not line.startswith("From "):
		continue
	a=line.rstrip()
	words=a.split()
	#print(words)
	lst.append(words[1])
#print(lst)
counts=dict()
for word in lst:
	counts[word]=counts.get(word,0)+1
bigcount=None
bigword=None
for word,count in counts.items():
	if bigcount is None or count>bigcount:
		bigword=word
		bigcount=count
print(bigword,bigcount)










