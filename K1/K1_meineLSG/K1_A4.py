#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fach: MODELLBILDUNG UND SIMULATION
Name: AUFGABE K1
@author: vazquez
Created on Fri Apr  2 15:09:49 2021
"""

import numpy as np # data arrays
#import scipy # scientific computing
import matplotlib.pyplot as plt # Visualisierung
#from numpy import pi as pi # für die Zahl pi

from scipy.io import loadmat
from scipy import interpolate

data = loadmat('mkl.mat')

x = data['x_werte'].flatten()               #Achtung, wird als 2D Matrix gespeichert [1,8], was 
y = data['y_werte'].flatten()               #...Problemen beim Plotten macht. flatten() druckt nDim 
                                            #...np.array in 1D np.array [ ,8].                                      

#ALTERNATIVE FUER 2D TO 1D NP.ARRAY UMWANDLUNG:

#temp_x = data['x_werte'].flatten()         #Achtung, wird als 2D Matrix gespeichert! 
#temp_y = data['y_werte'].flatten()         #Achtung, wird als 2D Matrix gespeichert! 
#x = temp_x[0,:]                            #Umwandlung in Zeilenvektor.
#y = temp_y[0,:]                            #Umwandlung in Zeilenvektor. 


#INTERPOLATED FUNCTION:

f_inter = interpolate.interp1d(x,y, kind='cubic')   #Warum cubic?
x_inter = np.linspace(0,1.35, 100)         #(start, stop, values between)
y_inter = f_inter(x_inter)


fig = plt.figure(1, figsize=(10,6)); fig.clf()
ax = fig.add_subplot(111)
ax.plot(x, y, 'k') #linestyle=':')
ax.plot(x_inter, y_inter, 'b')

ax.grid(True)                               #True = Grid wird angezeigt.



ax.set_xlabel('x_werte')
ax.set_ylabel('y_werte')
