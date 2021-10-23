#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 16:19:05 2021

@author: vazquez
"""

import numpy as np

a = 3
b = [2,3]
c = np.arange(1,78,2) #arrange(Start, end (exclusive), steps)

#Variablen werden gespeichert:
np.savez('test.npz', b=b, c=c)          

#Zunaechst werden die Variablen geloescht:
del a
del b
del c

#Variablen werden geladen:
data = np.load('test.npz')                      

#Es wird geprueft, ob variable a wirklich geloescht wurde:
print("Gespeicherte Variablen: ", data.files)
print("Inhalt:")
print(data['b'])
print(data['c'])

