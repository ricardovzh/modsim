#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 16:18:25 2021

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
d = 0.3     #Daempfung
t_max=5;    #Maximale Zeit
t=np.linspace(0, t_max,101)


#Anfangsbedingungen:
phi_0 = pi/4
x0=[phi_0, 0] 

   
#DGSystem 1 Ordung, die zu loesen ist:
def xdot_fkt_lin(t, x, *args):      #STANDARD Form: (Zeit, Zustandsgroessen) 
    xdot= [x[1], -g/l*x[0] - d*x[1]]     #Zustandsgroessen: [x1=Winkelgeschw, x0=Winkel]
    return xdot

    
def xdot_fkt_nichtLin(t, x, *args):      #STANDARD Form: (Zeit, Zustandsgroessen) 
    xdot= [x[1], -g/l*np.sin(x[0]) - d*x[1]]     #Zustandsgroessen: [x1=Winkelgeschw, x0=Winkel]
    return xdot



#DGL wird geloest:
sol_lin = solve_ivp(xdot_fkt_lin, [0, t_max], x0, t_eval=t, method='LSODA', args=(g, l))
 #solve_ivp(Dif Funktion, [Zeitspanne] , Anf. Bed., Loes.Methode, Argumente)
sol_nichtLin = solve_ivp(xdot_fkt_nichtLin, [0, t_max], x0, t_eval=t, method='LSODA', args=(g, l))


#Zuweisung der Werte,die uns interesieren:  
t=sol_lin.t                      #Zeit

x_lin=sol_lin.y                   #Zuweisung der Zustandsgroessen
x_nichtLin=sol_nichtLin.y

phi_lin=x_lin[0]                  #Winkel linear
phi_dot_lin=x_lin[1]              #Winkelgeschwindigkeit nichtlinear

phi_nichtLin=x_nichtLin[0]        #Winkel nichtlinear
phi_dot_nichtLin=x_nichtLin[1]    #Winkelgeschwindigkeit nichtlinear


#Plotting:
fig = plt.figure(1, figsize=(10,6)); fig.clf()
ax = fig.add_subplot(111)
ax.plot(t, phi_lin, label='$\phi$(t) linear', color='C0', linestyle='-', linewidth=2)
ax.plot(t, phi_nichtLin, label='$\phi$(t) nichtlinear', color='C1', linestyle='-', linewidth=2)
#ax.plot(t, phi_dot)
ax.grid("True")
ax.set_ylabel('Winkel $\phi$(t)/rad')
ax.set_xlabel('Time t/s')
ax.legend()                     #Erforderlich, so dass Legende angezeigt wird!
