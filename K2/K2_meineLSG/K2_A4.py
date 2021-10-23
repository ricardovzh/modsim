#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 14:47:13 2021

Class: Modellbildung und Simulation
Unit: K2 A4 (Phy. Pendel mit Lufwiderstand)

@author: vazquez
"""


import matplotlib.pyplot as plt
from OMPython import ModelicaSystem
from help_fkt import delete_OM_files
from numpy import pi as pi

#Daempfungsparameter:
cw=0.35; r=0.05; rho=1.188; m=1; l=1;
d=cw*rho*l*pi*r**2/(l*m)


modelname='pendel_block_lw'
mod=ModelicaSystem(modelname+'.mo',modelname)
mod.setSimulationOptions('stopTime=20.0')
mod.setParameters('gain2.k='+str(-d))               #Parameter wird an OP weitergegeben.
mod.simulate()
[t]=mod.getSolutions('time')
[phi]=mod.getSolutions('integrator2.y')
[phi_dot]=mod.getSolutions('integrator1.y')
delete_OM_files(modelname)

fig=plt.figure(1, figsize=(10,6)); fig.clf()
ax = fig.add_subplot(111)
ax.plot(t, phi, 'b')
ax.plot(t, phi_dot)
ax.grid()
ax.set_xlabel('t')
ax.set_ylabel('$\\varphi$') # \ bedeutet Sonderzeichen (z.B.: \n). Um ein \ zu bekommen:'\\'

