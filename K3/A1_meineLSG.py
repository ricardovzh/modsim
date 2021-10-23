import numpy as np 
#import scipy 
import matplotlib.pyplot as plt
from numpy import pi as pi
from scipy.integrate import solve_ivp

u_dach=2
f=1
R=20
L=9e-3
Cap=1000e-6

t_max=2
Delta_t=1e-3
t=np.linspace(0, t_max, int(t_max/Delta_t)+1)

A=np.array([[-1/(R*Cap), -1/Cap],       #Aus Systemmatrix
            [1/L,         0    ]])
B=np.array([[1/(R*Cap)],                #Aus Systemmatrix
               [0]])

C=np.array([[   1,  0],                 #Aus Ausgangsmatrix
            [   0,  1],
            [ -1/R, 0]])
D=np.array([[  0],                      #Aus Ausgangsmatrix
            [  0],
            [1/R]])


def xdot_fkt(t, x):                     #x wird hier implizit als Zustandsgroessenvektor eingegeben.
    x=np.reshape(x, (2,1))              #x[0] = Abl. der Spannung am Kond || x[1] = Abl. der Strom durch L.
                                        #Diese Anordung wurde in der Berechnung (siehe Doku) arb. festgestellt.
    xdot = np.dot(A,x) + B*u_dach*np.sin(2*np.pi*f*t) #Achtung! Matrizenmulti. mit np.dot().

    xdot=np.reshape(xdot, (1,2))        #Umwandlung in erwartete Gestalt (1x2 Matrix)
    return xdot

u_a_0=0; i_l_0=0 # Anfangswerte
x0=np.array([u_a_0, i_l_0])

sol = solve_ivp(xdot_fkt, [0, t_max], x0, t_eval=t, method='LSODA')
x=sol.y;    #In x werden die Zustandsgr. in Abhaengigkeit der Zeit gespeichert.
# Ergänzen Sie hier die Gleichung zur Berechnung der Ausgangsgrößen
y = np.dot(C,x) + D*u_dach*np.sin(2*np.pi*f*t)

u_a=y[0]; i_c=y[2]-y[1]; i_e=y[2]       #i_c wird so beschrieben, da i_L = y[1]

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
