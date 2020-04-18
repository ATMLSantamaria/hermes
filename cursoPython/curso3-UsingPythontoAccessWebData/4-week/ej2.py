#!/usr/bin/env python3

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')

if len(url)<1:
	url="http://py4e-data.dr-chuck.net/known_by_Fikret.html"
c=input("Enter count: ")
if len(c)<1:
	c=4
p=input("Enter position: ")
if len(p)<1:
	p=3 
c=int(c)
p=int(p)
count=0
while True:
	html2=urlopen(url).read()
	soup2 = BeautifulSoup(html2, "html.parser")
	buscar=soup2('a')
	element=buscar[p-1]
	url=element.get('href',None)
	#print(url)
	#nombre=print(element.attrs)
	nombre=str(re.findall("by_(.+)\.",url)[0])
	#print(nombre)
	#print('URL',element.get('href',None))
	count=count+1
	if count==c:
		print(url)
		print(nombre)
		break
		


"""
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
hola=list()
# Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:
    # Look at the parts of a tag
	#print('TAG:', tag)
	#print('URL:', tag.get('href', None))
	#print('Contents:', tag.contents[0])
	#print('Attrs:', tag.attrs)
	
	hola.append(tag.contents[0])
	

print("---------------------------------------")
sm=0
for numero in hola:
	sm=sm+float(numero)
#print(hola)
#print("------------------------------------------")
#print(sm)
"""
