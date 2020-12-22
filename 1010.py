# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 10:49:38 2020

@author: Rohr
"""

a = input().split(" ")
b = input().split(" ")

c, d, e = a
f, g, h = b

print("VALOR A PAGAR: R$ %0.2f" %(int(d) * float(e) + int(g) * float(h)))