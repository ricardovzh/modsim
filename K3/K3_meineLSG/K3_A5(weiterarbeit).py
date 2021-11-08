#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 19:34:10 2021

Class: Modellbildung und Simulation
Unit: K2 A5 (Weiterarbeit)

@author: vari1011
"""

import numpy as np 
#import scipy 
import matplotlib.pyplot as plt
from scipy import signal

L = 9e-3
C = 1000e-6
R = 20

#Berechnung Uebertragungsfunktion:
zaehler = np.array([L, 0])            #L*S
nenner = np.array([R*L*C, L, R])        #RLC*S^2 + L*S + R
G = signal.TransferFunction(zaehler, nenner)      #dt = sampling time in s.

#Berechnung Sprungantwort:
t1, y1 = signal.step(G)                 
w, A, phi = signal.bode(G)

#Berechnung Polen:
polen = G.poles                        
re = polen.real
im = polen.imag

##############################################################PLOT:
###PLOT_1 (Sprungantwort)
fig = plt.figure(1, figsize =(10,100)); fig.clf()
ax1 = fig.add_subplot(411)
ax1.plot(t1, y1, label = 'y', color = 'red')
ax1.set_xlim(0,0.1)
ax1.legend()
ax1.grid('true')

###PLOT_2 (Amplitudengang)                          #Vom Bodediagramm kann man ein Bandpassverhalten erkennen.
ax2 = fig.add_subplot(412)
ax2.plot(w, A, label = 'A', color = 'orange')
#ax2.loglog(basex=10, basey=1)
ax2.set_xscale('log')
ax2.set_xlim(100,1000)
ax2.set_ylim(-50,1)
ax2.legend()
ax2.grid('true')

###PLOT_3 (Phasengang)
ax3 = fig.add_subplot(413)
ax3.plot(w, phi, label = 'phi', color = 'blue')
#ax3.loglog(basex=10, basey=1)
ax3.set_xscale('log')
ax3.set_xlim(100,1000)
ax3.legend()
ax3.grid('true')

###PLOT_4 (Lage der Pole)
ax4 = fig.add_subplot(414)
ax4.scatter(re, im, label = 'Pole', color = 'red')
#ax2.loglog(basex=10, basey=1)
#ax3.set_xscale('log')
ax4.set_xlim(-30,30)
ax4.set_ylim(-420,420)
ax4.legend()
ax4.grid('true')


