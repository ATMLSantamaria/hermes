#!/usr/bin/env python3



import sys
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
c=input("Enter count: ")
p=input("Enter position: ")
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
# EXTRAE TOTAS LAS URL que por algun motivo empiezan pora a
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))

#print(soup.get_text())
