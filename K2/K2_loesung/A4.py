from OMPython import ModelicaSystem
import matplotlib.pyplot as plt
from help_fkt import delete_OM_files
from numpy import pi as pi

cw=0.35; du=0.1; rho=1.188; m=1; l=1;
d=cw*rho*l*pi*du**2/(8*m)
modelname='pendel_block_lw'
mod=ModelicaSystem(modelname+'.mo',modelname)
mod.setSimulationOptions('stopTime=500.0')
mod.setParameters('gain2.k='+str(-d))
mod.simulate()
[t]=mod.getSolutions('time')
[phi]=mod.getSolutions('integrator2.y')
delete_OM_files(modelname)


fig=plt.figure(1, figsize=(10,6)); fig.clf()
ax = fig.add_subplot(111)
ax.plot(t, phi, 'b')
ax.grid()
ax.set_xlabel('t')
ax.set_ylabel('$\\varphi$') # \ bedeutet Sonderzeichen (z.B.: \n). Um ein \ zu bekommen:'\\'


