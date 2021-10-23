# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 16:25:41 2021

Class: Modellbildung und Simulation
Unit: K2 A1 (Loesen mi Python)

@author: vari1011
"""
import matplotlib.pyplot as plt
import numpy as np
from numpy import pi as pi
from scipy.integrate import solve_ivp


#Variablen der DGL:
g = 9.81    #Erdbeschleunigung
l = 1.0     #Laenge des Zeiles
t_max=5;    #Maximale Zeit
t=np.linspace(0, t_max,101)


#Anfangsbedingungen:
phi_0 = pi/4
x0=[phi_0, 0] 

   
#DGSystem 1 Ordung, die zu loesen ist:
def xdot_fkt(t, x, *args):      #STANDARD Form: (Zeit, Zustandsgroessen) 
    xdot= [x[1],
           -g/l*x[0]]     #Zustandsgroessen: [x1=Winkelgeschw, x0=Winkel]
    return xdot


#DGL wird geloest:
sol = solve_ivp(xdot_fkt, [0, t_max], x0, t_eval=t, method='LSODA', args=(g, l))
 #solve_ivp(Dif Funktion, [Zeitspanne] , Anf. Bed., Loes.Methode, Argumente)


#Zuweisung der Werte,die uns interesieren:  
t=sol.t         #Zeit
x=sol.y
phi=x[0]        #Winkel
phi_dot=x[1]    #Winkelgeschwindigkeit


#Plotting:
fig = plt.figure(1, figsize=(10,6)); fig.clf()
ax = fig.add_subplot(111)
ax.plot(t, phi, 'b')
#ax.plot(t, phi_dot)
ax.grid("True")
ax.set_ylabel('Winkel $\phi$(t)/rad')
ax.set_xlabel('Time t/s')

