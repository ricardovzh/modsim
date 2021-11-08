#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 21:09:47 2021

Class: Modellbildung und Simulation
Unit: K2 A1 (Loesen mit Python)

@author: vari1011
"""

import matplotlib.pyplot as plt
from OMPython import ModelicaSystem
from help_fkt import delete_OM_files

L=9e-3
Cap=1000e-6

modelname='RLC_schwingkreis'
mod=ModelicaSystem(modelname+'.mo',modelname)
mod.setSimulationOptions('stopTime=2.0')
mod.simulate()
#Zustandsgroessen:
[u_a]=mod.getSolutions('u_a')
[i_L]=mod.getSolutions('i_L')
[i_c]=Cap*mod.getSolutions('der(u_a)')      #Achtung! Multiplikation i_c = Cap*der(u_a) muss noch durchgefuehrt werden!
#Eingangsgroessen:
[t]=mod.getSolutions('time')
[u_e]=mod.getSolutions('u_e')
[i_e]=mod.getSolutions('i_e')
delete_OM_files(modelname)

##################################################################PLOT:
fig=plt.figure(1, figsize=(10,6)); fig.clf()
ax1 = fig.add_subplot(211)
ax1.plot(t, u_a, label = 'u_a',color='black')
#ax1.plot(t, i_L, label = 'i_L', color='r')
ax1.plot(t, i_c, label = 'i_c', color='blue')
ax1.set_ylabel('$u_a, i_c$')
ax1.grid('true')
ax1.legend()


ax2 = fig.add_subplot(212)
ax2.plot(t, 10*i_e, label = '10*i_e',color= 'red')
ax2.plot(t, u_e, label = 'u*sin(w*t)',color= 'darkgreen')
ax2.set_ylabel('$u_e, 10 \cdot i_e$')
ax2.set_xlabel('t')
ax2.grid('true')
ax2.legend()
