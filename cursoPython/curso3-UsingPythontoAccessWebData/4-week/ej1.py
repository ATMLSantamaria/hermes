#!/usr/bin/env python3

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
hola=list()
# Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:
    # Look at the parts of a tag
	print('TAG:', tag)
	print('URL:', tag.get('href', None))
	print('Contents:', tag.contents[0])
	print('Attrs:', tag.attrs)
	
	hola.append(tag.contents[0])
	

print("---------------------------------------")
sm=0
for numero in hola:
	sm=sm+float(numero)
print(hola)
print("------------------------------------------")
print(sm)
