from OMPython import ModelicaSystem
import matplotlib.pyplot as plt
from help_fkt import delete_OM_files

modelname='pendel_block_damp'
mod=ModelicaSystem(modelname+'.mo',modelname)
mod.setSimulationOptions('stopTime=5.0')
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


