import numpy as np 
from OMPython import ModelicaSystem
import matplotlib.pyplot as plt
from help_fkt import delete_OM_files
from numpy import pi as pi

u_dach=2
f=1
modelname='A2'
mod=ModelicaSystem(modelname+'.mo',modelname)
mod.setSimulationOptions('stopTime=2.0')
mod.simulate()
[t]=mod.getSolutions('time')
[u_a]=mod.getSolutions('u_a')
[i_e]=mod.getSolutions('i_e')
[i_L]=mod.getSolutions('i_L')
i_c=i_e-i_L
delete_OM_files(modelname)

fig=plt.figure(1, figsize=(10,6)); fig.clf()
ax = fig.add_subplot(211)
ax.plot(t, u_a, 'black')
ax.plot(t, i_c, 'r')
ax.grid()
ax.set_ylabel('$u_a, i_c$')
ax = fig.add_subplot(212)
ax.plot(t, 10*i_e, 'red')
ax.plot(t, u_dach*np.sin(2*pi*f*t), 'darkgreen')
ax.set_ylabel('$u_e, 10 \cdot i_e$')
ax.set_xlabel('t')
ax.grid()
