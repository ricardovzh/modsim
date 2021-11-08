#import numpy as np 
from OMPython import ModelicaSystem
import matplotlib.pyplot as plt
from help_fkt import delete_OM_files
#from numpy import pi as pi

u_dach=2
f=1
R=20
L=9e-3
Cap=1000e-6

modelname='A4'
mod=ModelicaSystem(modelname+'.mo',modelname)
mod.setSimulationOptions('stopTime=0.1')
mod.setParameters('resistor1.R='+str(R))
mod.setParameters('inductor1.L='+str(L))
mod.setParameters('capacitor1.C='+str(Cap))
mod.simulate()
[t]=mod.getSolutions('time')
[u_a]=mod.getSolutions('inductor1.v')
[i_e]=-mod.getSolutions('constantVoltage1.i')
[i_c]=mod.getSolutions('capacitor1.i')
delete_OM_files(modelname)

fig=plt.figure(1, figsize=(10,6)); fig.clf()
ax = fig.add_subplot(111)
ax.plot(t, u_a, 'black')
ax.grid()
ax.set_ylabel('$u_a$')
ax.set_xlabel('$t$')
