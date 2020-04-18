#!/usr/bin/python3

text = "X-DSPAM-Confidence:    0.8475"
dotpos=text.find(":")
final=text[dotpos+1:]
print(final)
numero=final.lstrip()
print(numero)
numero=float(numero)
print(numero)
