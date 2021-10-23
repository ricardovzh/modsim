from OMPython import ModelicaSystem
import matplotlib.pyplot as plt
from help_fkt import delete_OM_files

modelname='pt1_step'
mod=ModelicaSystem(modelname+'.mo',modelname)
mod.setSimulationOptions('stopTime=5.0')
#mod.setParameters('firstOrder1.k=2.0')
mod.simulate()

[t]=mod.getSolutions('time')
[phi]=mod.getSolutions('firstOrder1.y')
delete_OM_files(modelname)

fig=plt.figure(1, figsize=(10,6)); fig.clf()
plt.plot(t, phi, 'b')
plt.xlabel('t')
plt.grid()
plt.show()