#!/usr/bin/env python3

from urllib.request import urlopen
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
if len(url)<1:
    url="http://py4e-data.dr-chuck.net/comments_42.xml"
xml = urlopen(url, context=ctx).read()

stuff = ET.fromstring(xml)
lst = stuff.findall('comments/comment')
print('comments count:', len(lst))
sm=0
for item in lst:
    #print('Name', item.find('name').text)
    #print('Age', item.find('count').text)
    age=float(item.find('count').text)
    sm=sm+age

print(sm)
    #print('Attribute', item.get('x'))
